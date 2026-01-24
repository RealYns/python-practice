
class User():

    def __init__(self, first_name, last_name, email=None, age=None, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country

    def describe_user(self):
        print("\nFirst name:" + self.first_name.title())
        print("Last name:" + self.last_name.title())

        if self.email is not None:
            print("Email: " + self.email.title())
        else:
            print("Email: Not provided")

        if self.age is not None:
            print("Age: " + str(self.age))
        else:
            print("Age: Not provided")

        if self.country is not None:
            print("Country: " + self.country.title())
        else:
            print("Country: Not provided")


    def greet_user(self):
        print("\nGreetings, " + self.first_name.title() + "!")

user_0 = User('john', 'smith')
user_0.describe_user()
user_0.greet_user()

user_1 = User('alucard', 'hellsing', 'alucardhellsing@gmail.com')
user_1.describe_user()
user_1.greet_user()

user_2 = User('seras', 'victoria', age=20)
user_2.describe_user()
user_2.greet_user()