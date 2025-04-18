# if statement
age=20

if age>=18:
    print("You are allowed to vote in the elections")

# else
    age=16

if age>=18:
    print("You are eligible for voting")
else:
    print("You are a minor")

# elif
age=17

if age<13:
    print("You are a child")
elif age<18:
    print("You are a teenager")
else:
    print("You are an adult")

# Nested Condiitonal Statements
num=int(input("Enter the number"))

if num>0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

else:
    print("The number is zero or negative")


# Practical Examples

year=int(input("Enter the year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")

else:
    print(year,"is not a leap year")
    

# Simple Calculator program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform the requested operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

print("Result:", result)