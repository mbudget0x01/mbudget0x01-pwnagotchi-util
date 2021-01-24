import socket
import packages.coordinator_api.request_builder as builder
import packages.coordinator_api.request_parser as parser
from packages.coordinator_api.request_results import request_results

#Client side
def send_request(tcp_socket:socket.socket, request_builder:builder.request_builder) -> parser.request_parser:
    req = request_builder.build()
    tcp_socket.send(req)
    resp = tcp_socket.recv(1024)
    my_parser = parser.request_parser(resp)
    if my_parser.request_handled is None:
        raise Exception("Request not Handled!")
    return my_parser

#server side if you just want to ack e.g. broadcast
def handle_request(request:bytes, request_result) -> bytes:
    if not isinstance(request_result,request_results):
        raise TypeError("request result must be in enum request_results")
    my_parser = parser.request_parser(request)
    my_builder = my_parser.get_builder()
    my_builder.set_request_result(request_result.value)
    return my_builder.build()

