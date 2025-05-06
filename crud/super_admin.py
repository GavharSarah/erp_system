import csv

USERS_FILE = "data/users.csv"


class SuperAdmin:
    def __init__(self, user):
        self.user = user

    def menu(self):
        while True:
            print("\n--- Super Admin Menu ---")
            print("1. Show all admins")
            print("2. Create admin")
            print("3. Delete admin")
            print("4. Show statistics")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_all_admins()
            elif choice == '2':
                self.create_admin()
            elif choice == '3':
                self.delete_admin()
            elif choice == '4':
                self.show_statistics()
            elif choice == '5':
                break

    def show_all_admins(self):
        print("\n--- All Admins ---")
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == 'admin':
                    print(f"Username: {row[0]}, Password: {row[1]}")

    def create_admin(self):
        username = input("New admin username: ")
        password = input("New admin password: ")
        with open(USERS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, 'admin', '', ''])
        print("Admin created successfully.")

    def delete_admin(self):
        username = input("Enter admin username to delete: ")
        updated_users = []
        deleted = False

        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[2] == 'admin':
                    deleted = True
                    continue
                updated_users.append(row)

        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_users)

        print("Admin deleted." if deleted else "Admin not found.")

    def show_statistics(self):
        stats = {"superadmin": 0, "admin": 0, "teacher": 0, "student": 0}
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                role = row[2]
                if role in stats:
                    stats[role] += 1
        print("\n--- User Statistics ---")
        for role, count in stats.items():
            print(f"{role.capitalize()}s: {count}")
