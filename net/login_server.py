import MySQLdb
import socketserver


class User:
    userCount = 0

    def __init__(self, db, uname=None, pword=None):
        self.isLoggedIn = False
        self.username = uname
        self.password = pword
        self.db = db
        self.userCount += 1

    def login(self, uname, pword):
        if self.isLoggedIn is True:
            print("User is already logged in!!")

        else:
            self.username = uname
            self.password = pword
            cur = self.db.cursor()
            select_stmt = "select username,password from user_auth \
                           where username=\"{0}\""
            cur.execute(select_stmt.format(self.username))
            for username, password in cur.fetchall():
                if self.password != password:
                    print("Password is incorrect!!")
                elif self.password == password:
                    print("Logged in as user: " + username)
                    self.isLoggedIn = True

    def checkLogin(self):
        if self.isLoggedIn is True:
            return True
        else:
            return False

    def logout(self):
        self.isLoggedIn = False

    def register(self, uname, pword, ident):
        cur = self.db.cursor()
        select_stmt = "select username,password from user_auth \
                        where username=\"{0}\""
        self.username = uname
        self.password = pword
        self.id = ident
        if self.isLoggedIn is True:
            print("User is already logged in!!")

        elif cur.execute(select_stmt.format(self.username)) == 1:
            print("User already registered")

        else:
            insert_stmt = "insert into user_auth (username, password, id) \
                           values(\"{0}\", \"{1}\", {2})"

            cur.execute(insert_stmt.format(
                        self.username, self.password, self.id))
            self.db.commit()
            print("Registered user: " + uname)

    def __del__(self):
        self.userCount -= 1


class TCP_handler(socketserver.BaseRequestHandler):
    users = {}

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()

        db = MySQLdb.connect(host="localhost", user="uniclick",
                             passwd="bluepolo", db="uniclick")
        TCP_handler.users.update({self.client_address: User(db)})
        print(TCP_handler.users)

        try:
            self.handle()
        finally:
            self.finish()

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            data_str = self.data.decode("utf-8")
            print(data_str)
            self.request.sendall(self.data.upper())
            if data_str == "LOGIN":
                username = self.request.recv(1024).strip()
                print(username)
                self.request.sendall(username.upper())
                password = self.request.recv(1024).strip()
                print(password)
                self.request.sendall(password.upper())
                username = username.decode("utf-8")
                password = password.decode("utf-8")
                TCP_handler.users[
                    self.client_address].login(username, password)
                if TCP_handler.users[self.client_address].isLoggedIn is True:
                    print("Login successful")
                else:
                    print("Login unsuccessful")

            elif data_str == "CHKLG":
                self.request.recv(1024).strip()
                if TCP_handler.users[self.client_address].checkLogin() is True:
                    self.request.sendall(bytes("TRUE", 'utf-8'))
                else:
                    self.request.sendall(bytes("FALSE", 'utf-8'))

            elif data_str == "RGSTR":
                username = self.request.recv(1024).strip()
                print(username)
                self.request.sendall(username.upper())
                password = self.request.recv(1024).strip()
                print(password)
                self.request.sendall(password.upper())
                stud_id = self.request.recv(1024).strip()
                print(stud_id)
                self.request.sendall(stud_id.upper())
                username = username.decode("utf-8")
                password = password.decode("utf-8")
                stud_id = stud_id.decode("utf-8")
                TCP_handler.users[
                    self.client_address].register(username, password, stud_id)

            elif data_str == "LGOUT":
                TCP_handler.users[self.client_address].logout()

            elif data_str == "EXIT":
                break
            else:
                pass

    def finish(self):
        del TCP_handler.users[self.client_address]


if __name__ == "__main__":
    host, port = "45.55.163.153", 8080
    server = socketserver.TCPServer((host, port), TCP_handler)
    server.serve_forever()
