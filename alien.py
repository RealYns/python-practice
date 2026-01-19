alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])

print(alien_0['points'])

print("You have " + str(alien_0['points']) + " points.")

alien_0['pos_x'] = 100
alien_0['pos_y'] = -200

print(alien_0)

alien_0['color'] = 'red'

print(alien_0['color'])

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['pos_x'] = alien_0['pos_x'] + x_increment

print("The x coordinate is updated! x = " + str(alien_0['pos_x']))

del alien_0['points']

print(alien_0)

alien_1 = {
    'color' : 'green' ,
    'points' : 10 ,
}

alien_2 = {
    'color' : 'yellow' ,
    'points' : 15 ,
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)