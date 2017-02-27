import socket

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
sock.connect((host, port))

def 