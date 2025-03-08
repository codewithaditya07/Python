# # 1. Check if a number is even or odd
# num = int(input("Enter any number:-"))
# if num % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")

 # 2. Sum of digits of a given number
# num = 12345
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print(total)
  

#  3. Check if a string is a palindrome
# s = "palindrome"
# a = "level"
# b = "madam"
# print(s == s[::-1])
# print(a == a[::-1])
# print(b == b[::-1])

# 4. Factorial of a number using recursion
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n-1)
# print(factorial(5))

# 5. Find the second largest element in a list
# lst = [10,20,30,40,50]
# sorted_lst = sorted(set(lst),reverse=True)
# print(sorted_lst[1])


# 6. Count occurrences of each character in a string
# s = "hello "
# char_count = {}

# for char in s:
#     char_count[char] = char_count.get(char,0) + 1
#     print(char_count)

# 7. Reverse a list without using reverse() method
# lst = [1,2,3,4,5]
# reversed_lst = lst[::-1]
# print(reversed_lst)

# 8. Check if a number is prime
# def prime (n):
#     if n < 2:
#         return False
#     for i in range (2,n):
#         if n % i == 0:
#          return False
#     return True
# print(prime(7))
# print(prime(10))

# 9. Merge two sorted lists into a single sorted list
# lst1 = [1,3,5,7]
# lst2 = [2,4,8,10]
# merge_lst = sorted(lst1 + lst2)
# print(merge_lst)

# 10. Find the longest word in a given sentence
# s = "hii what are you doing"
# def longest_word(s):
#   word = s.split()
#   return max(word , key=len)
# print(longest_word(s))


# 11.Reverse a word without using reverse() method
# word = "unatti"
# reversed_word = word[::-1]
# print(reversed_word)


# find the second largest number in an array
def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort(reverse=True)  # Sort in descending order
    return arr[1] if len(arr) > 1 else None  # Return second element

numbers = [10, 20, 5, 8, 20, 30]
# numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(second_largest(numbers))  # Output: 20
