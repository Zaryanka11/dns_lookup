import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 54288
listener.bind((HOST, PORT))
listener.listen(0)

connection, address = listener.accept()

connection.send("Привет, подкючайся!".encode('utf8'))

connection.send("Привет!".encode('utf8'))
while True:
  data_output = ''
  while True:
    data = connection.recv(1024).decode("utf8")
    data_output+=data
    if not data:
      break

  print(data_output)