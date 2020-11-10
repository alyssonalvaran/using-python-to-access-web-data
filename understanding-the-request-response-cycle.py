import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
connection.send(command)

while True:
    data = connection.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
connection.close()