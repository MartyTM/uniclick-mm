import socket

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
host = "45.55.163.153"
port = 8080
sock.connect((host, port))

def 