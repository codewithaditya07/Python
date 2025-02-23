# 1. Basic Syntax – Variables & Data Types

# x = 10       # Integer
# y = 3.14     # Float
# name = "Ali" # String
# nums = [1, 2, 3]  # List
# tup = (4, 5, 6)   # Tuple
# data = {"a": 1, "b": 2}  # Dictionary
# unique_nums = {7, 8, 9}  # Set

# 2. Loops & Conditionals
# # If-elif-else
# num = 10
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # For loop
# for i in range(1, 6):
#     print(i)

# # While loop
# count = 0
# while count < 3:
#     print(count)
#     count += 1

# 3. Functions
# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  # Output: Hello, Alice!


# 4. String Manipulation
# s = "  Python is fun!  "
# print(s.strip())  # Removes spaces -> "Python is fun!"
# print(s.upper())  # Converts to uppercase
# print(s.split())  # ['Python', 'is', 'fun!']
# print("-".join(["Hello", "World"]))  # Output: Hello-World


# 5. Lists & Tuples
# nums = [1, 3, 5, 7]
# nums.append(9)  # Add element
# nums.sort()     # Sort list
# print(nums)     # [1, 3, 5, 7, 9]

# tup = (1, 2, 3)
# print(tup[1])  # Output: 2 (Tuples are immutable)


# 6. Dictionaries & Sets
# # Dictionary
# person = {"name": "John", "age": 25}
# print(person.get("name"))  # Output: John
# print(person.keys())  # dict_keys(['name', 'age'])

# # Set
# unique_vals = {1, 2, 3, 3, 4}
# print(unique_vals)  # Output: {1, 2, 3, 4} (No duplicates)


# 7. File Handling
# # Writing to a file
# with open("test.txt", "w") as file:
#     file.write("Hello, Python!")

# # Reading from a file
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)  # Output: Hello, Python!


# 8. Basic Algorithms – Sorting & Searching
# # Sorting
# nums = [4, 1, 3, 2]
# nums.sort()  # Ascending order
# print(nums)  # Output: [1, 2, 3, 4]

# # Binary Search
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2


# 9. Error Handling – Try-Except
# try:
#     x = 10 / 0  # Division by zero error
# except ZeroDivisionError:
#     print("Cannot divide by zero!")