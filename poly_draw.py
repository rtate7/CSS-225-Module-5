# Bob Tate
# 1/27/21
#
# Solution to Problem 2
# This program iterates through a list of numbers twice.
# The first time through it prints all of the numbers.
# The second time through it prints each number and its square.

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


