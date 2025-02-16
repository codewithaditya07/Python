# sum =0
# for i in range (1,51):
#     if(i%5!=0):
#         print("number",i)
#         sum +=i
# print("sum of",sum)

# sum = 0
# for i in range (1,21):
#     i = i *i
#     print("squre",i)
#     sum +=i
# print("the sum ",sum)

# light =input("light is:- ")
# if (light == "red"):
#     print("stop")
# elif (light == "yellow"):
#     print("wait")
# elif (light == "green"):
#     print("go")
# else:
#     print("light is broken")

#write a program to input 2 number & print the sum
# sum1 = int(input("enter first no "))
# sum2 = int(input("enter second no "))

# print("the sum of",sum1 + sum2)

# write a program to input side of square & print its area
# side = float(input("enter the no "))
# print("the area is",side**2)

# write a program to 2 floating point number and find average
# a = float(input("first no "))
# b = float(input("second no "))
# print("the avg is ", (a+b)/2)


# Slicing 
# str = "hello i am adii"
# print(str[11:15])
# print(str[0:15])
# print(str[0:5])
# print(str[-15:-10])
# print(str[-4:-1])

# list method

# 1. list.append()
# lst =[1,2,3,4]
# lst.append(5)
# lst.sort()
# print(lst)

# shopping cart program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input("food to by(q to quit):")
#     if food.lower() == "q":
#         break
#     else :
#       price = float(input(f"price of food {food}: RS "))
#       foods.append(food)
#       prices.append(price)
# print(".....your cart.....")

# for food in foods :
#    print(food, end =" ")
# for price in prices:
#    total += price
# print() 
# print(f"your toatal bill is: RS{total}")    

#  number pad
# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*",0,"#"))
# for row in num_pad:
#    for num in row:
#       print(num, end = " ")
#    print()  

 

# importing Required modules
# For More Projects Visit : Codewithcurious.com/projects
# import turtle
# import colorsys

# # Create window to Display Pattern
# t = turtle.Turtle()
# s = turtle.Screen()

# # Setting Background color
# s.bgcolor("black")

# # Speed of turtle to draw pattern
# t.speed(0)

# n = 36
# h = 0

# # Loop for drawing Pattern
# for i in range(460):
#     c = colorsys.hsv_to_rgb(h,1,0.9)
#     h+=1/n
#     t.color(c)
#     t.left(145)
#     for j in range(5):
#         t.forward(300)
#         t.left(150)

# Importing the Suboprocess module
# import subprocess

# running command
# command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))
# input("")


i=0
while(i<=10):
    print(i)
    i += 1