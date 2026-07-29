# Inheritance

# Write a program to create a class Person with attributes name and age. Create an object of this class and print its attributes.
# class Person:
#     def __init__(self,a,b):
#         self.name = a
#         self.age = b
#     def per(self):
#         return (f"my name is {self.name} and i am {self.age}year old ")
    
# Person1 = Person("parth",20)
# print(Person1.per())


# Create a class Rectangle with attributes length and width. Add a method area to calculate and return the area of the rectangle.
# class Rectangle:
#     def __init__(self,length,width):
#        self.len = length
#        self.wid = width
#     def  rec(self):
#         print(f"Rectangle of {self.len*self.wid}")
# area = Rectangle(20,10)    
# print(area.rec())


# private attributes
# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age

#     def get_name(self):
#         return self.__name
    
# person =Person("adii",20)
# print(person.get_name())
# print(person.age)

# protected attributes
# class Parents:
#     def __init__(self):
#         self._protected_attribute = "hello i am protected"

# class Child(Parents):
#     def access_protected(self):
#         return self._protected_attribute

# obj = Child()
# print(obj.access_protected())
# print(obj._protected_attribute)


# create a class of bank account with private attritube to provide methods deposite and withdraw to modify the balance
    
# class bankacc:
#     def __init__(self,initial_balance):           #Constructor (__init__ method)
#         self.__balance = initial_balance

#     def deposite(self,amount):                    #Deposit Method (deposite method)
#         if amount > 0:
#             self.__balance += amount
#         else :
#             print("deposite amount must be positive")
        
#     def withdraw(self,amount):                     #Withdraw Method (withdraw method)
#         if amount<=self.__balance:
#             self.__balance -= amount
#         else:
#             print("insufficint balance")

#     def get_balance(self):                      # Get Balance Method (get_balance method)
#        return self.__balance

# account = bankacc(1000)
# account.deposite(500)
# account.withdraw(200)
# print("balance", account.get_balance())

# Design a class Employee with attributes name, age, and salary.
#  Add a class variable company that stores the company's name. 
# Write methods to display employee details and change the company name.

# class Employee:
#     company_name = "apex ltd pvt" 
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def display( self):
#        print (f"Employee name is {self.name} and age is {self.age} and  salary is {self.salary} company name is {Employee.company_name}")
    
#     @classmethod
#     def change_company(cls,new_company):
#         cls.company_name = new_company

# emp = Employee("adii",20,600000)
# emp1 = Employee("adit",22,800000)

# emp.display()
# emp1.display()

# Employee.change_company("apppex")
# emp.display()
# emp1.display()


# Write a class Library to store a collection of books. Include methods to add a book, lend a book, and display the available books.
# class library:
#     def __init__(self):
#         self.book = []
    
#     def add_book(self,book):
#         self.book.append(book)
#         print(f"{book} book is added in library")

#     def lend_book(self,book):
#      if book in self.book:
#         self.book.remove(book)
#         print(f"{book} has been out")

     
#     def dislpay_book(self):
#         if self.book:
#          print("available books")
#          for book in self.book:
#             print(f"{book}")            
#         else:
#            print("no books are available in library")

# library = library()
# library.add_book("eco book")
# library.add_book("math book")
# library.add_book("labs")
# library.dislpay_book()
# library.lend_book("math book")
# library.dislpay_book()

# Q
# class complex:
#     def __init__(self,real=0.0, imag=0.0):
#      self.real = real
#      self.imag = imag

#     def __add__(self,other):                       
#         new = complex()
#         new.real = self.real + other.real 
#         new.imag = self.imag + other.imag
#         return new

#     def sub(self,other):                              
#         new = complex()
#         new.real = self.real + other.real
#         new.imag = self.imag + other.imag
#         return new
 
#     def display(self):
#         print(self.real,self.imag)

# num1 = complex(2.0 , 4.0)
# num2 = complex(5.0 , 6.0)
# obj = num1 + num2
# obj.display()
# print(obj)

# Create a class Student with attributes name, roll_number, and marks (a dictionary of subject: marks).
#  Implement methods to calculate the total marks, average marks, and assign grades based on the average.

# class Student:
#     def __init__(self,name,roll_num,marks):
#         self.name = name
#         self.roll_num = roll_num
#         self.marks =marks
    
#     def cal_total(self):
#         return sum(self.marks.values())
    
#     def  cal_avg(self):
#         return self.cal_total()/ len (self.marks)
    
#     def grade (self):
#         avgrage = self.cal_avg()
#         if avgrage >= 90:
#             return "A"
#         elif avgrage >= 75:
#             return "B"
#         elif avgrage >= 50:
#             return "C"
#         else:
#             return "F"
        
#     def display (self):
#         print(f"name{self.name}, roll no is {self.roll_num}")
#         print(f"total marks {self.cal_total()}, average {self.cal_avg():.2f}")
#         print(f"grade {self.grade()}")

# marks = {"math":85,"science":90,"english" : 80}
# student = Student("madhav",200564,marks)
# student.display()
