# Bob Tate
# 1/27/21
#
# Solution to Problem 5
# This program uses Python's turtle library to draw a rubik's cube.

def draw_diamond(size):
    rubik.forward(size)
    rubik.left(120)
    rubik.forward(size)
    rubik.left(60)
    rubik.forward(size)
    rubik.left(120)
    rubik.forward(size)

def draw_filled_diamond(color, size):
    rubik.fillcolor(color)
    rubik.begin_fill()
    draw_diamond(size)
    rubik.end_fill()

def hash_square():
    rubik.right(60)
    rubik.forward(SIDE_LENGTH / 3)
    rubik.left(120)
    rubik.forward(SIDE_LENGTH)
    rubik.right(120)
    rubik.forward(SIDE_LENGTH / 3)
    rubik.right(60)
    rubik.forward(SIDE_LENGTH)
    rubik.left(60)
    rubik.forward(SIDE_LENGTH / 3)
    rubik.left(120)
    rubik.forward(SIDE_LENGTH / 3)
    rubik.left(60)
    rubik.forward(SIDE_LENGTH)
    rubik.right(60)
    rubik.forward(SIDE_LENGTH / 3)
    rubik.right(120)
    rubik.forward(SIDE_LENGTH)
    rubik.right(60)
    rubik.forward(2 * SIDE_LENGTH / 3)
    rubik.right(120)
    rubik.forward(SIDE_LENGTH)

import turtle  

SIDE_LENGTH = 200

# Set up turtle (rubik)
window = turtle.Screen()        
rubik = turtle.Turtle() 
rubik.shape("circle")
rubik.width(SIDE_LENGTH / 25)

# draw
rubik.right(90)
draw_filled_diamond("blue", SIDE_LENGTH)

rubik.right(60)
draw_filled_diamond("yellow", SIDE_LENGTH)

rubik.right(60)
draw_filled_diamond("red", SIDE_LENGTH)

rubik.color("black")

for i in range(3):
    hash_square()

rubik.up()
rubik.right(150)
rubik.forward(500)

# keeps the turtle window open until user closes it
turtle.mainloop()