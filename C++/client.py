import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 54288
connection.connect((HOST, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
connection.send("И тебе привет!".encode('utf8'))
connection.close()