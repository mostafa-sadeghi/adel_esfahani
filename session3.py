import turtle
from time import sleep

main_surface = turtle.Screen()
main_surface.bgcolor("cyan")
main_surface.setup(600, 600)
main_surface.title("my app")
main_surface.bgpic("lui.png")
main_surface.register_shape("strawberry.gif")

my_turtle = turtle.Turtle()
my_turtle.speed("slowest")
my_turtle.shape("strawberry.gif") # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic
my_turtle.pensize(4)
my_turtle.color("red")
# my_turtle.begin_fill()
# my_turtle.forward(150)
# my_turtle.left(90)
# my_turtle.color("green")
# my_turtle.stamp()
# sleep(1)
# my_turtle.color("red")
# my_turtle.forward(150)
# my_turtle.left(90)
# my_turtle.color("green")
# my_turtle.stamp()
# sleep(1)
# my_turtle.color("red")
# my_turtle.forward(150)
# my_turtle.left(90)
# my_turtle.color("green")
# my_turtle.stamp()
# sleep(1)
# my_turtle.color("red")
# my_turtle.forward(150)
# my_turtle.color("green")
# my_turtle.stamp()
# my_turtle.color("red")
# my_turtle.hideturtle()
#
# my_turtle.left(90)

# pentagon    hexagon    heptagon    octagon    nonagon

# my_turtle.end_fill()

my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()


turtle.done()