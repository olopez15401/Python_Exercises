"""A simple guest book program """

with open('guestbook.txt', 'a') as guestbook:

    while True:
        guest_name = input(
            'What is your name [Leave empty and press enter to stop]: ')
        if guest_name:
            guestbook.write(guest_name.title() + "\n")
            print("Welcome " + guest_name.title() + ".")
        else:
            break

    guestbook.close()

print("Guests in guestbook: ")

with open('guestbook.txt') as guestbook:
    for line in guestbook:
        print(line.strip())
        
guestbook.close()