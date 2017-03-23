import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "45.55.163.153", 8080

try:
    sock.connect((host, port))
    print("Welcome to UniClick!")
    while True:
        print("What would you like to do?")
        print("1 - Login\n2 - Check Login Status\n3 - Register")
        print("4 - Logout\n5 - Close Session\n")
        opt = input("Select an Option: ")
        print("\n")

        if opt == '1':
            cmd = "LOGIN"
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            sock.sendall(bytes(cmd, 'utf-8'))
            received = str(sock.recv(1024), 'utf-8')
            sock.sendall(bytes(username, 'utf-8'))
            uname_recv = str(sock.recv(1024), 'utf-8')
            sock.sendall(bytes(password, 'utf-8'))
            pword_recv = str(sock.recv(1024), 'utf-8')

        elif opt == '2':
            cmd = "CHKLG"
            sock.sendall(bytes(cmd, 'utf-8'))
            received = str(sock.recv(1024), 'utf-8')
            sock.sendall(bytes("READY", 'utf-8'))
            login_bool = str(sock.recv(1024), 'utf-8')
            if login_bool == "TRUE":
                isLoggedIn = True
                print("User is logged in")
            if login_bool == "FALSE":
                isLoggedIn = False
                print("User is NOT logged in")

        elif opt == '3':
            cmd = "RGSTR"
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            stud_id = input("Enter your student ID number: ")
            sock.sendall(bytes(cmd, 'utf-8'))
            received = str(sock.recv(1024), 'utf-8')
            sock.sendall(bytes(username, 'utf-8'))
            uname_recv = str(sock.recv(1024), 'utf-8')
            sock.sendall(bytes(password, 'utf-8'))
            pword_recv = str(sock.recv(1024), 'utf-8')
            sock.sendall(bytes(stud_id, 'utf-8'))
            id_recv = str(sock.recv(1024), 'utf-8')

        elif opt == '4':
            cmd = "LGOUT"
            sock.sendall(bytes(cmd, 'utf-8'))
            received = str(sock.recv(1024), 'utf-8')

        elif opt == '5':
            cmd = "EXIT"
            sock.sendall(bytes(cmd, 'utf-8'))
            received = str(sock.recv(1024), 'utf-8')
            break

        else:
            pass
finally:
    sock.close()


