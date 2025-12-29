# comprehension

# Q1 generate a list of squares of all no from 1 to 10
# square = [i**2 for i in range (1,11)]
# print(square)

# Q2 create a lsit of all numbers divisible by 3 from 1 to 50
# lst = [i**2 for i in range (1,51) if i%3==0]
# print(lst)

# Q3 extract vowels from the string comprehension
# v="comprehension"
# lst1=[x for x in "comprehension" if x in "aeiou"]
# print(lst1)

# Q4create a list of tuples where each tuple contains a number and list square for number from 1 to 5
# lst2 =[(i,i**2) for i in range (1,6)]
# print(lst2)

# Q5create a dictionary where keys are numbers from 1 to 5 and values are cube
# cube_dic ={i:i**3 for i in range (1,6)}
# print(cube_dic)

# Q6Create a dictionary from 1 to 10 where keys are numbers and values are "even" or "odd" based on the number's parity.
# dic ={i:"even"  if (i%2==0) else "odd" for i in range (1,10) }
# print(dic)

# Q7Create a list of all words in a sentence that are longer than 4 characters.
#sentence = "List comprehension is a powerful feature in Python"
# s=("List comprehension is a powerful feature in Python")
# long_word=[word for word in s.split()if len(word) > 4]
# print(long_word)

# Q8reverse each word in a given list of words
#word = ("hello","world","python","rocks")
# w =  ("hello","world","python","rocks")
# x=[i for i in words[::-1]]
# reversed_words=[i[::-1] for i in w]
# print(reversed_words)


# Q9create a list of common elements between two lists
# lst=[1,2,3,4,5]
# lst1=[3,4,5,76,7]
# x=[x for x in lst if x in lst1]
# print(x)

# Q10CREATE A DICTIONARY FROM A LIST OF WORDS WHERE KEYS ARE THE WORDS
# AND VALUES THE LENGETH OF THOSE WORDS 
# word = ["list","comprehension","is","amazing"]
# dic={x:len(x) for x in word}
# print(dic)


# calculator

# first = input("enter 1st no : ")
# operator = input("choose operator  +,-,*,/,% :- ")
# second = input("enter 2nd no : ")

# first = int(first)
# second = int(second)

# if operator == '+':
#     print( first + second)
# elif operator == '-':
#     print( first - second)
# elif operator == '*':
#     print( first * second)
# elif operator == '/':
#     print( first / second)
# elif operator == '%':
#     print( first % second)
# else:
#    print("invalid operation" )


i = 1
while i <= 5:
    print(i)
    i = i + 1


# i = 1
# while i <= 5:
#     print(i * "*")
#     i = i + 1



