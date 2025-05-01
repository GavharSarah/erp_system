def auth_menu():
    while True:
        try:
            print("""
                1. Login
                2. Exit
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def super_admin_menu():
    while True:
        try:
            print("""
                1. Show all admins
                2. Create admin
                3. Delete admin
                4. Show statistics
                5. Show branches
                6. Create branch
                7. Delete branch
                8. Logout    
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                pass
            elif choice == "8":
                print("Good bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def admin_menu():
    while True:
        try:
            print("""
                1. Students CRUD (login, password)
                2. Groups CRUD (start date, total lesson hours)
                3. Student to group
                4. Search student -> full data, balance
                5. Add to balance (payment)
                6. Teacher CRUD
                7. Teacher to group
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                pass
            elif choice == "7":
                print("Good bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def teacher_menu():
    while True:
        try:
            print("""
                1. My groups
                2. Show group (by id)
                3. Start the lesson (group id) 
                4. Homework CRUD (lesson id)
                5. Logout
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print("Good bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


def student_men():
    while True:
        try:
            print("""
                1. Show groups
                2. Upload homework (id)
                3. Show my all attendance
                4. Show my balance
                5. Payment
                5. Logout
            """)
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                print("Good bye!")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue


if __name__ == "__main__":
    auth_menu()
