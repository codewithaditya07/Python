# Write a program to create a new string made of an input string’s first, middle, and last character.

# str1 = 'James'
# print("Original String is", str1)

# res = str1[0]

# l = len(str1)

# mi = int(l / 2)

# res = res + str1[mi]

# res = res + str1[l - 1]

# print("New String:", res)

# Write a program to create a new string made of the middle three characters of an input string.

# def get_middle_three_chars(str1):

#     print("Original String is", str1)

#     mi = int(len(str1) / 2)

#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)

# get_middle_three_chars("JhonDipPeta")
# get_middle_three_chars("JaSonAy")

# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)
    mi = int(len(s1) / 2)

    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")


