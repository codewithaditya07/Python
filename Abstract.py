# Q WAP abstract method for handling different types of vehicles. 
# We'll demonstrate the abstraction of methods for starting the engine and stopping the engine.

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    # Abstract method 
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return f"{self.brand} car engine started."

    def stop_engine(self):
        return f"{self.brand} car engine stopped."

class Motorcycle(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        return f"{self.brand} motorcycle engine started."

    def stop_engine(self):
        return f"{self.brand} motorcycle engine stopped."

car = Car("Toyota")
print(car.start_engine()) 
print(car.stop_engine()) 

motorcycle = Motorcycle("Yamaha")
print(motorcycle.start_engine()) 
print(motorcycle.stop_engine()) 


from abc import ABC, abstractmethod

# Define an abstract class
class Animal(ABC):
    
    # Abstract method
    @abstractmethod
    def sound(self):
        pass
    
    # Regular method
    def move(self):
        print("The animal is moving")

class Dog(Animal):
    
    def sound(self):
        print("Woof!")

class Cat(Animal):

    def sound(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.sound()  

