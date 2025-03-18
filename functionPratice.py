# Write a program to create a function that takes two arguments, name and age, and print their value.
# def first(name,age):
#     print(name,age)
# first("parth",20)

# Write a program to create function func1() to accept a variable length of arguments and print their value.
# def func1(*args):
#     for i in args:
#         print(i)

# func1(20, 40, 60)
# func1(80, 100)

# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
# Also, it must return both addition and subtraction in a single return call.

# def  calculation(a,b):
#     add = a+b
#     sub = a-b
#     return add,sub

# cal = calculation(80,40)
# print(cal)


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)

# show_employee("Ben", 12000)
# show_employee("Jessa")

# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
# # outer function
# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# result = outer_fun(5, 10)
# print(result)

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# def addition(num):
#     if num: 
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)

# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)

# showStudent = display_student
# showStudent("Emma",26)

# Generate a Python list of all the even numbers between 4 to 30

# print(list(range(4, 30, 2)))

# Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]

print(max(x))