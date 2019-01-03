from User import User
class Admin(User):

    def __init__(self,first_name,last_name,user_id):
        super().__init__(first_name,last_name,user_id)
        privs = ['add users','ban users','add posts', 'delete posts']
        self.privilages=Privilages(privs)

"""
    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage.title())
"""

class Privilages():
    def __init__(self,privilages):
        self.privilages = privilages

    def show_privilages(self):
        for priv in self.privilages:
            print(priv)

"""
me = Admin('Oscar','Lopez',2046)
me.describe_user()
me.privilages.show_privilages()
"""