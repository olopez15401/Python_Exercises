def greet_users(names):
    """ Print a simple greeting to each user in the list """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['oscar', 'shawn', 'Marcos', 'Nery', 'Ian', 'Jorge']
greet_users(usernames)