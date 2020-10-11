import turtle

'''
Shariq Jamil

This function takes in a turtle (https://docs.python.org/3/library/turtle.html) and 
draws a rainbow.
'''

def draw_rainbow():
    # instantiate screen as the sky
    sky = turtle.Screen()
    sky.bgcolor('light blue')

    # instantiate rainbow turtle
    cursor = turtle.Turtle()
    cursor.pensize(10)

    # draws a ray for each color in the rainbow
    for ray_num in range(7):
        draw_ray(cursor, ray_num)
    # draws the ground below the rainbow
    draw_ground(cursor)
    turtle.done()


def draw_ground(cursor):
    # set ground color
    cursor.color('brown')
    # position left of the rainbow without drawing
    cursor.penup()
    cursor.setposition(-300, 0)
    cursor.pendown()
    # draw ground under the rainbow
    cursor.setposition(200, 0)


def draw_ray(cursor, ray_num):
    # color order is inverted because the rainbow is drawn in reverse order
    colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    # set cursor color based on order
    cursor.color(colors[ray_num])
    # draw the ray
    draw_semicircle(cursor, ray_num)


def draw_semicircle(cursor, ray_num):
    cursor.penup()
    # set position so that the rainbow will be centered
    cursor.setposition((ray_num * 10) + 50, 0)
    cursor.setheading(90)
    cursor.pendown()

    # set the radius of the innermost ray (violet)
    smallest_radius = 100
    # draw a semi circle
    cursor.circle(smallest_radius + (ray_num * 10), 180)


draw_rainbow()
