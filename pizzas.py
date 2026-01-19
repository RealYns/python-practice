pizza = {
    'crust' : 'thick' ,
    'toppings' : ['mushrooms', 'peppers', 'olive'] ,
}

print("I ordered a " + pizza['crust'] + "-crust pizza with the following toppings:" )

for toppings in pizza['toppings']:
    print("\t" + toppings.title())