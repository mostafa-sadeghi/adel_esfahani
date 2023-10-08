# result = 5 + 3 * 2
# print(result)

# name = "adel"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])


# for x in name:
#     print(x)


# a = '3'
# b = "2"

# print(a + b)

# print(3 * '2')


# name = input("enter a name: ")
# course = input("enter course's name: ")

# message = f"{name} is learning {course}"
# print(message)

# number_1 = int(input("Enter first Number: "))
# number_2 = int(input("Enter second Number: "))

# result = number_1 + number_2

# print(f"{number_1} + {number_2} = {result}")
# print(f"{number_1} - {number_2} = {result}")
# print(f"{number_1} * {number_2} = {result}")
# print(f"{number_1} / {number_2} = {result}")


shopping_list = "eggs, milk, cheese, butter"
print(shopping_list[0:4])
print(shopping_list[6:10])

shopping_list = ["eggs", "milk", "cheese", "butter", 1]
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[4])

import time
new_item = input("enter what you want: ")
shopping_list.append(new_item)
print(f"{new_item} has been appended to the list...")
time.sleep(3)
print(shopping_list)