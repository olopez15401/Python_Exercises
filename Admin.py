from User import User
class Admin(User):

    def __init__(self,first_name,last_name,user_id):
        super().__init__(first_name,last_name,user_id)
        self.privilages=['can add posts','can delete posts','can ban users']

    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage.title())

me = Admin('Oscar','Lopez',3609)
me.describe_user()
me.show_privilages()