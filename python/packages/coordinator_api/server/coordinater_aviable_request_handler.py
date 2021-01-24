import packages.log.log as log
import packages.coordinator_api.client.tcp_file_transfer as tcp_file_transfer
import packages.coordinator_api.request_types as request_types
import packages.coordinator_api.tcp_request as tcp_request
from packages.coordinator_api.request_builder import request_builder
from packages.coordinator_api.request_parser import request_parser


from socketserver import BaseRequestHandler


class coordinater_aviable_request_handler(BaseRequestHandler):
    def handle(self):
        log.log_debug("Broadcast receifed from: "+ self.client_address[0])
        raw_msg = self.request[0]
        parser = request_parser(raw_msg)

        if parser.request_type != request_types.request_types.COORDINATOR_AVIABLE.value:
            log.log_debug("Request with message: " + parser.request_type + " ignored")
            return
        if parser.request_handled != "":
            log.log_debug("Ignoring handled udp request.")
            return
        log.log_debug("Valid service request...")
        my_ip = self.server.server_address[0]
        log.log_debug("On Server-side ip: " + str(my_ip))
        client_ip = parser.request_data
        
        socket = self.request[1]
        resp = tcp_request.handle_request(raw_msg,tcp_request.request_results.ACK)
        socket.sendto(resp, self.client_address)
        log.log_info("initiating communication with: " + client_ip)
        tcp_file_transfer.initiate_file_transfer(client_ip, 5556)