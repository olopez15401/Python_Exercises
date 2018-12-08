def get_formatted_name(first_name,last_name, middle_name = ''):
    """ Return a full name, neatly formatted """
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

def greet():
    while True:
        print("Hello, please tell me your name:")
        print("Enter 'q' at anytime when done.")

        f_name = input("First name: ")
        if not f_name or f_name == 'q':
            print("So sorry you have to leave. Goodbye.")
            break
        
        l_name = input("Last name: ")
        if not l_name or l_name == 'q':
            print("So sorry you have to leave, " + f_name + ". Goodbye.")
            break
        formatted_name = get_formatted_name(f_name,l_name)
        print("\nHello, " + formatted_name + "!")

greet()