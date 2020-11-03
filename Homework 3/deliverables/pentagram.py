import turtle

'''
Shariq Jamil

This function takes in a turtle (https://docs.python.org/3/library/turtle.html), an edge length
and a pen width. Using these parameters, the method draws a pentagram.
'''


def draw_pentagram(t, edgeLen, penWidth):
    # set turtle's stroke width
    t.pensize(penWidth)
    # place cursor so that pentagram is centered
    set_initial_position(t, edgeLen / 2)
    # for each of the five lines in a pentagram
    for i in range(5):
        # draw the line
        t.forward(edgeLen)
        # turn right for the next line
        t.right(144)
    turtle.done()


def set_initial_position(t, half_edgeLen):
    t.penup()
    # set starting position so that pentagram is drawn centered
    t.setposition(-half_edgeLen, half_edgeLen / 2)
    t.pendown()


my_cursor = turtle.Turtle()
draw_pentagram(my_cursor, 200, 5)
