from User import User
from Admin import Admin
from Admin import Privilages

moderator = Admin('Oscar','Lopez',3609)
print(moderator.describe_user())
moderator.privilages.show_privilages()

