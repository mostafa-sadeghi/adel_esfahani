# import turtle

# main_screen = turtle.Screen()
# my_turtle = turtle.Turtle()
# my_turtle.shape("turtle")
# my_turtle.pensize(4)
# my_turtle.pencolor("red")

# sides = int(main_screen.textinput("sides", "How many sides do you want?"))

# def my_function():
#     my_turtle.fillcolor("cyan")
#     my_turtle.begin_fill()
#     # for i in range(sides):
#     #     my_turtle.forward(100)
#     #     my_turtle.left(360/sides)

#     i = 0
#     while i < sides:
#         my_turtle.forward(100)
#         my_turtle.left(360/sides)
#         i += 1


#     my_turtle.end_fill()

# my_function()

# turtle.done()


import turtle

main_screen = turtle.Screen()

my_turtle = turtle.Turtle()


def draw_star(tcolor):
    my_turtle.color(tcolor)
    my_turtle.begin_fill()
    for i in range(5):
        my_turtle.forward(100)
        my_turtle.right(144)

    my_turtle.end_fill()

mycolor = main_screen.textinput("Color Selection","Enter your favorite color")

draw_star(mycolor)


turtle.done()


