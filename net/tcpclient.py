import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cmd = "LOGIN"
host, port = "45.55.163.153", 8080

try:
    sock.connect((host, port))
    sock.sendall(bytes(cmd, 'utf-8'))
    received = str(sock.recv(1024), 'utf-8')
    sock.sendall(bytes("mmarshal", 'utf-8'))
    sock.sendall(bytes("bluepolo", 'utf-8'))
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))


