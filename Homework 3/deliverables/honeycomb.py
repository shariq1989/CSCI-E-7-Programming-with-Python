import turtle

# global variable for setting edge length
edge = 50

'''
Shariq Jamil

This function takes in a turtle (https://docs.python.org/3/library/turtle.html) and 
draws a honeycomb.
'''
def draw_honeycomb(t):
    # set turtle's stroke width
    t.pensize(5)
    # position cursor for drawing from center of hex
    position_from_center(t)
    # draw the center hexagon
    draw_hexagon(t)
    # draw the six surrounding hexes
    for hex_count in range(6):
        # set hexagon center
        set_position(t, hex_count)
        # draw the hexagon
        draw_hexagon(t)
    turtle.done()


def set_position(t, hex_count):
    t.penup()
    # always start from the center
    t.setposition(0, 0)

    # set direction and move towards the center of surrounding hex
    t.setheading(60 * (hex_count))
    t.forward(edge)
    t.right(60)
    t.forward(edge)

    t.pendown()
    # move turtle to drawing position
    position_from_center(t)


# moves turtle from center to hex drawing position
def position_from_center(t):
    t.penup()
    # point and move north
    t.setheading(90)
    t.forward(edge)

    # move to the beginning of the top side of hex
    t.left(90)
    t.forward(edge / 2)
    t.pendown()


def draw_hexagon(t):
    t.right(180)
    # draw six sides of the hexagon
    for i in range(6):
        # draw the length of the globally defined edge
        t.forward(edge)
        # position for the next side
        t.right(60)


my_cursor = turtle.Turtle()
# starts the honeycomb program
draw_honeycomb(my_cursor)
