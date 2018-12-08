magicians = ["Shawn","Jorge","Oscar","Neil","Marcos"]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magicians)

def make_great(magicians):
    great_magicians = []
    while magicians:
        great_magicians.append("The Great " + magicians.pop())
    return great_magicians


show_magicians(make_great(magicians))
