import csv
import datetime

USERS_FILE = "data/users.csv"
GROUPS_FILE = "data/groups.csv"
LESSONS_FILE = "data/lessons.csv"
HOMEWORK_FILE = "data/homeworks.csv"

class Teacher:
    def __init__(self, user):
        self.user = user
        self.username = user[0]

    def menu(self):
        while True:
            print("\n--- Teacher Menu ---")
            print("1. My Groups")
            print("2. Show Group by ID")
            print("3. Start Lesson (by Group ID)")
            print("4. Homework CRUD (by Lesson ID)")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_my_groups()
            elif choice == '2':
                self.show_group_by_id()
            elif choice == '3':
                self.start_lesson()
            elif choice == '4':
                self.homework_crud()
            elif choice == '5':
                break

    def show_my_groups(self):
        group_id = self.user[3]
        print(f"\nAssigned Group ID: {group_id}")
        with open(GROUPS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == group_id:
                    print(f"Group ID: {row[0]}, Start Date: {row[1]}, Total Hours: {row[2]}")
                    return
        print("Group not found.")

    def show_group_by_id(self):
        gid = input("Enter group ID: ")
        with open(GROUPS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == gid:
                    print(f"Group ID: {row[0]}, Start Date: {row[1]}, Total Hours: {row[2]}")
                    return
        print("Group not found.")

    def start_lesson(self):
        group_id = input("Enter Group ID to start lesson: ")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lesson_id = f"L{int(datetime.datetime.now().timestamp())}"

        with open(LESSONS_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([lesson_id, group_id, self.username, date])

        print(f"Lesson started. ID: {lesson_id}, Time: {date}")

    def homework_crud(self):
        print("\n--- Homework CRUD ---")
        print("1. Create")
        print("2. Update")
        print("3. Delete")
        choice = input("Choice: ")

        if choice == '1':
            lesson_id = input("Lesson ID: ")
            task = input("Enter homework: ")
            with open(HOMEWORK_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([lesson_id, task])
            print("Homework created.")
        elif choice == '2':
            lesson_id = input("Lesson ID to update: ")
            updated = False
            homeworks = []
            with open(HOMEWORK_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == lesson_id:
                        new_task = input("New homework: ")
                        row[1] = new_task
                        updated = True
                    homeworks.append(row)
            with open(HOMEWORK_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(homeworks)
            print("Homework updated." if updated else "Not found.")
        elif choice == '3':
            lesson_id = input("Lesson ID to delete: ")
            homeworks = []
            deleted = False
            with open(HOMEWORK_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] != lesson_id:
                        homeworks.append(row)
                    else:
                        deleted = True
            with open(HOMEWORK_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(homeworks)
            print("Homework deleted." if deleted else "Not found.")
