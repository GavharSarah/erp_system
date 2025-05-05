from math import trunc


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == username and password == password:
            print("Login Successful")
            print('logged in successfully with username {username} and password {password}')
            print(" choose 1. Teacher "
                  "2.Student"
                  "3.")
            try:
                while True:


        else:
            print("Login Failed")




