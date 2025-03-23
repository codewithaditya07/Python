# 1. Encapsulation (Data Hiding using Private Variables)
# Q: What is encapsulation in Python? Implement a BankAccount class with a private balance attribute.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):  
        return self.__balance

# Creating an object
account = BankAccount("12345", 5000)
account.deposit(1000)
account.withdraw(2000)
print(account.get_balance())  # Output: 4000

# 2. Inheritance (Reusing Parent Class Methods in Child Class)
# Q: Explain inheritance in Python with an example of a parent class Animal and a child class Dog.
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animals make different sounds.")

# Child Class (inherits from Animal)
class Dog(Animal):
    def sound(self):  # Overriding method
        print(f"{self.name} barks!")

dog = Dog("Buddy")
dog.sound()  # Output: Buddy barks!

# 3. Polymorphism (Method Overriding & Function Using Different Objects)
# Q: What is polymorphism in Python? Implement a Bird class and a Penguin class where Penguin overrides the fly method.
class Bird:
    def fly(self):
        print("Birds can fly.")

class Penguin(Bird):
    def fly(self):  # Overriding method
        print("Penguins cannot fly.")

# Function demonstrating polymorphism
def show_flying_ability(bird):
    bird.fly()

sparrow = Bird()
penguin = Penguin()

show_flying_ability(sparrow)  # Output: Birds can fly.
show_flying_ability(penguin)  # Output: Penguins cannot fly.

# 4. Abstraction (Hiding Implementation Details using Abstract Class)
# Q: What is abstraction in Python? Implement an abstract class Shape with an area method and a Circle class that extends it.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Implementing abstract method
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Area of Circle:", circle.area())  # Output: 78.5

# 5. Method Overriding (Child Class Changing Parent Class Behavior)
# Q: Explain method overriding in Python with an example of a parent class Vehicle and a child class Car.

class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):  # Overriding method
        print("Car is starting...")

# Creating objects
v = Vehicle()
c = Car()

v.start()  # Output: Vehicle is starting...
c.start()  # Output: Car is starting...

# 6. Multiple Inheritance (One Child Class from Multiple Parent Classes)
# Q: What is multiple inheritance in Python? Implement a class C that inherits from both A and B.
class A:
    def method_A(self):
        print("Method A")

class B:
    def method_B(self):
        print("Method B")

class C(A, B):
    def method_C(self):
        print("Method C")

obj = C()
obj.method_A()  # Output: Method A
obj.method_B()  # Output: Method B
obj.method_C()  # Output: Method C

# 7. super() Function (Calling Parent Class Method in Child Class)
# Q: What is the purpose of the super() function in Python? Implement a Parent class with a method and call it inside a Child class using super().

class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        super().show()  # Calls Parent's show method
        print("This is the child class.")

obj = Child()
obj.show()
# Output:
# This is the parent class.
# This is the child class.

# 8. Static and Class Methods (@staticmethod & @classmethod)
# Q: What is the difference between @staticmethod, @classmethod, and instance methods? Provide examples.

class Example:
    class_var = "Class Variable"

    def instance_method(self):
        return "Instance method"

    @classmethod
    def class_method(cls):
        return cls.class_var

    @staticmethod
    def static_method():
        return "Static method"

obj = Example()
print(obj.instance_method())  # Output: Instance method
print(Example.class_method())  # Output: Class Variable
print(Example.static_method())  # Output: Static method

# 9. Method Resolution Order (MRO) in Multiple Inheritance
# Q: How does Python determine the order of method execution in multiple inheritance? Demonstrate using the mro() function.
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Displays the MRO order