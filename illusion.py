
import turtle
from appJar import gui
from _tkinter import TclError


def draw(grid_colour, square_colour, intersection_colour, square_side, pensize, image_side):
    """
    Function for drawing the grid with the wanted specifications using the turtle module
    :param grid_colour: The colour of the lines in the grid
    :param square_colour: The fill colour of the squares
    :param intersection_colour: The colour of the dots in the intersections
    :param square_side: The length of the side of each square
    :param pensize: The width of the draw pen, also applies to the dots
    :param image_side: The size of the side of the image
    :return: None
    """
    # This way we can declare a negative lower bound, to adjust for the origin in the centre
    try:
        image_side /= 2
        trt.reset()
        trt.getscreen().resetscreen()
        turtle.screensize(canvwidth=image_side, canvheight=image_side, bg=None)
        trt.hideturtle()
        trt.color(square_colour)
        trt.penup()
        trt.goto(-image_side, -image_side)
        trt.pendown()
        trt.begin_fill()
        trt.goto(-image_side, image_side)
        trt.goto(image_side, image_side)
        trt.goto(image_side, -image_side)
        trt.goto(-image_side, -image_side)
        trt.end_fill()
        trt.color(grid_colour)
        trt.pensize(pensize)
        vertical = image_side
        horisontal = image_side
        square_side = square_side
        line_length = -(image_side)
        lower_bound = -(image_side)
        trt.speed(0)
        # Draw vertical lines until we have hit the bottom of our image
        while vertical >= lower_bound:
            trt.penup()
            trt.goto(vertical, lower_bound)
            trt.pendown()
            trt.goto(vertical, horisontal)
            vertical -= square_side
        vertical = image_side
        # Draw horisontal lines until we have hit the bottom of our image
        while horisontal >= lower_bound:
            trt.penup()
            trt.goto(lower_bound, horisontal)
            trt.pendown()
            trt.goto(vertical, horisontal)
            trt.color(intersection_colour)
            # Draw the dots on every horizontal line
            while line_length <= (-1*lower_bound):
                trt.pendown()
                trt.dot()
                line_length += square_side
                trt.penup()
                trt.backward(square_side)
            trt.color(grid_colour)
            line_length = lower_bound
            horisontal -= square_side
        # Save the canvas as an eps file
        trt.getscreen().getcanvas().postscript(file="result.eps")
        app.setLabel("info", "Drawing finished, result available at result.eps in current working directory")
    except turtle.TurtleGraphicsError:
        app.setLabel("info", "Please use valid colours")


def press(b):
    """
    Handles the button presses in the UI.
    :param b: the button pressed
    :return: None
    """
    if b == "Cancel":
        app.stop()
    else:
        try:
            # Get the labels and parse the necessary values
            line_colour = app.getEntry("Colour of lines: ")
            bg_colour = app.getEntry("Colour of squares: ")
            dot_colour = app.getEntry("Colour of dots: ")
            try:
                line_size = float(app.getEntry("Width of the lines: "))
                square_side = float(app.getEntry("Length of square side: "))
                image_side = float(app.getEntry("Length of image side: "))
                # Call the draw function
                if line_colour == "" or bg_colour == "" or dot_colour == "":
                    app.setLabel("info", "Please fill all the fields")
                else:
                    app.setLabel("info", "Drawing")
                    draw(line_colour, bg_colour, dot_colour, square_side, line_size, image_side)
            except ValueError:
                app.setLabel("info", "Please use numbers in the last three input fields")
        except TclError:
            print("Error: Exited window before drawing finished")


# Start a new UI
app = gui()
# Declare a global turtle
trt = turtle.Turtle()
# Declare the labels
app.addLabel("title", "Illusion drawer")
app.addLabelEntry("Colour of lines: ")
app.addLabelEntry("Colour of squares: ")
app.addLabelEntry("Colour of dots: ")
app.addLabelEntry("Width of the lines: ")
app.addLabelEntry("Length of square side: ")
app.addLabelEntry("Length of image side: ")
app.addLabel("info", "Press draw to start creation process (all fields must be filled)")

# Add the buttons
app.addButtons(["Create", "Cancel"], press)
app.go()
