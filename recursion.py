# recursion
# def recur(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         recur(n-1)
# recur(5)  
# 
# def fun_rec(n):
#     if n==0:
#         return 0
#     return n+fun_rec(n-1)

# a=fun_rec(5)
# print(a)

# write a recurive funciton to calculate sum of digit of a number
# def sum_rec(n):
#     if n==0:
#         return 0
#     return n%10 +sum_rec(n//10)

# a=sum_rec(123)
# print(a)

#  write a recursive function to count the number of digit
# def rec_num(n):
#     if n==0:
#         return 0
#     return 1+rec_num(n//10)

# a=rec_num(12345)
# print(a)

#  write a recurive funtion to revsere a string
# 1 method
# def rev_str(s):
#      if len(s)==0:
#          return s
#      return rev_str(s[1:]) + s[0] 

# a=rev_str("hello")
# print(a)

# 2 method
# n= "hello"
# def reverse(n):
#     if len(n) ==0:
#         return ""
#     return n[-1:] + reverse(n[:-1])
# print(reverse(n))

#  write a recursive function to calculate a some of array in a lsit
# def sum_lst(n,b):
#     if b==0:
#         return 0
    
#     return n[b-1] + sum_lst(n ,b-1)

# print(sum_lst([1,2,3,4,5],5))

# factorial
# def fac(n):
#     if n== 0:
#         return 1
#     return n *fac(n-1)
# print(fac(3))
# find a maximum value in array using recurion

# lst =[1,2,5,8,9]
# n = 5
# def find_max(lst,n):
#     if n==1:
#         return lst[0]
    
#     return max(lst[n-1],find_max(lst,n-1))

# print("max",find_max(lst,n))

# check if array is sorted print ture or false using recursion
# lst=[1,2,3,4]              # lst = [1,2,5,4,2] false

# def sort_arr(lst):
#     if len(lst)<=1:
#         return True
#     return lst[0] < lst[1] and sort_arr(lst[1:])
# print(sort_arr(lst)



# check the string is palindrome print true or false
# word="abccba"
# def pali_str(word):
#     if len(word)<=1:
#         return True
#     return word[0]==word[-1] and pali_str(word[1:-1])
# print(pali_str(word))

# find product of an array using recursion
# lst =[1,5,6]
# n = 3
# def pro_arr(lst,n):
#     if n==0:
#         return 1
#     return lst[n-1]*pro_arr(lst,n-1)
# print(pro_arr(lst,n))

# find  occurence of an element in a list

def ele_lst(arr,target):
    if len(arr)== 0:
        return 0
    return (1 if arr[0]==target else 0) + ele_lst(arr[1:],target)

print(ele_lst([1,2,2,2,3,4,44,5],2))