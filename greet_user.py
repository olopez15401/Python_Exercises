import json

def get_stored_username():
    filename = "username.json"

    with open(filename) as f_obj:
        username = json.load(f_obj)
        print("Welcome back, " + username + "!")

get_stored_username()