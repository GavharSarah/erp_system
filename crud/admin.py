import csv
import os

USERS_FILE = "data/users.csv"
GROUPS_FILE = "data/groups.csv"

class Admin:
    def __init__(self, user):
        self.user = user

    def menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Students CRUD")
            print("2. Groups CRUD")
            print("3. Add Student to Group")
            print("4. Search Student (Full Data & Balance)")
            print("5. Add to Student Balance")
            print("6. Teachers CRUD")
            print("7. Add Teacher to Group")
            print("8. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.student_crud()
            elif choice == '2':
                self.group_crud()
            elif choice == '3':
                self.add_student_to_group()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                self.add_to_balance()
            elif choice == '6':
                self.teacher_crud()
            elif choice == '7':
                self.add_teacher_to_group()
            elif choice == '8':
                break



    def student_crud(self):
        print("\n--- Student CRUD ---")
        print("1. Create")
        print("2. Update Password")
        print("3. Delete")
        choice = input("Choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            with open(USERS_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password, 'student', '', '0'])
            print("Student created.")
        elif choice == '2':
            username = input("Enter student username: ")
            new_pass = input("New password: ")
            self.update_field(username, 'student', 1, new_pass)
        elif choice == '3':
            self.delete_user('student')

    def add_student_to_group(self):
        username = input("Enter student username: ")
        group_id = input("Enter group ID: ")
        self.update_field(username, 'student', 3, group_id)

    def search_student(self):
        username = input("Enter student username to search: ")
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[2] == 'student':
                    print(f"Data: Username={row[0]}, Password={row[1]}, Group={row[3]}, Balance={row[4]}")
                    return
        print("Student not found.")

    def add_to_balance(self):
        username = input("Enter student username: ")
        amount = float(input("Enter amount to add: "))
        users = []
        found = False
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[2] == 'student':
                    row[4] = str(float(row[4]) + amount)
                    found = True
                users.append(row)
        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        print("Balance updated." if found else "Student not found.")



    def teacher_crud(self):
        print("\n--- Teacher CRUD ---")
        print("1. Create")
        print("2. Update Password")
        print("3. Delete")
        choice = input("Choice: ")

        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            with open(USERS_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password, 'teacher', '', ''])
            print("Teacher created.")
        elif choice == '2':
            username = input("Enter teacher username: ")
            new_pass = input("New password: ")
            self.update_field(username, 'teacher', 1, new_pass)
        elif choice == '3':
            self.delete_user('teacher')

    def add_teacher_to_group(self):
        username = input("Enter teacher username: ")
        group_id = input("Enter group ID: ")
        self.update_field(username, 'teacher', 3, group_id)



    def group_crud(self):
        print("\n--- Group CRUD ---")
        print("1. Create")
        print("2. Update")
        print("3. Delete")
        choice = input("Choice: ")

        if choice == '1':
            group_id = input("Group ID: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            hours = input("Total lesson hours: ")
            with open(GROUPS_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([group_id, start_date, hours])
            print("Group created.")
        elif choice == '2':
            group_id = input("Group ID to update: ")
            new_start = input("New start date: ")
            new_hours = input("New total hours: ")
            groups = []
            with open(GROUPS_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == group_id:
                        row[1], row[2] = new_start, new_hours
                    groups.append(row)
            with open(GROUPS_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(groups)
            print("Group updated.")
        elif choice == '3':
            group_id = input("Group ID to delete: ")
            groups = []
            with open(GROUPS_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] != group_id:
                        groups.append(row)
            with open(GROUPS_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(groups)
            print("Group deleted.")



    def update_field(self, username, role, field_index, new_value):
        updated = False
        users = []
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[2] == role:
                    row[field_index] = new_value
                    updated = True
                users.append(row)
        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        print("Update successful." if updated else f"{role.capitalize()} not found.")

    def delete_user(self, role):
        username = input(f"Enter {role} username to delete: ")
        users = []
        deleted = False
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if not (row[0] == username and row[2] == role):
                    users.append(row)
                else:
                    deleted = True
        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        print(f"{role.capitalize()} deleted." if deleted else f"{role.capitalize()} not found.")
