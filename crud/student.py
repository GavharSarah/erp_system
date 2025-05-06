import csv
import os
from datetime import datetime

DATA_FOLDER = "data"
HOMEWORKS_FILE = os.path.join(DATA_FOLDER, "homeworks.csv")
ATTENDANCE_FILE = os.path.join(DATA_FOLDER, "attendance.csv")
USERS_FILE = os.path.join(DATA_FOLDER, "users.csv")


class Student:
    def __init__(self, user):
        self.user = user  # ['username', 'password', 'student', 'group_id', 'balance']

    def menu(self):
        while True:
            print("\n--- Student Menu ---")
            print("1. Show My Group")
            print("2. Upload Homework")
            print("3. Show My Attendance")
            print("4. Show My Balance")
            print("5. Make Payment")
            print("6. Logout")

            choice = input("Enter choice: ")

            if choice == '1':
                self.show_my_group()
            elif choice == '2':
                self.upload_homework()
            elif choice == '3':
                self.show_attendance()
            elif choice == '4':
                self.show_balance()
            elif choice == '5':
                self.make_payment()
            elif choice == '6':
                break

    def show_my_group(self):
        print(f"You are in group: {self.user[3]}")

    def upload_homework(self):
        lesson_id = input("Enter lesson ID: ")
        answer = input("Enter your homework answer: ")
        filename = f"{self.user[0]}_homework_{lesson_id}.txt"
        with open(os.path.join(DATA_FOLDER, filename), 'w') as file:
            file.write(answer)
        print(f"Homework uploaded to {filename}")

    def show_attendance(self):
        group_id = self.user[3]
        if not os.path.exists(ATTENDANCE_FILE):
            print("No attendance records yet.")
            return

        with open(ATTENDANCE_FILE, 'r') as file:
            reader = csv.reader(file)
            records = [row for row in reader if row[0] == group_id]

        if not records:
            print("No attendance found for your group.")
        else:
            print("Your group’s attendance:")
            for row in records:
                print(f"- {row[1]}")

    def show_balance(self):
        print(f"Your current balance: {self.user[4]}")

    def make_payment(self):
        amount = float(input("Enter payment amount: "))
        self.user[4] = str(float(self.user[4]) + amount)
        self._update_user_balance()
        print(f"Payment successful. New balance: {self.user[4]}")

    def _update_user_balance(self):
        users = []
        with open(USERS_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.user[0] and row[2] == 'student':
                    row[4] = self.user[4]
                users.append(row)

        with open(USERS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)