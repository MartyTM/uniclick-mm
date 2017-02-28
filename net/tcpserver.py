import socketserver


class TCP_handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        data_str = self.data.decode("utf-8/")
        print(data_str)
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    host = "45.55.163.153"
    port = 8080

    server = socketserver.TCPServer((host, port), TCP_handler)
    server.serve_forever()
