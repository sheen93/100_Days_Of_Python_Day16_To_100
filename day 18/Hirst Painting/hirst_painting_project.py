import colorgram
import turtle as t
from color_pallete import final_color_palette
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.shape("turtle")
tim.hideturtle()

# number_of_colors = 100
# colors = colorgram.extract('H8fPT3FdxkC6_4800x4800.jpg', number_of_colors)
#
# def random_color():
#     color = random.choice(colors)
#     rgb_color = color.rgb
#     # return rgb_color
#     return (rgb_color[0], rgb_color[1], rgb_color[2])

tim.pu()
x_pos = -240
y_pos = -240
tim.teleport(x_pos,y_pos)
distance = 50
for j in range(10):
    for j in range(10):
        tim.dot(20, random.choice(final_color_palette))
        tim.fd(distance)
    y_pos += distance
    tim.teleport(x_pos, y_pos)












screen = t.Screen()
screen.exitonclick()