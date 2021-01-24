import socketserver
import _thread
import logging

server = None

def prepare(ip, port, handler):
    logging.debug("Preparing tcp server...")
    global server

    
    if server is not None:
        logging.debug("Server is already running!")
        return

    addr = (ip, port)

    server = socketserver.ThreadingTCPServer(addr,handler)
    #server = socketserver.TCPServer(addr,handler)
    server.allow_reuse_address = True
    _thread.start_new_thread(_start_server,())
    
def _start_server():
    logging.debug("Starting tcp server...")
    global server
    server.serve_forever()

def stop_server():
    global server
    if server is not None:
        server.shutdown()
        server.server_close()
        server = None