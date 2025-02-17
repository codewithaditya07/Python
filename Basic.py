# Exercise 1: Calculate the multiplication and sum of two numbers

# number1 = 20
# number2 = 30
# multiply = number1 * number2
# add = number1 + number2

# print(multiply)
# print(add)

def multiply_or_sum(num1,num2):
    product = num1*num2
    if product <= 1000:
     return product
    else:
      return num1 + num2
    
result = multiply_or_sum(20,30)
print("the result is ",result) 

result = multiply_or_sum(30,40)
print("the result is ",result) 
    