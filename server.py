import socket
import requests

r = requests.get("https://ramziv.com/ip").text
print(r)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)

server.bind(('127.0.0.1', 1111))

server.listen()

while True:
    user_socket, address = server.accept()
    user_socket.send('You are connected'.encode('utf-8'))

