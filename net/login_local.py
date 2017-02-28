import MySQLdb


class User:
    userCount = 0

    # Might be better to init uname and pword to None type
    def __init__(self, db, uname=None, pword=None):
        self.isLoggedIn = False
        self.username = uname
        self.password = pword
        self.db = db
        self.userCount += 1

    def login(self):
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


if __name__ == "__main__":
    users = []
    session = 0
    db = MySQLdb.connect(host="localhost", user="uniclick",
                         passwd="bluepolo", db="uniclick")

    print("Welcome to the UniClick login page")
    while(1):
        users.append(User(db))
        print("You are session number: " + str(session))
        print("What would you like to do?")
        print("1 - Login\n2 - Check Login Status\n3 - Register")
        print("4 - Logout\n5 - Start a New Session\n6 - Close Session\n")
        opt = input("Select an Option: ")
        print("\n")
        if opt == '1':
            print("User login...")
            users[session].login()
        elif opt == '2':
            print("Checking user login...")
            if users[session].checkLogin():
                print("User is Logged in!")
                print("Logged in as user: " + users[session].username)
            else:
                print("User is NOT Logged in!")
        elif opt == '3':
            print("User registration...")
            users[session].register()
        elif opt == '4':
            print("Logging out")
            users[session].logout()
        elif opt == '5':
            print("Opening new session...")
            session += 1
        elif opt == '6':
            print("Closing session...")
            del users[session]
            session -= 1
            if session < 0:
                break
        else:
            print("Invalid input!!")

    db.close()

