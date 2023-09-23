from turtle import Turtle, Screen
import random


screen = Screen()
nina = Turtle()
nina.shape("turtle")
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color



colors = ["light slate gray", "cornflower blue", "turquoise", "cadet blue", "dark slate gray", "olive drab", "firebrick", "medium purple", "red", "chartreuse"]
directions = [0, 90, 180, 270]
nina.width(10)
nina.speed(0)


for _ in range(200):
    nina.color(random_color())
    nina.forward(30)
    nina.setheading(random.choice(directions))
    

screen.exitonclick()