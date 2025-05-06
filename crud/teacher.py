import csv
import os
from datetime import datetime

DATA_FOLDER = "data"
HOMEWORK_FILE = os.path.join(DATA_FOLDER, "homeworks.csv")
ATTENDANCE_FILE = os.path.join(DATA_FOLDER, "attendance.csv")

class Teacher:
    def __init__(self, user):
        self.user = user  # ['username', 'password', 'teacher', 'group_id', '']

    def menu(self):
        while True:
            print("\n--- Teacher Menu ---")
            print("1. My Groups")
            print("2. Show Group by ID")
            print("3. Start Lesson (group ID)")
            print("4. Homework: Create")
            print("5. Homework: Update")
            print("6. Homework: Delete")
            print("7. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_my_groups()
            elif choice == '2':
                self.show_group_by_id()
            elif choice == '3':
                self.start_lesson()
            elif choice == '4':
                self.create_homework()
            elif choice == '5':
                self.update_homework()
            elif choice == '6':
                self.delete_homework()
            elif choice == '7':
                break

    def show_my_groups(self):
        print(f"Your assigned group: {self.user[3]}")

    def show_group_by_id(self):
        group_id = input("Enter group ID: ")
        if group_id == self.user[3]:
            print(f"Group ID: {group_id}")
        else:
            print("You are not assigned to this group.")

    def start_lesson(self):
        group_id = input("Enter group ID to start lesson: ")
        if group_id == self.user[3]:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(ATTENDANCE_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([group_id, date])
            print("Lesson started and attendance recorded.")
        else:
            print("You can't start lessons for groups you're not assigned to.")

    def create_homework(self):
        group_id = input("Group ID: ")
        if group_id != self.user[3]:
            print("You can't assign homework to this group.")
            return
        lesson_id = input("Lesson ID: ")
        description = input("Homework description: ")
        with open(HOMEWORK_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([lesson_id, group_id, description])
        print("Homework created.")

    def update_homework(self):
        lesson_id = input("Enter lesson ID to update: ")
        new_desc = input("New homework description: ")

        updated = False
        homeworks = []

        if os.path.exists(HOMEWORK_FILE):
            with open(HOMEWORK_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == lesson_id and row[1] == self.user[3]:
                        row[2] = new_desc
                        updated = True
                    homeworks.append(row)

        with open(HOMEWORK_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(homeworks)

        print("Homework updated." if updated else "Homework not found.")

    def delete_homework(self):
        lesson_id = input("Enter lesson ID to delete: ")

        deleted = False
        homeworks = []

        if os.path.exists(HOMEWORK_FILE):
            with open(HOMEWORK_FILE, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not (row[0] == lesson_id and row[1] == self.user[3]):
                        homeworks.append(row)
                    else:
                        deleted = True

        with open(HOMEWORK_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(homeworks)

        print("Homework deleted." if deleted else "Homework not found.")
