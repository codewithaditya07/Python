# 1. Check if a number is even or odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check_even_odd(5))  # Odd

# 2. Sum of digits of a given number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
print(sum_of_digits(1234))  # 10

# 3. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar"))  # True


# 4. Factorial of a number using recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # 120


# 5. Find the second largest element in a list
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None
print(second_largest([10, 20, 4, 45, 99]))  # 45


# 6. Count occurrences of each character in a string
from collections import Counter
def char_count(s):
    return dict(Counter(s))
print(char_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# 7. Reverse a list without using reverse() method
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]


# 8. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(29))  # True


# 9. Merge two sorted lists into a single sorted list
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]


# 10. Find the longest word in a given sentence

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example usage
print(longest_word("Python is an amazing programming language"))  # Output: programming
