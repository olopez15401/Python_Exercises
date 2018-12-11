class User():
    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def describe_user(self):
        print(self.first_name.title() + "\n" + self.last_name.title() + "\n" + str(self.user_id))

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

oscar = User("oscar","Lopez",1)
oscar.describe_user()
oscar.greet_user()

