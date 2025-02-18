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

word=input('input string:-')
print("Original String:", word)
size=len(word)
print("print only even index chars")
for i in range (0,size -1,2):
    print("index[",i,"]",word[i])
