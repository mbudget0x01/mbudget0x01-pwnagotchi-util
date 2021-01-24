import packages.log.log as log
from socketserver import BaseRequestHandler, UDPServer, ThreadingUDPServer



server = None

class Debug_Handler(BaseRequestHandler):
    def handle(self):
        log.log_debug("Message: " + self.request[0].decode("utf-8"))
        log.log_debug("IP: " + self.client_address[0])
        log.log_debug("Port: " + str(self.client_address[1]))
        socket = self.request[1]
        socket.sendto(b"hello", self.client_address)

def start_listening(listening_port, handler):
    global server
    
    if server is not None:
        log.log_warning("Server is already listening.")
        return
   
    addr = ("", listening_port)
    log.log_debug("listening on %s:%s" % addr)
    server = ThreadingUDPServer(addr,handler)
    server.allow_reuse_address = True
    server.serve_forever()