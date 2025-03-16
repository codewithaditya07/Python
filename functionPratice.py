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

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")