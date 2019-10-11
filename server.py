import socket
import json
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)  # max backlog of connections

print ('Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection(client_socket):
    request = client_socket.recv(2024)
    survey = str(request)
    results = survey.replace('\\n', '\n')
    i = 0
    print(results);
    

    response_body = [
            '<html><body><h1>Hello, world!</h1><PRE>' + results
        ]
    response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': len(response_body),
            'Connection': 'close',
        }
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK' # this can be random

        # sending all this stuff
    client_sock.send('HTTP/1.1 200 OK\n\r\n\r\n'.encode() )

    client_socket.close()

while True:
    client_sock, address = server.accept()
    print ('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    client_handler.start()

