import socket,time


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080


# initialize Socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
# AF_INET --> specify the IPv4 address
# SOCK_STREAM --> for TCP Socket (Transmission Control Protocol)
# SOCK_DGRAM --> for UDP Socket (User Datagram Protocol)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.setblocking(False)


# Binding Socket to IP address & Port
server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT}")

while True:
    try:
        client_socket, client_address = server_socket.accept()
        print(client_address)
        print(client_socket)
    except:
        time.sleep(1)
        continue