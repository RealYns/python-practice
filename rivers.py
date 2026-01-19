rivers = {
    'nile' : 'egypt' ,
    'amazon' : 'colombia' ,
    'yangtze' : 'yangtze' ,
}

for river in rivers.keys():
    print("The " + river.title() + " wruns through " + rivers[river].title() + ".")