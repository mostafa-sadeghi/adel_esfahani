# write a program that takes user's name and family and age from input
# and if the user's age is greater than 18 prints "you are adult"
# if the user's age is between 13 and 18 prints "you are teenager"
# else print "you are kid".

# name = input("enter your name: ")
# age = int(input("enter your age: "))


# if age >= 18:
#     print("you are adult")
# # elif age >= 13 and age < 18:
# elif 13 <= age < 18:
#     print("you are teenager")
# else:
#     print("you are kid")

# write the program that takes user's name and print his/her name's chars seperately
name = input("enter the name: ")
print(len(name))
for x in name:
    print(x)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# with for loop print each number from the above list
# with for loop calculate sum of all numbers in that list