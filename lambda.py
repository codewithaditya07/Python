# lambda arguments : expression

# add_10 = lambda  x:x+10
# print(add_10(5))


# product of sum
# mul_2 = lambda x,y : x*y
# print(mul_2(10,2))

# map function
# map(function,iterable)

# lst = [2,4,6,8]
# lst2 = list(map (lambda x:x**2,lst))
# print(lst2)

# def square(x):
#     return x**2

# number =[ 1,2,3,4]
# square_num= map(square,number)
# print(list(square_num))



# num1 =[1,2,4]
# num2 =[2,4,8]

# sum = map(lambda x,y:x+y,num1,num2)
# print(list(sum))


# given a list of number add 5 to each using map

# lst = [10,20,30,40,50]
# add = map(lambda x:x+5,lst)
# print(list(add))

# wap list of tem to cel using map funcion
cel = [10,20,30,40]
tem = map (lambda x:x*9/5+32,cel)
print(list(tem))


# num = [-1,2,-3,4]
# re = list(map(lambda x : 0 if x < 0 else x , num))
# print(re)

# write a python program  to double even and and square the  odd number using labmda and map

# num = [1,2,3,4,5,6]
# re= map(lambda x : x*2 if x%2==0 else x**2,num )
# print(list(re))

# in phthon filter is a built function use to flietr elemt iterble(list , tuple) based on a specific condtiton
# filter(function,iterable)

# num =[1,2,3,4,5,6,7,8,9]
# num1 = filter(lambda x: x % 2 == 0 , num)
# print(list(num1))
# def num1(x):
#     return x> 3
# num = [ 1,2,3,4,5]
# num1 = filter(num1, num)
# print(list(num1))
