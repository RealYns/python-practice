
def get_formatted(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()

culprit = get_formatted('John', 'Smith', 'Lee')
print("The culprit is " + culprit)