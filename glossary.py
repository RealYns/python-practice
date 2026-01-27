from collections import OrderedDict

glossary = {
    'For' : 'Used for looping, especially repeated tasks.' ,
    'If' : 'Used for conditions, if the condition is met, it does whatever is in the if statement.' ,
    'Lists' : 'Used to store things such as names, numbers etc.' ,
    'Print' : 'Prints whatever is inside of parentheses' ,
    'Dictionaries' : 'Used to store a limitless amount variables.' ,
}

for func in glossary.keys():
    print(func.title() + ": " + glossary[func])