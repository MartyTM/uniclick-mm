import MySQLdb
import socketserver


class User:
    userCount = 0

    # Might be better to init uname and pword to None type
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

    def register(self):
        cur = self.db.cursor()
        select_stmt = "select username,password from user_auth \
                        where username=\"{0}\""
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.id = input("Enter you student ID number: ")
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
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        data_str = self.data.decode("utf-8")
        print(data_str)
        if data_str == "LOGIN":
            username = self.request.recv(1024).strip()
            password = self.request.recv(1024).strip()
            TCP_handler.users[self.client_addres].login(username, password)
        else:
            pass

    def finish(self):
        del TCP_handler.users[self.client_address]


if __name__ == "__main__":
    host, port = "45.55.163.153", 8080
    server = socketserver.TCPServer((host, port), TCP_handler)
    server.serve_forever()

