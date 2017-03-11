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
            self.username = input("Enter a username: ")
            self.password = input("Enter a password: ")
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
    users = []
    session = 0

    def __init__(self, request, client_address, server):
        db = MySQLdb.connect(host="localhost", user="uniclick",
                             passwd="bluepolo", db="uniclick")
        self.session = TCP_handler.session
        TCP_handler.users.append(User(db))
        TCP_handler.session += 1

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

    def __del__(self):
        del TCP_handler.users[self.session]


if __name__ == "__main__":
    host, port = "45.55.163.153", 8080
    server = socketserver.TCPServer((host, port), TCP_handler)
    server.serve_forever()

