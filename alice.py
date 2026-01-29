def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'guest.txt', 'rezero.txt']
for filename in filenames:
    count_words(filename)