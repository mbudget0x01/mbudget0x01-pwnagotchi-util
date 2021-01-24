from packages.coordinator_api.request_builder import request_builder as request_builder
from packages.coordinator_api.request_parser import request_parser as request_parser
from packages.coordinator_api.request_types import request_types
from packages.coordinator_api.request_results import request_results
import socket
import struct
import logging

def broadcast_request(host_ip=None):
    PORT = 5555


    cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    #prepare data
    if host_ip is None:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    else:
        host_ip = host_ip
    
    logging.info("IP: " + str(host_ip))

    data = request_builder().set_request_type(request_types.COORDINATOR_AVIABLE.value).set_request_data(host_ip).build()

    addr = ('', PORT)
    cs.bind(addr)
    cs.sendto(data,('255.255.255.255', PORT))

    resp = None
    while resp == None:
        
        recv_data, addr = cs.recvfrom(1024)
        logging.info("[UDP] Received message: %s"%recv_data)
        parser = request_parser(recv_data)
        if parser.request_handled == request_results.ACK:
            resp = True
        if parser.request_handled == "":
            logging.info("[UDP] Ignoring loopback.")

    cs.close()
