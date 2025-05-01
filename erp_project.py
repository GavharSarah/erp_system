class ERPSystem:
    def __init__(self):
        self.super_admins = []
        self.admins = []
        self.teachers = []
        self.students = []
        self.branches = []
        self.groups = []

    def auth_menu(self):
        while True:
            print("\nAuth Menu:")
            print("1. Login")
            print("2. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def login(self):
        role = input("Enter your role (super_admin/admin/teacher/student): ").strip().lower()
        if role == "super_admin":
            self.super_admin_menu()
        elif role == "admin":
            self.admin_menu()
        elif role == "teacher":
            self.teacher_menu()
        elif role == "student":
            self.student_menu()
        else:
            print("Invalid role. Try again.")

    def super_admin_menu(self):
        while True:
            print("\nSuper Admin Menu:")
            print("1. Show all admins")
            print("2. Create admin")
            print("3. Delete admin")
            print("4. Show statistics")
            print("5. Show branches")
            print("6. Create branch")
            print("7. Delete branch")
            print("8. Logout")
            choice = input("Choose an option: ")

            if choice == "8":
                print("Logging out...")
                break
            else:   
                print("Feature not implemented yet.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Students CRUD")
            print("2. Groups CRUD")
            print("3. Student to group")
            print("4. Search student")
            print("5. Add to balance")
            print("6. Teacher CRUD")
            print("7. Teacher to group")
            print("8. Logout")
            choice = input("Choose an option: ")

            if choice == "8":
                print("Logging out...")
                break
            else:
                print("Feature not implemented yet.")

    def teacher_menu(self):
        while True:
            print("\nTeacher Menu:")
            print("1. My groups")
            print("2. Show group")
            print("3. Start the lesson")
            print("4. Homework CRUD")
            print("5. Logout")
            choice = input("Choose an option: ")

            if choice == "5":
                print("Logging out...")
                break
            else:
                print("Feature not implemented yet.")

    def student_menu(self):
        while True:
            print("\nStudent Menu:")
            print("1. Show groups")
            print("2. Upload homework")
            print("3. Show my all attendance")
            print("4. Show my balance")
            print("5. Payment")
            print("6. Logout")
            choice = input("Choose an option: ")

            if choice == "6":
                print("Logging out...")
                break
            else:
                print("Feature not implemented yet.")


if __name__ == "__main__":
    erp_system = ERPSystem()
    erp_system.auth_menu()