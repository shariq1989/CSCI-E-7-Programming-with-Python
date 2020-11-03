import turtle

'''
Shariq Jamil

This function takes in a turtle (https://docs.python.org/3/library/turtle.html), an edge length
and the number of boxes per side. Using these parameters, the method draws a grid.
'''


def draw_grid(t, edgeLen, count):
    # set turtle's stroke width
    t.pensize(5)
    # calculate half length of grid. This will be used to
    # center the grid
    half_grid_length = edgeLen * (count / 2)
    # place cursor so that grid is centered
    set_initial_position(t, half_grid_length)
    # for the number of boxes per side
    for square_num in range(count):
        # draw the row
        draw_row(t, edgeLen, count, half_grid_length)
        # position the cursor in preparation for the next draw
        move_down(t, edgeLen, square_num, half_grid_length)
    turtle.done()


def set_initial_position(t, half_grid_length):
    t.penup()
    # set starting position so that grid is drawn centered
    t.setposition(-half_grid_length, half_grid_length)
    t.pendown()


# moves the turtle under the previous row in
# preparation for the next row
def move_down(t, edgeLen, square_num, half_grid_length):
    # move the cursor under the row that was just drawn
    # edgeLen * 2 is used to account for the initial position used for centering
    move_cursor(t, -half_grid_length, half_grid_length - edgeLen * (square_num + 1))


# moves the turtle to the given coordinates without drawing
def move_cursor(t, x_axis, y_axis):
    t.penup()
    t.setposition(x_axis, y_axis)
    t.pendown()


# moves the turtle to the top right of the previously drawn
# square in preparation for the next square
def move_right(t, edgeLen):
    t.penup()
    t.forward(edgeLen)
    t.pendown()


# draws a row of squares
def draw_row(t, edgeLen, count, half_grid_length):
    # for the prescribed number of squares on a side
    for i in range(count):
        # draw a square
        draw_square(t, edgeLen)
        # get in position for the next square
        move_right(t, edgeLen)
    # reset turtle's position
    move_cursor(t, -half_grid_length, half_grid_length)


def draw_square(t, edgeLen):
    # for each side of a square
    for i in range(4):
        # draw the side
        t.forward(edgeLen)
        # position to draw the next side
        t.right(90)


my_cursor = turtle.Turtle()
draw_grid(my_cursor, 50, 4)
