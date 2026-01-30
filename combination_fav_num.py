import json

filename = 'numbers.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
        print(number)
except FileNotFoundError:
    number = int(input("What's your favourite number?\n"))
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)