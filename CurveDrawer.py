# from Cay Horstmann's "Java Concepts" pg. 245, Exercises P6.18 and P6.19

import math
import turtle

t = turtle.Turtle()


# equation for P6.18
def f(val):
    return (0.00005 * (math.pow(val, 3))) - (0.03 * (math.pow(val, 2))) + (4 * val) + 200


# equation for P6.19
def g(theta):
    r = math.cos(2 * theta)  # ONLY CHANGE THIS LINE
    cartesian_x = r * math.cos(theta)
    cartesian_y = r * math.sin(theta)
    return cartesian_x * 200, cartesian_y * 200


def drawCartesian():
    # x-pixels over which to graph
    x_min = 0
    x_max = 400
    # initializing starting x-position of turtle
    x = x_min
    # graph smoothness modifier (in intervals), a higher number of intervals takes longer to graph but looks smoother
    graph_smooth = 100
    d = (x_max - x_min) / graph_smooth

    for i in range(graph_smooth):
        t.penup()
        coord1 = (x, f(x))
        t.goto(coord1)

        t.pendown()
        x += d
        coord2 = (x, f(x))
        t.goto(coord2)


def drawPolar():
    # x-pixels over which to graph
    x_min = 0
    x_max = 2 * math.pi
    # initializing starting x-position of turtle
    x = x_min
    # graph smoothness modifier (in intervals), a higher number of intervals takes longer to graph but looks smoother
    graph_smooth = 100
    d = (x_max - x_min) / graph_smooth

    for i in range(graph_smooth):
        t.penup()
        coord1 = g(x)
        t.goto(coord1)

        t.pendown()
        x += d
        coord2 = g(x)
        t.goto(coord2)


drawCartesian()
# drawPolar()
turtle.done()
