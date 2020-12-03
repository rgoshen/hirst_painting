# extract colors from image.jpg and create an rgb tuple list
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
from random import choice

t.colormode(255)
pen = t.Turtle()
pen.speed("fastest")
pen.hideturtle()

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
number_of_dots = 100
number_of_dots_row = 10
x_start = -300
y_start = -200
y_next = y_start

# initial position
pen.penup()
pen.setx(x_start)
pen.sety(y_start)

for dot_count in range(1, number_of_dots + 1):
    pen.dot(20, choice(color_list))
    pen.forward(50)

    if dot_count % number_of_dots_row == 0:
        y_next += 50
        pen.setx(x_start)
        pen.sety(y_next)


screen = t.Screen()
screen.exitonclick()
