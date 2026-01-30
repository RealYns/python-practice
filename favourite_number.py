import json

number = input("What's your favourite number?\n")
filename = 'numbers.json'
with open(filename, 'w') as file_object:
    json.dump(number, file_object)