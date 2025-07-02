import socket, time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# initialize Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# AF_INET --> specify the IPv4 address
# SOCK_STREAM --> for TCP Socket (Transmission Control Protocol)
# SOCK_DGRAM --> for UDP Socket (User Datagram Protocol)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding Socket to IP address & Port
server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)
    
    # Returns HTTP response
    headers = request.split('\n')
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == 'GET':
        if path == '/':
            fin = open('index.html')
        elif path == '/book':
            fin = open('book.json')
        else:
            # handle the edge case
            pass
    
        content = fin.read()
        fin.close()
        response = 'HTTP/1.1 200 OK\n\n' + content
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'

    client_socket.sendall(response.encode())

    # Close connection - show what happens if the client socket
    # is not closed.
    client_socket.close()

# Close socket
server_socket.close()