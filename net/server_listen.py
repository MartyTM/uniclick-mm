import MySQLdb

class User:
    userCount = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLoggedIn = false

    def login(self, db):
        cur = db.cursor()
        cur.execute()    
    def register(self, db):
    
    def __del__(self):
        usercount -= 1



if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user="uniclick", 
                        password="bluepolo", db="uniclick")
    db.close()

