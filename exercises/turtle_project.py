"""My scene will be of a beautful nightsky with birds, stars, and shooting stars.

There will also be trees at the bottom. Above and beyond: I used the circle() and pensize()
methods. I used many while loops throughout my code. I used randomness with the
randint() function from the random library to randomize RGB values for stars, 
coordinates for stars, and tree branch width and lengths and tree heights. I would say my scene
is more complex than that which is achieved with only four components (also used
more than four). pensize() method use: lines 198 and 202. circle() method use: lines 160, 239, 273, and 279. Randomness: lines 63, 64, 86, 87, 135, 136, 154, and 155. Loops: lines 32, 61, 84, 115, 133, 188, 212, 236, and 253.
"""

__author__ = "730695813"

# import necessary items
from turtle import Turtle, colormode, done, tracer, update
from random import randint
colormode(255)


# signature line for sky() function
def sky(Turtle: Turtle, x: float, y: float, x_size: int, y_size: int, red_val: int, green_val: int, blue_val: int) -> None:
    """This fucntion prints a portion of a bright night sky and takes certain RGB values as inputs."""
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
    
    # portion is filled
    Turtle.end_fill()


# signature line for tree() function
def tree(Turtle: Turtle, x: float, y: float, branch_num: int) -> None:  # starts at top of tree
    """This function will produce a tree at certain coordinates with an input value branches."""
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

    # create branches
    while (i < branch_num):
        # set probabilistic width and length values
        current_width_one: float = branch_base_width_value + ((randint(-10, 10) / 100) * 10)
        current_length_one: float = branch_base_length_value + randint(-4, 4)

        # creates branch
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

    # create branches
    while (i < branch_num):
        # set probabilistic width and length values
        current_width_one = branch_base_width_value + ((randint(-10, 10) / 100) * 10)
        current_length_one = branch_base_length_value + randint(-4, 4)

        # creates branch
        tree_branch(Turtle, x_while, y_while, current_width_one, current_length_one)

        # update variables
        if current_width_one < 0:
            current_width_one *= -1
        y_while -= current_width_one * .7
        branch_base_length_value += step
        i += 1
    
    # reset rotation angle
    Turtle.setheading(0)


# signature line for tree_branch() function
def tree_branch(Turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """This function will create a rectangle at an angle."""
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


# signature line for star_cover() function
def star_cover(Turtle: Turtle, x: float, y: float, x_size: int, y_size: int, num_stars: int) -> None:
    """This function covers the input area with an input number of stars."""
    # intial setup
    i: int = 0

    # loop to draw the stars
    while (i < num_stars):
        # don't want stars on boundaries
        x_coord: float = randint(3, x_size - 3) + x
        y_coord: float = randint(3, y_size - 3) + y

        # initial setup
        Turtle.up()
        Turtle.goto(x_coord, y_coord)
        Turtle.down()
        
        # call star() function and increment counter
        star(Turtle, x, y)
        i += 1


# signature line for star() function
def star(Turtle: Turtle, x: float, y: float) -> None:  # x and y are not used because the Turtle already goes to the necessary location before star() is called
    """This function creates a star at given coordinates."""
    # initial setup and semi-random star-color and star-size generator
    Turtle.down()
    Base_RGB: int = 60
    star_size: float = (randint(10, 13) / 100) * 10
    shift_value: int = randint(0, 160)
    Turtle.fillcolor(Base_RGB + shift_value, Base_RGB + shift_value, Base_RGB + shift_value)
    Turtle.begin_fill()
    
    # make a circle and fill
    Turtle.circle(star_size)
    Turtle.end_fill()


# signature line for bottom_scene() function
def bottom_scene(Turtle: Turtle, x: float, y: float, tree_num: int) -> None:
    """This function will produce the bottom of my scene: many tress and black bottom."""
    # initial setup
    Turtle.up
    Turtle.goto(x, y)
    Turtle.setheading(0)
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
    y_while: float = y

    # loop for each tree
    while (i < tree_num + 1):
        Turtle.down()
        tree(Turtle, x, y_while, branch_num)
        x += step
        Turtle.up()
        y_while = y - randint(-25, 50)
        Turtle.goto(x, y_while)
        i += 1

    # draw birds
    Turtle.pensize(2)
    bird(Turtle, 220, -20)
    bird(Turtle, 240, -50)
    bird(Turtle, 220, -70)
    Turtle.pensize(1)


# signature line for background() function
def background(Turtle: Turtle, x: float, y: float, channel_width: int, channel_num: int, color_factor: float, red_val: int, green_val: int, blue_val: int, star_num: int) -> None:
    """Creates the gradient background on color for night sky and the starcover."""
    # initial setup
    i: int = 0

    # loop for each segment of sky; increases green and blue values to make a gradient in sky
    while (i < channel_num):
        sky(Turtle, x + channel_width * i, y, channel_width, 725, red_val, int(green_val + i / color_factor), int(blue_val + i / color_factor))
        i += 1

    # calls star_cover() and shooting_star() functions
    star_cover(Turtle, x, y, 725, 725, star_num)
    shooting_star(Turtle, -230, 250, 10)
    shooting_star(Turtle, 8, 50, -90)


# signature line for shooting_star() function
def shooting_star(Turtle: Turtle, x: float, y: float, angle: int) -> None:
    """This function produces a shooting star at x and y input values."""
    # intial setup
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    i: int = 0
    step: float = 0.01
    current_radius: float = 2
    shift_value: int = 0
    base_value: int = 100

    # draw circles big to small and changes their RGB color value to create color gradient
    while (i < 100):
        Turtle.begin_fill()
        Turtle.color(base_value + shift_value, base_value + shift_value, base_value + shift_value)
        Turtle.circle(current_radius)
        Turtle.end_fill()
        shift_value += 1
        current_radius -= step
        i += 1
    
    # intial setup
    Turtle.goto(x - 1, y + 2)
    Turtle.left(angle)
    i = 0
    shift_value = 0
    base_value = 225

    # make shooting-star trail with gradient color
    while (i < 20):
        Turtle.color(base_value + shift_value, base_value + shift_value, base_value + shift_value)
        Turtle.backward(4)
        shift_value -= 10
        i += 1
    
    Turtle.up()


# signature line for bird() function
def bird(Turtle: Turtle, x: float, y: float) -> None:
    """This function produces a bird at a location specified in inputs."""
    # initial setup
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    Turtle.color(0, 0, 0)

    # drawing first half of bird
    Turtle.right(90)
    Turtle.circle(10, -150)

    # drawing second half of bird
    Turtle.up()
    Turtle.goto(x, y)
    Turtle.down()
    Turtle.circle(10, 150)

    # final settings
    Turtle.setheading(0)
    Turtle.up()


# signature line for main() function
def main() -> None:
    """The entry point of my scene."""
    # initial setup
    tracer(0, 0)  # Disable delay in tracing
    MAX_SPEED: int = 0
    leo: Turtle = Turtle()
    leo.speed(MAX_SPEED)
    leo.hideturtle()

    # creates scene
    background(leo, -358, -358, 10, 73, 1.75, 0, 5, 10, 5500)
    bottom_scene(leo, -358, -120, 24)

    # Now update the rendering
    update()
    done()


# idiom for running module
if __name__ == "__main__":
    main()