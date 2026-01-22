def build_person(first_name, last_name, age=''):
    person = {
        'first' : first_name ,
        'last' : last_name ,
    }
    if age:
        person['age'] = age
    return person

culprit = build_person('John', 'Smith', age=27)
print(culprit)