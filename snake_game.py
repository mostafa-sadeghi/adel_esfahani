from turtle import Screen, Turtle
from random import randint
from time import sleep
main_screen = Screen()
main_screen.bgcolor("black")
main_screen.title("snake Game")
main_screen.setup(600, 600)

def create_turtle(tshape, tcolor):
    my_turtle= Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    x = randint(-280, 280)
    y = randint(-280, 230)
    object.goto(x,y)

def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

def go_up():
    snake_head.direction = "up"

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)


main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_up, "w")

running = True

while running:
    main_screen.update()
    move_snake()
    sleep(0.2)