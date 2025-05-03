class SuperAdminMenu:
    def __init__(self):
        self.admins = []

    def show_all_admins(self):
        if self.admins:
            print("Admins List:")
            for admin in self.admins:
                print(admin)
        else:
            print("No admins found.")

    def create_admin(self, admin_name):
        if admin_name not in self.admins:
            self.admins.append(admin_name)
            print(f"Admin '{admin_name}' created.")
        else:
            print(f"Admin '{admin_name}' already exists.")

    def delete_admin(self, admin_name):
        if admin_name in self.admins:
            self.admins.remove(admin_name)
            print(f"Admin '{admin_name}' deleted.")
        else:
            print(f"Admin '{admin_name}' not found.")

    def show_statistics(self):
        print(f"Total admins: {len(self.admins)}")

    def logout(self):
        print("You have logged out.")
