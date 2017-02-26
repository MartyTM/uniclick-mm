import MySQLdb

class User:
    userCount = 0

    # Might be better to init uname and pword to None type
    def __init__(self, db, uname=None, pword=None):
        self.isLoggedIn = false
        self.username = uname
        self.password = pword
        self.db = db
        userCount += 1

    def login(self):
        if self.isLoggedIn == true:
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
                    self.isLoggedIn = true
    
    def checkLogin(self):
        if self.isLoggedIn = true:
            return true
        else
            return false
    
    def logout(self):
        self.isLoggedIn = false
                
    def register(self, db):
        cur = self.db.cursor()
        select_stmt = "select username,password from user_auth \
                        where username=\"{0}\""
        if self.isLoggedIn == true:
            print("User is already logged in!!")
        
        elif cur.execute(select_stmt.format(self.username)) != 1:
            print("User already registered")

        else:
            self.username = input("Enter a username: ")
            self.password = input("Enter a password: ")
            self.id = input("Enter you student ID number: ")
            insert_stmt = "insert into user_auth (username, password, id) \
                           values(\"{0}\", \"{1}\", {2})"

            cur.execute(insert_stmt.format(self.username, self.password, self.id))
            self.db.commit()

    def __del__(self):
        usercount -= 1



if __name__ == "__main__":
    users = []
    session = 0
    db = MySQLdb.connect(host="localhost", user="uniclick", 
                        passwd="bluepolo", db="uniclick")
    
    while(1):
    # Main menu 
        print("Welcome to the UniClick login page")
        while(1):
            users.append(User(db))
            print("You are session number: " + str(session))
            print("What would you like to do?")
            print("1 - Login \n 2 - Check Login Status \n 3 - Register")
            print("4 - Logout \n 5 - Start a New Session \n 6 - Close Session")
            opt = input("Select an Option: ")
            if opt = 1:
                print("User login...")
                users(session).login()
            elif opt = 2:
                if users(session).checkLogin():
                    print("User is Logged in!")
                else
                    print("User is NOT Logged in!")
            elif opt = 3:
                user(session).register()
            elif opt = 4:
            elif opt = 5:
            else:

    
    db.close()

