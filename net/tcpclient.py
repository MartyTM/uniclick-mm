import socket

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
host, port = "45.55.163.153", 8080

sock.connect((host, port))
while True:
    received = str(sock.recv(1024), "utf-8")
    print("Received: {}".format(received))
    send = input()
    sock.sendall(bytes(send, "utf-8"))


