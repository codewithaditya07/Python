# 1	Write a program to purposefully raise Indentation Error and Correct it
# Purposefully creating Indentation Error

# def greet():
# print("Hello Student")   # No indentation inside function

# greet()

# # Corrected program
# def greet():
#     print("Hello Student")   # Proper indentation

# greet() 

# 2 Write a program to compute distance between two points taking input from the user (Pythagorean Theorem)
# Program to calculate distance between two points

# Program to calculate distance between two points

# import math

# # Taking input from user
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# # Applying distance formula
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# # Display result with 2 decimal places
# print(f"Distance between two points = {distance:.2f}")

# 3	Write a program add.py that takes 2 numbers as command line arguments and prints its sum

# add.py
# import sys

# # Taking command line arguments
# num1 = float(sys.argv[1])
# num2 = float(sys.argv[2])

# # Calculating sum
# result = num1 + num2

# # Display result
# print("Sum =", result)

# 4	WAP to swap two numbers by using third variable and without using third variable

# Swap using third variable

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Before swapping:")
# print("a =", a, "b =", b)

# # Swapping
# temp = a
# a = b
# b = temp

# print("After swapping:")
# print("a =", a, "b =", b)

# Swap without third variable (Arithmetic method)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Before swapping:")
# print("a =", a, "b =", b)

# a = a + b
# b = a - b
# a = a - b

# print("After swapping:")
# print("a =", a, "b =", b)

# 5	Write a program to calculate area of a triangle	
# Program to calculate area of triangle

# base = float(input("Enter base of triangle: "))
# height = float(input("Enter height of triangle: "))

# area = 0.5 * base * height

# print(f"Area of triangle = {area:.2f}")

# 6	WAP to implement the concept of local and global variable.	
# Global variable
# x = 10

# def show():
#     # Local variable
#     y = 5
#     print("Inside function:")
#     print("Global variable x =", x)   # accessing global variable
#     print("Local variable y =", y)

# show()

# print("\nOutside function:")
# print("Global variable x =", x)
# print(y)   # This will give error because y is local

# 7	WAP to implement various operators	
# Program to demonstrate various operators

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# Arithmetic Operators
# print("\nArithmetic Operators")
# print("Addition =", a + b)
# print("Subtraction =", a - b)
# print("Multiplication =", a * b)
# print("Division =", a / b)
# print("Modulus =", a % b)
# print("Exponent =", a ** b)
# print("Floor Division =", a // b)

# Relational (Comparison) Operators
# print("\nRelational Operators")
# print("a > b :", a > b)
# print("a < b :", a < b)
# print("a == b :", a == b)
# print("a != b :", a != b)
# print("a >= b :", a >= b)
# print("a <= b :", a <= b)

# # Logical Operators
# print("\nLogical Operators")
# print("(a > 0 and b > 0) :", a > 0 and b > 0)
# print("(a > 0 or b > 0) :", a > 0 or b > 0)
# print("not(a > b) :", not(a > b))

# # Assignment Operators
# print("\nAssignment Operators")
# c = a
# c += b
# print("c += b :", c)
# c -= b
# print("c -= b :", c)

# # Bitwise Operators
# print("\nBitwise Operators")
# print("a & b =", a & b)
# print("a | b =", a | b)
# print("a ^ b =", a ^ b)
# print("~a =", ~a)
# print("a << 1 =", a << 1)
# print("a >> 1 =", a >> 1)


x = [1,2,3]
print(x*2)

for i in range(1,5):
    if i==3:
        break
    print(i,end=" ")
    


# print(bool(0), bool(5))