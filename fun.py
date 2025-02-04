# function

# Q1 WRITE A PROGRAM TO RECEVIE THREE INTERGERS FROM KEYORAD AND GET THEIR 
# SUM AND PRODUCT CALCULATE THROUGH A USER - DEFINED FUNCTION CAL_SUM_PROD()
# def cal_sum_prod(a,b,c):
    # print("sum of",a+b+c)
    # return a+b+c,a*b*c

# a=cal_sum_prod(4,2,3)
# print(a)
# print(cal_sum_prod(2,4,5))

# 13.3 if the input string is "here-come-the-dots-followed-by-dashes"
# then, the converted string should be "by-come-dashes-dots-followed-here-the"

# s1="here-come-the-dots-followed-by-dashes"
# def convert(s):
#   ss=[x for x in s.split('-')]
#   print(ss)
#   ss.sort()
#   print(ss)
#   c= '-'.join(ss)
#   return c

    
# a = convert(s1)
# print(a)

# Q1 write a python function to create and return a lsit containig tuples
# of the from (x,x2,x3)for all x between 1 to 20(both included)

# def z():
#     a =[(x,x**2,x**3) for x in range (1,21)]
#     print(a)

# z()

# q13.6 
# s= "Sakhi was a singer because her mother was a singer , and  Sakhi/'s mother was a singer because her fahter was a singer"
# def convert(s):
#     word =(x for x in s.split(" "))
#     return " ".join(sorted(list(set(word))))       
#     print(word)

# a= convert(s)
# print(a)


# q13.7
# a="james bond 8007"
# def count_alpha_digits(a):
#     d={"alphabet": 0,"digit" : 0}
#     for i in a:
#         if i.isalpha():
#             d["alphabet"]+=1
#         elif i.isdigit():
#           d["digit"]+=1
#         else:
#             pass
#     return d

# b = count_alpha_digits(a)
# print(b)


# write a function to calculate the sum of digit of a number
num = 1234
def cal(num):
    total = 0
    while num>0:
        digit = num%10
        total += digit
        num = num//10
    return total
print(cal(num))


#write a function to find the largest number in the list
# num=[1,2,3,4,5,6,8,9]
# def largest(num):
#     largest=0
#     for i in num:
#         if i>largest:
#             largest=i
#     return largest
# b=largest(num)
# print(b)