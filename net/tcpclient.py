import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data = "test"
host, port = "45.55.163.153", 8080

try:
    sock.connect((host, port))
    sock.sendall(data + "\n")
    received = sock.recv(1024)
finally:
    sock.close()

print("Sent:    {}".format(data))
print("Received:{}".format(received))


