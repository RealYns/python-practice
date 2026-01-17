requested_toppings = ["mushrooms", "olives", "peppers"]
available_toppings = ["extra cheese", "peppers", "mushrooms", "pineapples", "peperoni"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we are out of " + requested_topping + ".")
print("\nThe pizza is done.")
