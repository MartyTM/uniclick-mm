import socket
import sys
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while(1):
            client, addr = self.sock.accept()
            client.settimeout(60)
            thr = threading.Thread(target=self.listenToClient,
                                   args=(client, addr))
            thr.daemon = True
            thr.start()

    def listenToClient(self, client, addr):
        size = 4096
        while(1):
            try:
                recv_msg = client.recv(size)
                if recv_msg:
                    resp_msg = "Received: " + recv_msg
                    client.send(resp_msg)
                else:
                    print("Client disconnected")
                    raise
            except:
                client.close()
                return False


if __name__ == "__main__":
    port = 8080
    host = socket.gethostname()
    Server(host, port).listen()
