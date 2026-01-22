from shutil import which


def describe_pet(name, which_animal):

    print("I have a " + which_animal.title() + "!")
    print("And his name is " + name.title() + "!\n")


describe_pet()