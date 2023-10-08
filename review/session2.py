# my_list = ['a', 'bbb', 'cccccc', 'dddddddd']
# my_list[0] = 'aaaaaaaaaaaaaaaaaaa'
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[-1])
# print(my_list[len(my_list) - 1])

# new_item = input("enter a new item: ")
# my_list.append(new_item)

# print(my_list)

# my_list.remove('bbb')
# print(my_list)

# print(my_list[:2])
# print(my_list[1:3])


# numbers = [1,2,3,4,5]
# numbers.remove(5)
# print(numbers)
# del numbers[1]
# print(numbers)
# numbers.pop(0)
# print(numbers)


# numbers = (1,2,3,4,5)
# print(numbers[0])
# print(numbers[:2])
# for i in range(len(numbers)):
#     print(numbers[i])


# numbers = [1,2,3,4,5,6,7]
# total = 0
# for x in numbers:
#     total += x
# print(total)

# total = 0
# for i in range(len(numbers)):
#     total += numbers[i]
# print(total)


import turtle

my_screen = turtle.Screen()
my_turtle = turtle.Turtle()

my_turtle.shape("turtle")

my_turtle.pensize(5)


def draw_star(x,y,color):
    my_turtle.pencolor(color)
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()
    i = 0
    while i < 5:
        my_turtle.fd(150)
        my_turtle.right(144)
        i += 1  # i = i + 1

draw_star(-220,0, "red")
draw_star(-20,0, "cyan")
draw_star(-120,0, "blue")
draw_star(-220,120, "red")
draw_star(-20,120, "cyan")
draw_star(-120,120, "blue")

turtle.done()
