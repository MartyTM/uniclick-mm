import MySQLdb

class User:
    userCount = 0

    def __init__(self):
        self.isLoggedIn = false
        userCount += 1

    def login(self, db):
        if self.isLoggedIn == true:
            print("User is already logged in!!")
        
        else:
            cur = db.cursor()
            select_stmt = "select username,password from user_auth \
                           where username=\"{0}\""
            cur.execute(select_stmt.format(username))
            
            for username, password in cur.fetchall():
                if self.password != password:
                    print("Password is incorrect!!")
                elif self.password == password:
                    print("Logged in as user: " + username)
                    self.isLoggedIn = true
                
    def register(self, db):
        if self.isLoggedIn == true:
            print("User is already logged in!!")
        
        else:
            self.username = "Enter a username: "
            self.password = "Enter a password: "
            cur = db.cursor()
            insert_stmt = "select username,password from user_auth \
                           where username=\"{0}\""
            cur.execute(insert_stmt.format(username,password))
            

    def __del__(self):
        usercount -= 1



if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user="uniclick", 
                        passwd="bluepolo", db="uniclick")

    # Main menu 
    print("Enter a username and password to login")
    username = input("Enter a Username: ")
    password = input("Enter a Password: ")

    
    db.close()

