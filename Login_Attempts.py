class Login_Attempts():

    def __init__(self, first_name, last_name, user_id):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + "\n" + self.last_name.title() + "\n" + str(self.user_id))

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

new_user = Login_Attempts('Jon','Doe',12345)
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempts()
print(new_user.login_attempts)