# Exercise 1: Calculate the multiplication and sum of two numbers

# number1 = 20
# number2 = 30
# multiply = number1 * number2
# add = number1 + number2

# print(multiply)
# print(add)

# def multiply_or_sum(num1,num2):
#     product = num1*num2
#     if product <= 1000:
#      return product
#     else:
#       return num1 + num2
    
# result = multiply_or_sum(20,30)
# print("the result is ",result) 

# result = multiply_or_sum(30,40)
# print("the result is ",result) 
    

# Exercise 2: Print the Sum of a Current Number and a Previous number
# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     previous_num = i

# Exercise 3: Print characters present at an even index number

# word=input('input string:-')
# print("Original String:", word)
# size=len(word)
# print("print only even index chars")
# for i in range (0,size -1,2):
#     print("index[",i,"]",word[i])

# Exercise 4: Remove first n characters from a string

# def remove_chars(word,n):
#     print("original string ",word)
#     x = word[n:]
#     return x
# print("Removing characters from a string")
# print(remove_chars("aditya",4))
# print(remove_chars("parth",2))

# Exercise 5: Check if the first and last numbers of a list are the same
# def first_last_same(numberList):
#     print("Given list:", numberList)
    
#     first_num = numberList[0]
#     last_num = numberList[-1]
    
#     if first_num == last_num:
#         return True
#     else:
#         return False

# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))

# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))


# Exercise 6: Display numbers divisible by 5
# lst = [10, 20, 33, 46, 55]
# print("Given Numbers:- ",lst)
# for i in lst:
#     if(i%5 == 0):
#         print("Display by 5 :-",i)
    

# Exercise 7: Find the number of occurrences of a substring in a string
# word = "Emma is good developer. Emma is a writer"
# cc = word.count("Emma")
# print(cc)

# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
# for num in range(6):
#     for i in range(num):
#         print (num, end=" ") 
#     print("\n")


# Exercise 9: Check Palindrome Number
# str = 'mom'

# if str[:] == str[-1:]:
#     print("palindrome")
# else: 
#    print("not a palindrome")
# Exercise 10: Merge two lists using the following condition
# def merge_list (lst1,lst2):
#     result_list = []
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# odd_from_list1 = [x for x in list1 if x % 2 != 0]
# even_from_list2 = [x for x in list2 if x % 2 == 0]
# new_list = odd_from_list1 + even_from_list2

# print(new_list)

# Exercise 11: Get each digit from a number in the reverse order.
# Number = int(input("Enter any number to reverse :-"))
# while Number > 0:
#   digit = Number % 10
#   Number  = Number // 10
#   print(digit,end="")

# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
# Taxable  Income 	  Rate (in %)
# First    $10,000	    0
# Next    $10,000	    10
# The     remaining	    20

# income = int(input("Enter the income:- "))
# tax_payable = 0

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     x = income - 10000
#     tax_payable = x * 10 / 100
# else:
#     tax_payable = 0
#     tax_payable = 10000 * 10 / 100
#     tax_payable += (income - 20000) * 20 / 100
# print("Total tax to pay is",tax_payable)

# Exercise 13: Print multiplication table from 1 to 10
# for i in range (1,11):
#     for j in range(1,11):
#         print(i * j, end=" ")
#     print("\t\t")

# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# i = 5
# while i >=0:
#     print(i * "*")
#     i = i - 1

# for i in range (5):
#     if i >=0:
#         print(i * "*")
#         i = i -1

# Exercise 15: Get an int value of base raises to the power of exponent
# 1st method
# def exponent (base,exp):
#     num = exp
#     result = 1
#     while num > 0 :
#         result = result * base 
#         num = num - 1
#     print(base,"power of",exp,"is:",result)
# exponent(2,2)

# 2nd method
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# result = pow(base, exponent)
# print(f"{base} raised to the power of {exponent} is {result}")

# Display three string “Name”, “Is”, “James” as “Name**Is**James”

# print("**".join(["Name", "Is", "James"]))

# Convert Decimal number to octal using print() output formatting

# num = 8
# print('%o'% num)

# Display float number with 2 decimal places using print()

# num = 458.541315

# print ('%.2f' % num)

# Accept a list of 5 float numbers as an input from the user
# numbers = []
# for i in range(0, 5):
#     print("Enter number at location", i, ":")
#     item = float(input())
#     numbers.append(item)

# print("User List:", numbers)


# Accept any three string from one input() call
# str1,str2,str3 = input("Enter three string :").split()
# print("First Name :",str1)
# print("Second Name :",str2)
# print("Third Name :",str3)


# Format variables using a string.format() method.
# quantity = 3
# totalMoney = 1000
# price = 450
# statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
# print(statement1.format(quantity, totalMoney, price))

# Print first 10 natural numbers using while loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# row = 5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(j,end=" ")

#     print("")

# Calculate sum of all numbers from 1 to a given number
# n = int(input("Enter Any Number :- "))
# z = sum(range(1,n+1))
# print("The sum is :- ",z)

# Print multiplication table of a given number
# num = 2
# for i in range(1,11):
#     product = num * i
#     print(product)

# Display numbers from a list using a loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if  i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

# Count the total number of digits in a number

# num = 1234588888
# count = 0
# while num != 0:
#     num = num // 10
#     count = count + 1
# print("total numbers of digits",count)

# Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# n =5
# row = 5
# for i in range(0,n+1):
#     for j in range(row-i,0,-1):
#         print(j,end=" ")
#     print("")

# Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]

# reverse_order = list1[::-1]
# print(reverse_order)

# Display numbers from -10 to -1 using for loop

# for num in range(-10,0):
#     print(num)

# Display a message “Done” after the successful execution of the for loop
# for i in range(5):
#     print(i)
# print("Done")

#  Print all prime numbers within a range

# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")

# for num in range(start,end +1):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# Display Fibonacci series up to 10 terms

num1,num2 = 0,1
print("Fibonacci Number :")

for i in range(10):
    print(num1,end=",")
    res = num1 + num2

    num1 = num2
    num2 = res

