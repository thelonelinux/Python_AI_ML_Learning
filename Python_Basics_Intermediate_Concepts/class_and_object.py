"""
============================================================
         OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
============================================================

What is OOP?
------------
Object-Oriented Programming (OOP) is a programming paradigm
that organizes code using Objects and Classes.

Instead of writing only functions, we create objects that
contain both data (attributes) and behavior (methods).

Real-Life Example
-----------------
Class  -> Car Blueprint
Object -> Honda City
Object -> BMW X5
Object -> Audi A6

One class can create multiple objects.

============================================================
"""

print("="*60)
print("1. CLASS")
print("="*60)

"""
Class
-----
A class is a blueprint or template used to create objects.

It defines:
1. Attributes (variables)
2. Methods (functions)
"""

class Student:

    college = "ABC College"      # Class Variable

    def study(self):
        print("Student is studying")


print("Class Created Successfully\n")

# ------------------------------------------------------------

print("="*60)
print("2. OBJECT")
print("="*60)

"""
Object
------
An object is an instance of a class.

Syntax:
object = ClassName()
"""

student1 = Student()
student2 = Student()

print(student1)
print(student2)

student1.study()
student2.study()

print()

# ------------------------------------------------------------

print("="*60)
print("3. CONSTRUCTOR (__init__)")
print("="*60)

"""
Constructor
-----------
A constructor initializes object data automatically
when an object is created.

Syntax:
def __init__(self):
"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)


emp1 = Employee("Vicky", 70000)
emp2 = Employee("Rahul", 85000)

emp1.display()
print()
emp2.display()

print()

# ------------------------------------------------------------

print("="*60)
print("4. INSTANCE VARIABLES")
print("="*60)

"""
Instance Variable
-----------------
Belongs to each object.

Different objects can have different values.
"""

class Car:

    def __init__(self, company, model):
        self.company = company
        self.model = model


car1 = Car("Honda", "City")
car2 = Car("BMW", "X5")

print(car1.company, car1.model)
print(car2.company, car2.model)

print()

# ------------------------------------------------------------

print("="*60)
print("5. CLASS VARIABLE")
print("="*60)

"""
Class Variable
--------------
Shared among all objects.
"""

class Mobile:

    company = "Samsung"

    def __init__(self, model):
        self.model = model


m1 = Mobile("S24")
m2 = Mobile("S25")

print(m1.company)
print(m2.company)

print()

# ------------------------------------------------------------

print("="*60)
print("6. METHODS")
print("="*60)

"""
Types of Methods

1. Instance Method
2. Class Method
3. Static Method
"""

class Calculator:

    company = "OpenAI"

    def __init__(self, number):
        self.number = number

    # Instance Method
    def square(self):
        return self.number ** 2

    # Class Method
    @classmethod
    def get_company(cls):
        return cls.company

    # Static Method
    @staticmethod
    def add(x, y):
        return x + y


obj = Calculator(10)

print(obj.square())
print(Calculator.get_company())
print(Calculator.add(20, 30))

print()

# ------------------------------------------------------------

print("="*60)
print("7. ENCAPSULATION")
print("="*60)

"""
Encapsulation
-------------
Wrapping data and methods together inside a class.

Private members use __ (double underscore).
"""

class Bank:

    def __init__(self):
        self.__balance = 10000

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance =", self.__balance)


account = Bank()

account.deposit(5000)
account.show_balance()

print()

# ------------------------------------------------------------

print("="*60)
print("8. INHERITANCE")
print("="*60)

"""
Inheritance
-----------
Child class acquires properties of Parent class.
"""

class Animal:

    def speak(self):
        print("Animal Speaks")


class Dog(Animal):

    def bark(self):
        print("Dog Barks")


dog = Dog()

dog.speak()
dog.bark()

print()

# ------------------------------------------------------------

print("="*60)
print("9. POLYMORPHISM")
print("="*60)

"""
Polymorphism
------------
Same method behaves differently.
"""

class Bird:

    def sound(self):
        print("Bird Sound")


class Sparrow(Bird):

    def sound(self):
        print("Chirp Chirp")


class Crow(Bird):

    def sound(self):
        print("Caw Caw")


birds = [Sparrow(), Crow()]

for bird in birds:
    bird.sound()

print()

# ------------------------------------------------------------

print("="*60)
print("10. ABSTRACTION")
print("="*60)

"""
Abstraction
-----------
Hide implementation and expose only functionality.

Implemented using ABC module.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


bike = Bike()
bike.start()

print()

# ------------------------------------------------------------

print("="*60)
print("11. SELF KEYWORD")
print("="*60)

"""
self
----
Represents the current object.

Python automatically passes self when an object
calls a method.
"""

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Hello", self.name)


p = Person("Vicky")
p.display()

print()
