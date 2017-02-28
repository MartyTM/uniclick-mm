import socketserver
import socket


class TCP_handler:
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    host = socket.gethostname()
    port = 8080

    with socketserver.TCPServer((host, port), TCP_handler) as server:
        server.server_forver()
