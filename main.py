import csv
from crud.super_admin  import SuperAdmin
from crud.admin import Admin
from crud.teacher import Teacher
from crud.student import Student

USERS_FILE = "data/users.csv"

def load_users():
    with open(USERS_FILE, "r") as file:
        reader = csv.reader(file)
        return list(reader)

def login():
    username = input("Username: ")
    password = input("Password: ")

    users = load_users()
    for user in users:
        if user[0] == username and user[1] == password:
            print(f"Login successful! Welcome, {user[2].capitalize()} {user[0]}")
            return user
    print("Invalid login.")
    return None

def main():
    while True:
        print("\n ERP System ")
        print("1. Login")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            user = login()
            if user:
                role = user[2]
                if role == "superadmin":
                    SuperAdmin(user).menu()
                elif role == "admin":
                    Admin(user).menu()
                elif role == "teacher":
                    Teacher(user).menu()
                elif role == "student":
                    Student(user).menu()
        elif choice == '2':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
