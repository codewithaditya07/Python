# Write a program to create a new string made of an input string’s first, middle, and last character.

str1 = 'James'
print("Original String is", str1)

res = str1[0]

l = len(str1)

mi = int(l / 2)

res = res + str1[mi]

res = res + str1[l - 1]

print("New String:", res)

# Write a program to create a new string made of the middle three characters of an input string.

# def get_middle_three_chars(str1):

#     print("Original String is", str1)

#     mi = int(len(str1) / 2)

#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)

# get_middle_three_chars("JhonDipPeta")
# get_middle_three_chars("JaSonAy")

# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# def append_middle(s1, s2):
#     print("Original Strings are", s1, s2)
#     mi = int(len(s1) / 2)

#     x = s1[:mi:]
#     x = x + s2
#     x = x + s1[mi:]
#     print("After appending new string in middle:", x)

# append_middle("Ault", "Kelly")


# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
# def mix_string(s1, s2):
    
#     first_char = s1[0] + s2[0]
#     middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

#     last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

#     # add all
#     res = first_char + middle_char + last_char
#     print("Mix String is ", res)

# s1 = "America"
# s2 = "Japan"
# mix_string(s1, s2)


# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

# str1 = "PYnAtivE"
# print('Original String:', str1)
# lower = []
# upper = []
# for char in str1:
#     if char.islower():
#         lower.append(char)
#     else:
#         upper.append(char)

# sorted_str = ''.join(lower + upper)
# print('Result:', sorted_str)


#  Count all letters, digits, and special symbols from a given string

def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
