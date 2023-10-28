"""Turtle_tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

side_length: int = 300

i = 0

leo.up()
leo.goto(-150, -130)
leo.pencolor(255, 0, 0)
leo.fillcolor(99, 204, 250)
# leo.color() function for setting pen and fill color

leo.speed(50)
leo.hideturtle()

leo.begin_fill()

while i < 3:
    leo.forward(side_length)
    leo.left(120)
    i += 1 

leo.end_fill()

i = 0

bob: Turtle = Turtle()

bob.speed(200)

bob.up()
bob.goto(-150, -130)
bob.pencolor(0, 0, 0)
bob.down()
bob.hideturtle()

while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i += 1 
bob.penup()

bob: Turtle = Turtle()

bob.speed(200)

bob.up()
bob.goto(-150, -130)
bob.pencolor(0, 0, 0)
bob.down()
bob.hideturtle()

while i < 65:
    bob.forward(side_length)
    bob.left(121)
    i += 1 
    side_length *= .97
bob.penup()

done()