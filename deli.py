sandwich_orders = ['tacos', 'pastrami', 'khanez ou bnin', 'grilled cheese', 'pastrami']
finished_sandwiches = []
print()

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami':
        finished_sandwiches.append(sandwich)
    else:
        print("We run out of pastrami.")

for sndwch in finished_sandwiches:
    print(sndwch.title() + " is done")

print(finished_sandwiches)
