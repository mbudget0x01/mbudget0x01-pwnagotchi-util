import socket

def receive_data(tcp_socket:socket.socket, size:int) -> bytes:
    data = bytearray()
    while len(data) < size:
        packet = tcp_socket.recv(size - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data