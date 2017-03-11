import socket

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
host, port = "45.55.163.153", 8080

sock.connect((host, port))
while True:
    send = input("Enter something to send to the server: ")
    sock.sendall(bytes(send, "utf-8"))


