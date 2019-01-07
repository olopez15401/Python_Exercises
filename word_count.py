def count_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()

            words = contents.split()
            num_words = len(words)
            print("The file " + filename + " has " + str(num_words) + " words")
   
    except FileNotFoundError:
        print("ERROR: File " + filename + " is not found!")

filename = "goofy.txt"
count_words(filename)