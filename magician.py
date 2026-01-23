def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians, great_magicians):
    while magicians:
        great_magician = magicians.pop()
        great_magicians.append("The Great " + great_magician)



magicians = ['John smith', 'Hisoka Morrow', 'Shaco']
great_magicians = []
make_great(magicians[:], great_magicians)
show_magicians(great_magicians)

print(magicians)