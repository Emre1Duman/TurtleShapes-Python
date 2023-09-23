from turtle import Turtle, Screen
import random

nina = Turtle()
nina.shape("turtle")
# nina.color("red")


colors = ["light slate gray", "cornflower blue", "turquoise", "cadet blue", "dark slate gray", "olive drab", "firebrick", "medium purple", "red", "chartreuse"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        nina.forward(100)
        nina.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)
    nina.color(random.choice(colors))


screen = Screen()
screen.exitonclick()