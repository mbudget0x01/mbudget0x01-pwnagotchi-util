import packages.log.log as log
import packages.session.file_system as file_system
import packages.tcp.tcp_data_transfer as tcp_data_transfer
import packages.coordinator_api.tcp_request as tcp_request
import packages.coordinator.workload_looper as workload_looper

from packages.coordinator_api.request_builder import request_builder as builder
from packages.coordinator_api.request_types import request_types as request_types
from packages.coordinator_api.request_results import request_results as request_results
from packages.coordinator_api.request_parser import request_parser as request_parser

import os
import socket
import json

def initiate_file_transfer(server_ip, port):
    log.log_info("Initiating file transfer...")    
    s = connect_new_client_socket(server_ip, port)
    data = request_file_list_data(s)
    if data is None:
        raise Exception("Invalid response.")
    file_list = json.loads(data)
    log.log_info("Received " + str(len(file_list)) + " file names.")
    s.close()

    existing_files = _get_existing_files()

    new_files = []

    file_counter = 0
    for f in file_list:
        if f in existing_files:
            log.log_debug("Skipping file " + f +" as it already exists.")
            continue
        sock = connect_new_client_socket(server_ip, port)
        file_data = request_file(sock,f)
        if file_data is not None:
            _save_file(file_data, f)
            file_counter += 1
            log.log_debug("New File received: " + f)
            new_files.append(f)
        sock.close()
    log.log_info_line()
    log.log_info("Finished file transfer, added " + str(file_counter) + " files")

    _generate_workloads(new_files)


def request_file_list_data(tcp_socket:socket.socket) -> str:
    #sending and handling file list request
    my_builder = builder().set_request_type(request_types.FILE_LIST.value)
    file_list_resp_parser = tcp_request.send_request(tcp_socket ,my_builder)
    if file_list_resp_parser.request_handled != request_results.ACK.value:
        log.log_warning("File list request denied!")
        return ""
    
    #waiting for incoming data segment identifier
    resp = tcp_socket.recv(1024)
    parser = request_parser(resp)
    if parser.request_type == request_types.DATA_SEGMENT.value:
        #data segment is valid -> return ack
        handled_identifier = parser.get_builder().set_request_result(request_results.ACK.value).build()
        tcp_socket.send(handled_identifier)
        #receive raw data
        data = tcp_data_transfer.receive_data(tcp_socket, int(parser.request_data))
        return data.decode("utf-8")
    return None

def request_file(tcp_socket:socket.socket, file_name:str) -> bytes:
    log.log_debug("Requesting File: " + file_name)
    request = builder().set_request_type(request_types.FILE.value).set_request_data(file_name).build()
    tcp_socket.send(request)
    resp = tcp_socket.recv(1024)
    parser = request_parser(resp)
    if parser.request_type == request_types.DATA_SEGMENT.value:
        handled_segment = parser.get_builder().set_request_result(request_results.ACK.value).build()
        tcp_socket.send(handled_segment)
        data = tcp_data_transfer.receive_data(tcp_socket, int(parser.request_data))
        log.log_debug("Received content of " + file_name)
        return data
    return None

def _save_file(content:bytes, file_name:str):
        folder = file_system.getBacklogPath()
        file = os.path.join(folder, file_name)
        with open(file, 'wb') as out_file:
            out_file.write(content)

def connect_new_client_socket(server_ip:str, port:int) -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log.log_debug("Connecting...")
    s.connect((server_ip, port))

    log.log_debug("Connected to: " + server_ip)
    return s

def _get_existing_files() -> [str]:
    folder = file_system.getBacklogPath()
    return os.listdir(folder)

def _generate_workloads(files:list):
    log.log_debug("Adding new files to workload")
    wl = workload_looper.workload_looper.getInstance()
    wl.add_workload(files)
    
