# write a program to print all even number between 1 t 20 using for loop

# for i in range (1,21):
#     if(i%2==0):
#         print("Even Numbers are : " , i)
#     else:
#         pass

# write a program that check if number from 1 to 50 are divisible  by 3 and  print "FIZZ" for those numbers

# for i in range(1,51):
#     if (i%3==0):
#         print("FIZZ")

# Write a program to count how many numbers between 1 and 100 are divisible by both 3 and 5
# count = 0
# for i in range(1,101):
#     if ((i%3 == 0) and (i%5 == 0)):
#         print("The number is " ,i)
#         count += 1
# print("Count = " , count)

# Write a program that prints "Even" or "Odd" for every number from 1 to 10

# for i in range(1,11):
#     if(i%2==0):
#         print("Even " , i)
#     else:
#         print("odd" , i)

# Write a program to calculate the sum of all numbers from 1 to 50 but exclude numbers divisible by 5.
# sum = 0
# for i in range(1,51):
#     if(i%5!=0):
#        print("The numbers are : " , i)
#        sum +=1
# print("The sum is : " , sum)

# Write a program to calculate the sum of the squares of all numbers from 1 to 20

# sum = 0
# for i in range(1,21):
#     i = i*i
#     sum = sum + i
#     print(i)
# print("The sum of squares are" ,sum)

# Write a program to count the number of vowels in a given string using a for loop and an if statement.
# text = "Hello, how are you?"
# vowels = "aeiouAEIOU"
# count = 0
# for i in text:
#     if i in vowels:
#         print(i)
#         count +=1
# print(count)

# Write a program to count the number of positive and negative numbers in a list.
# numbers = [-10, 15, -20, 25, -5, 30]
# positive_count = 0
# negative_count = 0
# for i in numbers:
#     if (i<0):
#         print("Negative Numbers are : " , i)
#         negative_count +=1
#     else:
#         print("Positive numbers are : " , i)
#         positive_count +=1
# print("Positive counts are : " , positive_count)
# print("Negative counts are : " , negative_count)

#Question:- A company insures its drivers in the following cases 
# If the driver is married
# If the driver is unmarried , male and above 30 years of age
# If the driver is unmarried , female and above 25 years of age
# In all the cases , the driver is not insured. If the martial status,sex and age as a input, write a program to determie whether the driver should be insured or not

print("Enter Every Input in lowercase")
Martial_status = input("Enter Your Martial Status : ")
Gender = input("Enter Your Gender : ")
Age = int(input("Enter Your Age : "))

if ((Martial_status == "unmarried" or "u") and (Gender =="male" or "m") and (Age > 30)):
    print("You are insured")
elif ((Martial_status == "unmarried" or "u") and (Gender =="female" or "f") and (Age > 25)):
    print("You Are insured")
elif (Martial_status == "married" or "m"):
    print("You are Insured")
else:
    print("Your are not insured")