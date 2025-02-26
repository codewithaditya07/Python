# 1️. Reverse a String Without Using [::-1]
# Problem: Write a function to reverse a string manually.

# def reverse_string(s):
#     reversed_str = ""
#     for char in s:
#         reversed_str = char + reversed_str
#     return reversed_str
# print(reverse_string("hello"))  # Output: "olleh"

# 2️. Find the Second Largest Number in a List
# Problem: Given a list of numbers, find the second largest number.

# def second_largest(nums):
#     unique_nums = list(set(nums))  # Remove duplicates
#     unique_nums.sort(reverse=True)  # Sort in descending order
#     return unique_nums[1] if len(unique_nums) > 1 else None  # Return second largest
# print(second_largest([10, 20, 4, 45, 99]))  # Output: 45

# 3️. Count Occurrences of Words in a String
# Problem: Given a string, count how many times each word appears.

# def word_count(s):
#     words = s.lower().split()
#     word_dict = {}
#     for word in words:
#         word_dict[word] = word_dict.get(word, 0) + 1
#     return word_dict

# print(word_count("apple banana apple orange banana apple"))
# # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# 4️. Check if a Number is Prime
# Problem: Write a function to check if a number is prime.

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(29))  # Output: True
# print(is_prime(10))  # Output: False

# 5️. Sort a Dictionary by Its Values
# Problem: Given a dictionary, sort it by its values in descending order.

# def sort_dict_by_value(d):
#     return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


# data = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}
# print(sort_dict_by_value(data))
# # Output: {'orange': 8, 'apple': 5, 'grape': 3, 'banana': 2}

# 6️. Find the Factorial of a Number
# Problem: Write a function to find the factorial of a number using recursion.

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # Output: 120
# print(factorial(7))  # Output: 5040

# 7️. Check if a String is a Palindrome
# Problem: Write a function to check if a string is a palindrome (same forward and backward).

# def is_palindrome(s):
#     return s == s[::-1]


# print(is_palindrome("madam"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

# 8️. Find the Missing Number in an Array
# Problem: Given an array containing n distinct numbers from 1 to n+1, find the missing number.

# def missing_number(arr):
#     n = len(arr) + 1
#     total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
#     return total_sum - sum(arr)


# print(missing_number([1, 2, 4, 5, 6]))  # Output: 3

# 9️. Find the Intersection of Two Lists
# Problem: Given two lists, find the common elements between them.

# def list_intersection(list1, list2):
#     return list(set(list1) & set(list2))

# # Test
# print(list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]

# 10.Fibonacci Sequence (Recursion)
# Problem: Write a function to generate the Fibonacci sequence up to n terms.

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         seq = fibonacci(n - 1)
#         seq.append(seq[-1] + seq[-2])
#         return seq

# print(fibonacci(6))  # Output: [0, 1, 1, 2, 3, 5]

# 1️. Create a Class and Object
# Problem: Create a class Car with attributes brand and year. Create an object and print the details.

# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

#     def display_info(self):
#         return f"Car: {self.brand}, Year: {self.year}"

# # Create an object
# car1 = Car("Toyota", 2022)
# print(car1.display_info())  # Output: Car: Toyota, Year: 2022

# 2️. Implement Inheritance
# Problem: Create a base class Animal with a method make_sound(). Create a derived class Dog that overrides make_sound().
# class Animal:
#     def make_sound(self):
#         return "Some sound"

# class Dog(Animal):
#     def make_sound(self):  # Overriding method
#         return "Bark!"

# # Create objects
# animal = Animal()
# dog = Dog()
# print(animal.make_sound())  # Output: Some sound
# print(dog.make_sound())     # Output: Bark!

# 3️.Implement Encapsulation (Private Variables)
# Problem: Create a class BankAccount with a private attribute __balance. Add methods to deposit and withdraw money safely.

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private variable

#     def deposit(self, amount):
#         self.__balance += amount
#         return f"Deposited {amount}, New Balance: {self.__balance}"

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             return "Insufficient funds!"
#         self.__balance -= amount
#         return f"Withdrew {amount}, Remaining Balance: {self.__balance}"

# # Create object
# account = BankAccount(1000)
# print(account.deposit(500))  # Output: Deposited 500, New Balance: 1500
# print(account.withdraw(300))  # Output: Withdrew 300, Remaining Balance: 1200

# 4️. Implement Polymorphism
# Problem: Create two classes Cat and Dog, both with a method speak(). Use polymorphism to call the method.
# class Cat:
#     def speak(self):
#         return "Meow!"

# class Dog:
#     def speak(self):
#         return "Bark!"

# # Polymorphism example
# def animal_sound(animal):
#     return animal.speak()

# cat = Cat()
# dog = Dog()

# print(animal_sound(cat))  # Output: Meow!
# print(animal_sound(dog))  # Output: Bark!

# 5️. Create a Class Method and Static Method
# Problem: Create a Person class with a class method to count people and a static method to check if age is valid.
# class Person:
#     count = 0  # Class variable

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.count += 1  # Increment count when an object is created

#     @classmethod
#     def get_count(cls):
#         return f"Total People: {cls.count}"

#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# # Create objects
# p1 = Person("Alice", 25)
# p2 = Person("Bob", 17)

# print(Person.get_count())  # Output: Total People: 2
# print(Person.is_adult(20))  # Output: True
# print(Person.is_adult(15))  # Output: False

# 6️.Operator Overloading
# Problem: Overload the + operator to add two Rectangle objects based on area.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def __add__(self, other):
#         return self.area() + other.area()

# # Create objects
# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(3, 6)

# print(rect1 + rect2)  # Output: 38 (20 + 18)