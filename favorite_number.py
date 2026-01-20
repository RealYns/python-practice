favorite_numbers = {
    'john' : [66, 45] ,
    'alex' : [47, 52] ,
    'jonas' : [9, 6, 69, 96] ,
    'a random new gen kid' : [67, 69] ,
    'velkoz' : [3.14] ,
}

for name, nums in favorite_numbers.items():
    print("\n" + name.title() + "'s numbers are:")
    for num in nums:
        print(num)