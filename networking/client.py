import socket

sock = socket.socket()
server_addr = ('0.0.0.0', 9090)
sock.connect(server_addr)
sock.send('Hello, world!')

data = sock.recv(1024)
sock.close()

print data
