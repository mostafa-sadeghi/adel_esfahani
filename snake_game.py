from turtle import Screen, Turtle
from random import randint
from time import sleep
import turtle
main_screen = Screen()
main_screen.bgcolor("black")
main_screen.title("snake Game")
main_screen.setup(600, 600)


def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    x = randint(-280, 280)
    y = randint(-280, 230)
    object.goto(x, y)


def move_snake():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)


main_screen.listen()
main_screen.onkeypress(go_up, "Up")
main_screen.onkeypress(go_up, "w")
main_screen.onkeypress(go_down, "Down")
main_screen.onkeypress(go_down, "s")
main_screen.onkeypress(go_left, "Left")
main_screen.onkeypress(go_left, "a")
main_screen.onkeypress(go_right, "Right")
main_screen.onkeypress(go_right, "d")

main_screen.tracer(False)
snake_tails = []
score = 0


running = True
while running:
    main_screen.update()
    turtle.penup()
    turtle.goto(0, 260)
    turtle.color("white")
    turtle.ht()
    turtle.clear()
    turtle.write(f"Score: {score}", font=("arial", 22), align="center")
    if snake_head.distance(snake_food) < 20:
        score += 1
        change_position(snake_food)
        new_tail = create_turtle("square", "green")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        snake_head.home()
        snake_head.direction = ""
        score = 0

    move_snake()
    sleep(0.2)
