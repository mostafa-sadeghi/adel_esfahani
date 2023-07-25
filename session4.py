# for i in range(5):
#     print("hello world")
#     print("welcome")
# print("outside")
#
# for i in range(5):
#     print(i)


# for i in range(10):
#     print(i, end=" ")
#
# print()
# for i in range(1, 11):
#     print(i, end=" ")
#
# print()
# for i in range(2,10,2):
#     print(i, end=" ")


for number in range(10, 0, -1):
    print(number, end=" ")
print()

for number in range(10, -1, -1):
    print(number, end=" ")
print()

numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    print(n, end=" ")
print()

total = 0
for n in numbers:
    total += n

print("total is:",total)

# TODO
"""
with for loop and turtle, write a program which draws these shapes:
triangle, square, pentagon, hexagon, heptagon, octagon, nonagon

"""