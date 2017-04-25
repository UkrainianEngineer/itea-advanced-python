import socket

sock = socket.socket()
# Bind socket into 0.0.0.0:9090.
server_addr = ('0.0.0.0', 9090)
sock.bind(server_addr)
# Listen socket for maximum 1 connection.
sock.listen(1)

while True:
    print 'waiting for connection...'
    # Accept connection.
    conn, addr = sock.accept()

    print 'connected: ', addr

    # Receive data from client by small parts 1024 bites.
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())
    conn.close()

