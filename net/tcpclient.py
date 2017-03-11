import socket
import sys

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)
host, port = "45.55.163.153", 8080

sock.connect((host, port))
print("1 - LOGIN - Login, duh")
print("2 - RGSTR - Register user")
print("3 - CHKLG - Check Login Status")
print("4 - LGOUT - Log out user")
opt = input("Enter an option to send to server:")

if opt == '1':
    print("User login...")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    sock.sendall(bytes("LOGIN", "utf-8"))
    sock.sendall(bytes(username, "utf-8"))
    sock.sendall(bytes(password, "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    if received == "OK":
        print("SUCCESS")
elif opt == '2':
    print("Checking user login...")
    sock.sendall(bytes("CHKLG", "utf-8"))
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
    sock.sendall(bytes("LGOUT", "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    if received == "OK":
        print("SUCCESS")
else:
    print("Invalid input!!")

print("Sent:     {}".format(data))
print("Received: {}".format(received))


