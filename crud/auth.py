super_admin_username = "super_admin"
super_admin_password = "super_pass"


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == super_admin_username and password == super_admin_password:
        pass


def logout():
    print("hello")
