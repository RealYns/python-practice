from users import User

class Privileges():
    def __init__(self, privileges = ['Can ban users', 'Can add posts', 'Can delete posts']):
        self.privileges = privileges

    def show_privileges(self):
        print("This is the list of privileges that this admin has: ")
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):

    def __init__(self, first_name, last_name, email=None, age=None, country=None):
        super().__init__(first_name, last_name, email, age, country)
        self.privileges = Privileges()



admin_0 = Admin('humongus', 'guy', 'humongusamongusguy@gmail.com')
admin_0.describe_user()
admin_0.privileges.show_privileges()