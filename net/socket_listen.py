import socket
import sys
from thread import *

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    socket.bind((host, port))