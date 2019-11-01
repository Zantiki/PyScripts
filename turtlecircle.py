# Sebastian Ikin, 23/09-19

import turtle
import math
from _tkinter import TclError


# Method to reset the screen, write the drawing-type and prep the turtle
def set_up(r, main_func):
    # Reset the window for a new drawing
    wnd.resetscreen()
    trt.penup()
    trt.goto(-250, 250)
    trt.pendown()
    #  Write what function its currently using for the drawing
    trt.write(main_func)
    # Sets the speed, position and circle for the turtle to work with
    trt.speed(50)
    trt.penup()
    trt.goto(0, -r)
    trt.pendown()
    trt.circle(r)


# Returns a list of our points.
def get_points(point_amount, radius):
    points = []
    i = 0
    while i < point_amount:
        # Add the point to our list.
        points.append(gen_point(point_amount, radius, i))
        i += 1
    return points


# Sets an iterable generator object where our points are the iterations.
def get_points_generated(point_amount, radius):
    i = 0
    while i < point_amount:
        # Make the point an iteration in the generator object.
        yield (gen_point(point_amount, radius, i))
        i += 1


# Calculates and returns a specific point based on the given index.
# the point is a list with two values in it.
def gen_point(point_amount, radius, point_goto_index):
    current_angle = (360/point_amount) * point_goto_index
    # Calculations based on the formula of a circle.
    x = radius * math.cos(math.radians(current_angle))
    y = radius * math.sin(math.radians(current_angle))
    return [x, y]


# Primary drawing method utilizing the generator object.
def draw_lines_generated(multiplier, radius, point_amount):
    # Reset window and turtle.
    set_up(radius, "using generator")
    # Create a reference to our generator object.
    points = get_points_generated(point_amount, radius)
    # An index reference variable (Used to keep track of an iterations position on the circle).
    i = 0
    # Iterate through our generator.
    for point in points:
        # Multiply, adjust and set the index of our goto_point.
        point_goto_index = (i * multiplier) % point_amount
        trt.penup()
        trt.goto(point[0], point[1])
        trt.pendown()
        # Call our gen_point function as finding this in the generator would require loading the iterations
        # (i.e looping until its found) between point and goto_point into memory,
        # losing a primary benefit of our generator.
        goto_point = gen_point(point_amount, radius, point_goto_index)
        # Draw the line between point and goto_point.
        trt.goto(goto_point[0], goto_point[1])
        # Increment our index reference.
        i += 1


# Primary drawing method utilizing lists and a while loop
def draw_lines(multiplier, radius, point_amount):
    # Reset our window and turtle.
    set_up(radius, "traditional list")
    # Get our list of points.
    points = get_points(point_amount, radius)
    i = 0
    while i < point_amount:
        # Calculate what index you would like the turtle to draw to next.
        point_index = (i * multiplier) % point_amount
        # Move our turtle to the next point, where the 0 index represents the x
        # and the 1 represents the y.
        trt.penup()
        trt.goto(points[i][0], points[i][1])
        trt.pendown()
        # Draw the line between i and i*multiplier.
        trt.goto(points[point_index][0], points[point_index][1])
        # Increment our i to the next point on the circle.
        i += 1


# Prompts the user to input the values they want.
p = input("How many points? ")
m = input("Size of multiplier? ")

# Throws an error if the screen is exited before the drawing is finished.
try:
    # Our globally scoped turtle objects.
    trt = turtle.Turtle()
    wnd = turtle.Screen()
    # Calls each of the draw functions, one coming after the other.
    draw_lines_generated(int(m), 200, int(p))
    draw_lines(int(m), 200, int(p))
    wnd.exitonclick()
# Error thrown if screen is exited too early.
except TclError:
    print("Error: Exited window before drawing finished")
