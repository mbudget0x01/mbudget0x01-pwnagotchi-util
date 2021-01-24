from socketserver import BaseRequestHandler
from packages.coordinator_api.request_types import request_types
from packages.coordinator_api.request_builder import request_builder
from packages.coordinator_api.request_results import request_results
import packages.coordinator_api.request_parser as request_parser
import packages.pwnagotchi_plugin.file_list as file_list
import packages.coordinator_api.server.load_file_data as file_data
import packages.coordinator_api.tcp_request as tcp_request
import logging

import os

handshakes_path = "/root/handshakes/"

class tcp_request_handler(BaseRequestHandler):

    def handle(self):
        logging.debug("Handle tcp request")
        msg = self.request.recv(1024)
        my_request_parser = request_parser.request_parser(msg)
        request_type = my_request_parser.request_type
        logging.debug("Received request of type: " + request_type)
        if request_type == request_types.FILE_LIST.value:
            socket = self.request
            #generating json data
            #path = os.path.dirname(os.path.realpath(__file__))
            #path = os.path.join(path, "test")
            path = os.path.realpath(handshakes_path)
            fl = file_list.generate_file_list_json(path)
            json = fl.encode("utf-8")
            # request handling

            #handle file list request
            handled_request = tcp_request.handle_request(msg, request_results.ACK)
            socket.send(handled_request)
            #send data segment meta
            data_segment_request_builder = request_builder().set_request_type(request_types.DATA_SEGMENT.value).set_request_data(str(len(json)))
            data_segment_request_parser = tcp_request.send_request(socket, data_segment_request_builder)
            if data_segment_request_parser.request_handled != request_results.ACK.value:
                logging.warning("File List: Data Segment not accepted")
                return

            #send raw data
            socket.send(json)

        elif request_type == request_types.FILE.value:
            socket = self.request
            file_name = my_request_parser.request_data
            #get file
            #path = os.path.dirname(os.path.realpath(__file__))
            #path = os.path.join(path, "test")
            #path = os.path.join(path, file_name)
            path = os.path.realpath(handshakes_path)
            path = os.path.join(path, file_name)
            data = file_data._load_file_data(path)
            data_segment_identifier = request_builder().set_request_type(request_types.DATA_SEGMENT.value).set_request_data(str(len(data))).build()
            socket.send(data_segment_identifier)
            data_segment_identifier_resp = socket.recv(1024)
            result = request_parser.request_parser(data_segment_identifier_resp)
            if result.request_handled == request_results.ACK.value:
                socket.send(data)
            
        else:
            logging.warning("Invalid request received")        
            socket = self.request #[0]
            socket.send("Invalid request".encode("utf-8"))
