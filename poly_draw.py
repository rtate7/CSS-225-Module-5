# Bob Tate
# 1/27/21
#
# Solution to Problem 3
# This program uses the turtle library to draw a polygon on the
# screen based on the user's specifications for number of sides
# and side lenght.

import turtle  

DEGREES_FULL_CIRCLE = 360

# Get User input
num_sides = int(input("How many sides should I draw? "))
side_length = int(input("How long should each side be? "))

angle = DEGREES_FULL_CIRCLE / num_sides

# Set up turtle (euclid)
window = turtle.Screen()        
euclid = turtle.Turtle() 

# draw
for side in range(num_sides):
    euclid.forward(side_length)
    euclid.left(angle)

# keeps the turtle window open until user closes it
turtle.mainloop()


