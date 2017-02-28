import socket
import sys

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
host, port = "45.55.163.153", 8080
data = " ".join(sys.argv[1:])

sock.connect((host, port))
sock.sendall(bytes(data + "\n", "utf-8"))
received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))


