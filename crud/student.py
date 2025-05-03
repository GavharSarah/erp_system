import json
import os
from datetime import datetime

class Student:
    def __init__(self, student_id):
        self.student_id = str(student_id)
        self.data_file = 'data.json'
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

        if self.student_id not in self.data:
            self.data[self.student_id] = {
                "role": "student",
                "groups": [],
                "homeworks": [],
                "attendance": [],
                "balance": 0.0
            }
            self.save_data()

    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def show_groups(self):
        groups = self.data[self.student_id]["groups"]
        print(f"Your groups: {groups}")

    def upload_homework(self, homework_id):
        self.data[self.student_id]["homeworks"].append(homework_id)
        self.save_data()
        print(f"Homework '{homework_id}' uploaded.")

    def add_attendance(self, status):
        date = datetime.now().strftime("%Y-%m-%d")
        record = {"date": date, "status": status}
        self.data[self.student_id]["attendance"].append(record)
        self.save_data()
        print(f"Attendance for {date} marked as '{status}'.")

    def show_attendance(self):
        attendance = self.data[self.student_id]["attendance"]
        if not attendance:
            print("No attendance records yet.")
        else:
            print("Attendance history:")
            for record in attendance:
                print(f"{record['date']} - {record['status']}")

    def show_balance(self):
        balance = self.data[self.student_id]["balance"]
        print(f"Current balance: {balance} UZS")

    def make_payment(self, amount):
        self.data[self.student_id]["balance"] -= amount
        self.save_data()
        print(f"Payment of {amount} UZS made.")

    def logout(self):
        print(f"Student {self.student_id} has logged out.")
