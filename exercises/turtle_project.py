"""My scene will be of a beautful nightsky and pretty landscape."""

from turtle import Turtle, colormode, done, tracer, update
from random import randint
colormode(255)


def sky(Turtle: Turtle, x: float, y: float, x_size: int, y_size: int, red_val: int, green_val: int, blue_val: int) -> None:
    """This fucntion prints a portion of a bright night sky."""
     # initial setup
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    i: int = 0
    Turtle.fillcolor(red_val, green_val, blue_val)
    Turtle.pencolor(red_val, green_val, blue_val)
    Turtle.begin_fill()

    # outlining
    while (i < 2):
        Turtle.forward(x_size)
        Turtle.left(90)
        Turtle.forward(y_size)
        Turtle.left(90)
        i += 1
    
    Turtle.end_fill()

    
def tree(Turtle: Turtle, x: float, y: float, branch_num: int) -> None: # starts at top of tree
    """This function will produce a tree at certain coordinates."""
    # initial setup
    Turtle.up
    Turtle.goto(x, y)
    i: int = 0
    Turtle.color(0, 0, 0)
    branch_base_width_value: float = 1.5
    branch_base_length_value: float = 1
    x_while: float = x
    y_while: float = y
    step: float = 30 / branch_num

    # right side of tree
    Turtle.left(-10)

    while (i < branch_num):
        # draw tree branches
        current_width_one: int = branch_base_width_value + ((randint(-10, 10) / 100) * 10)
        current_length_one: int = branch_base_length_value + randint(-4, 4)

        # creates branches
        tree_branch(Turtle, x_while, y_while, current_width_one, current_length_one)

        # update variables
        if current_width_one < 0:
            current_width_one *= -1
        y_while -= current_width_one * .7
        branch_base_length_value += step
        i += 1

    # left side of tree
    x_while = x
    y_while = y + 2
    i = 0
    Turtle.right(160)
    branch_base_length_value = 1

    while (i < branch_num):
        # draw tree branches
        current_width_one: int = branch_base_width_value + ((randint(-10, 10) / 100) * 10)
        current_length_one: int = branch_base_length_value + randint(-4, 4)

        # creates branches
        tree_branch(Turtle, x_while, y_while, current_width_one, current_length_one)

        # update variables
        if current_width_one < 0:
            current_width_one *= -1
        y_while -= current_width_one * .7
        branch_base_length_value += step
        i += 1
    
    # reset rotation angle
    Turtle.setheading(0)



def tree_branch(Turtle: Turtle, x: float, y: float, width: int, length: int) -> None:
    """This function will create a rectangle at an angle"""
    # initial setup
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    i: int = 0
    Turtle.fillcolor(0, 0, 0)
    Turtle.begin_fill()

    # outlining
    while (i < 2):
        # code for one side
        Turtle.forward(length)
        Turtle.left(90)
        Turtle.forward(width)
        Turtle.left(90)
        i += 1
    
    Turtle.end_fill()


def star_cover(Turtle: Turtle, x: float, y: float, x_size: int, y_size: int,  num_stars: int) -> None:
    i = 0
    while (i < num_stars):
        # don't want stars on boundaries
        x_coord: int = randint(3, x_size - 3) + x
        y_coord: int = randint(3, y_size - 3) + y

        # initial setup
        Turtle.up()
        Turtle.goto(x_coord, y_coord)
        Turtle.down()
        
        # call star() function and increment counter
        star(Turtle, x, y)
        i += 1


def star(Turtle: Turtle, x: float, y: float) -> None:
    
    # initial setup and semi-random star-color and star-size generator
    Turtle.down()
    Base_RGB = 60
    star_size: float = (randint(10, 13) / 100) * 10
    shift_value = randint(0, 160)
    Turtle.fillcolor(Base_RGB + shift_value, Base_RGB + shift_value, Base_RGB + shift_value)
    Turtle.begin_fill()
    
    # make a circle and fill
    Turtle.circle(star_size)
    Turtle.end_fill()


def bottom_scene(Turtle: Turtle, x: float, y: float, tree_num: int) -> None:
    """This function will produce the bottom of my scene: many tress and black bottom."""
    # initial setup
    Turtle.up
    Turtle.goto(x, y)
    Turtle.setheading(0)
    i: int = 0
    Turtle.color(0, 0, 0)
    Turtle.begin_fill()
    branch_num: int = 150
    i: int = 0
    step: float = 716 / tree_num

    # use tree_branch() function to create a black rectangle
    tree_branch(Turtle, -358, -358, 120, 725)
    Turtle.end_fill()

    # initial setup
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    y_while = y

    while (i < tree_num + 1):
        Turtle.down()
        tree(Turtle, x, y_while, branch_num)
        x += step
        Turtle.up()
        y_while = y - randint(-25, 50)
        Turtle.goto(x, y_while)
        i += 1


def background(Turtle: Turtle, x: float, y: float, channel_width: int, channel_num: int, color_factor: float, red_val: int, green_val: int, blue_val: int, star_num: int) -> None:
    """Creates the gradient background on color for night sky and the starcover."""
    i: int = 0
    while (i < channel_num):
        sky(Turtle, x + channel_width*i, y, channel_width, 725, red_val, int(green_val + i / color_factor), int(blue_val + i / color_factor))
        i += 1
    star_cover(Turtle, x, y, 725, 725, star_num)
    shooting_star(Turtle, -230, 250, 10)
    shooting_star(Turtle, 8, 50, -90)


def shooting_star(Turtle: Turtle, x: float, y: float, angle: int) -> None:
    """This function produces a shooting star at x and y input values."""
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    i: int  = 0
    step: float = 0.01
    current_radius: float = 2
    shift_value: int = 0
    base_value: int = 100

    # draw circles big to small
    while (i < 100):
        Turtle.begin_fill()
        Turtle.color(base_value + shift_value, base_value + shift_value, base_value + shift_value)
        Turtle.circle(current_radius)
        Turtle.end_fill()
        shift_value += 1
        current_radius -= step
        i += 1
    
    Turtle.goto(x - 1, y + 2)
    Turtle.left(angle)
    i = 0
    shift_value = 0
    base_value = 225

    while (i < 20):
        Turtle.color(base_value + shift_value, base_value + shift_value, base_value + shift_value)
        Turtle.backward(4)
        shift_value -= 10
        i += 1
    
    Turtle.up()


def bird(Turtle: Turtle, x: float, y: float) -> None:
    """This function produces a bird at a location specified in inputs."""


def main() -> None:
    """The main function to fun my code."""

    # initial setup
    tracer(0, 0) # Disable delay in tracing
    MAX_SPEED = 0
    leo: Turtle = Turtle()
    leo.speed(MAX_SPEED)
    leo.hideturtle()

    # creates scene
    background(leo, -358, -358, 10, 73, 1.75, 0, 5, 10, 10000)
    bottom_scene(leo, -358, -120, 24)

    # Now update the rendering
    update()
    done()


if __name__ == "__main__":
    main()