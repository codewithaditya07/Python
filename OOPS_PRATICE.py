# 1. Classes & Objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
car1 = Car("Toyota", "Camry")
car1.display()


# 2. Encapsulation (Public & Private Attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # This will cause an error (private attribute)

# 3. Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())  # Output: Bark

# 4. Polymorphism (Method Overriding & Overloading)
# Method Overriding

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.5

# Method Overloading (Using Default Arguments)
class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(2, 3))     # Output: 5
print(m.add(2, 3, 4))  # Output: 9

# 5. Abstraction (Using ABC Module)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

car = Car()
car.start()

# 6. Special Methods (__init__, __str__, etc.)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

p1 = Person("Alice", 25)
print(p1)  # Output: Person(Name: Alice, Age: 25)

# 7. Static & Class Methods
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def info(cls):
        return "This is a MathOperations class"

print(MathOperations.add(3, 4))  # Output: 7
print(MathOperations.info())     # Output: This is a MathOperations class


# bank
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self,ammout):
        self.balance  -= ammout
        print("Rs:(-)",ammout ,"is debited")
        print("total balance =",self.get_balance())


    def credit(self,ammout):
        self.balance += ammout
        print("Rs:(+)",ammout ,"is credited")
        print("total balance =",self.get_balance())

    def get_balance(self):
          return self.balance 
    
account1 = Account(8000,5050555)
print("Account balance =", account1.get_balance())
account1.debit(600)
account1.credit(2600)
account1.credit(6000)