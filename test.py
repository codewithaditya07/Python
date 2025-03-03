# # 1. Check if a number is even or odd
# num = int(input("Enter any number:-"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

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

# # 4. Factorial of a number using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
print(factorial(5))

# # 5. Find the second largest element in a list
# def second_largest(lst):
#     unique_sorted = sorted(set(lst), reverse=True)
#     return unique_sorted[1] if len(unique_sorted) > 1 else None
# print(second_largest([10, 20, 4, 45, 99]))  # 45


# # 6. Count occurrences of each character in a string
# def count_characters(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     return char_count

# # Example usage
# string = "hello world"
# result = count_characters(string)
# print(result)


# # 7. Reverse a list without using reverse() method
# def reverse_list(lst):
#     return lst[::-1]
# print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]


# # 8. Check if a number is prime
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(29))  # True


# # 9. Merge two sorted lists into a single sorted list
# def merge_sorted_lists(lst1, lst2):
#     return sorted(lst1 + lst2)
# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]


# # 10. Find the longest word in a given sentence

# def longest_word(sentence):
#     words = sentence.split()
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest

# # Example usage
# print(longest_word("Python is an amazing programming language"))  # Output: programming
