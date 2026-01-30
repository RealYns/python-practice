with open('random_paragraphs.txt') as file_object:
    contents = file_object.read().lower()
    words = contents.split()
    word_count = words.count('the')
    print(word_count)