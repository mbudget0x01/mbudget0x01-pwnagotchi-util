""" 
#############################################
#  Debug Purposes only 
#############################################
"""

import packages.tcp.tcp_server as tcp_server
import packages.coordinator_api.server.tcp_file_request_handler as tcp_file_request_handler
import packages.coordinator_api.client.coordinator_aviable_request as coordinator_aviable_request

def main():
    tcp_server.prepare('',5556,tcp_file_request_handler.tcp_file_request_handler)
    print("main")
    coordinator_aviable_request.broadcast_request()
    while True:
        pass

if __name__ == "__main__":
    main()