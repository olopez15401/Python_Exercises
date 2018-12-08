def make_album(artist_name, album_title):
    album = {
        "Artist": artist_name,
        "Album Title": album_title
    }
    return album


#print(make_album("Oscar", "Jiggle Wut"))

def make_albums():
    done = False
    while not done:
        artist = input("Enter the name of the artist:")
        #album_name = input("Enter the album name:")
        if artist == 'quit':
            done = True
        else:
            album_name = input("Enter the album name:")
            print(make_album(artist,album_name))

make_albums()
