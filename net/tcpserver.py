import socketserver
import socket


class TCP_handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    host = socket.gethostbyname(socket.gethostname())
    port = 8080

    server = socketserver.TCPServer((host, port), TCP_handler)
    server.serve_forever()
