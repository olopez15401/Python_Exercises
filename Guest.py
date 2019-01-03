guest_name = input('Your name please?:')
with open('guest.txt','w') as guest_file:
    guest_file.write(guest_name.title())
    print('Welcome ' + guest_name.title())
