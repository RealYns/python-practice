from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)

die_0 = Die(20)
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()
die_0.roll_die()