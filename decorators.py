"""
============================================================
                DECORATORS IN PYTHON
============================================================

Definition
----------
A Decorator is a function that takes another function as
input, adds extra functionality, and returns a new function
without modifying the original function.

Decorators are one of the most powerful Python features and are asked frequently in interviews.
 They are built on top of functions as first-class objects, closures, and higher-order functions.
 Since you've already studied closures, decorators will be much easier to understand.

Formula
-------
Decorator = Function + Closure + Wrapper Function

Why Use Decorators?
-------------------
1. Add functionality without changing original code.
2. Reuse common logic.
3. Logging
4. Authentication
5. Performance Measurement
6. Exception Handling

============================================================
"""

print("=" * 60)
print("EXAMPLE 1 : FUNCTIONS ARE FIRST-CLASS OBJECTS")
print("=" * 60)

"""
Functions in Python are objects.

They can be:
- Assigned to variables
- Passed as arguments
- Returned from other functions
"""


def greet():
    print("Hello Python")


say_hello = greet

say_hello()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 2 : FUNCTION AS ARGUMENT")
print("=" * 60)


def display(function):
    print("Before Calling Function")
    function()
    print("After Calling Function")


def message():
    print("Inside Message Function")


display(message)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 3 : FUNCTION RETURNING FUNCTION")
print("=" * 60)


def outer():

    def inner():
        print("Hello from Inner Function")

    return inner


obj = outer()
obj()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 4 : SIMPLE DECORATOR")
print("=" * 60)


def decorator(function):

    def wrapper():
        print("Before Function")

        function()

        print("After Function")

    return wrapper


def hello():
    print("Hello World")


decorated_function = decorator(hello)

decorated_function()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 5 : USING @ DECORATOR")
print("=" * 60)


def decorator(function):

    def wrapper():
        print("Decorator Started")

        function()

        print("Decorator Finished")

    return wrapper


@decorator
def welcome():
    print("Welcome to Python")


welcome()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 6 : DECORATOR WITH ARGUMENTS")
print("=" * 60)


def decorator(function):

    def wrapper(name):
        print("Before Execution")

        function(name)

        print("After Execution")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Vicky")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 7 : DECORATOR USING *args AND **kwargs")
print("=" * 60)


def decorator(function):

    def wrapper(*args, **kwargs):
        print("Before Function")

        result = function(*args, **kwargs)

        print("After Function")

        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print("Result =", add(10, 20))

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 8 : LOGGING DECORATOR")
print("=" * 60)


def logger(function):

    def wrapper(*args, **kwargs):
        print(f"Calling Function : {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished Function : {function.__name__}")

        return result

    return wrapper


@logger
def multiply(a, b):
    return a * b


print(multiply(5, 6))

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 9 : EXECUTION TIME DECORATOR")
print("=" * 60)

import time


def calculate_time(function):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Execution Time =", end - start)

        return result

    return wrapper


@calculate_time
def loop():

    total = 0

    for i in range(1000000):
        total += i

    return total


print(loop())

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 10 : AUTHENTICATION DECORATOR")
print("=" * 60)


def login_required(function):

    def wrapper(is_logged_in):

        if is_logged_in:
            function(is_logged_in)
        else:
            print("Access Denied")

    return wrapper


@login_required
def dashboard(user):
    print("Dashboard Opened")


dashboard(True)
dashboard(False)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 11 : MULTIPLE DECORATORS")
print("=" * 60)


def decorator_one(function):

    def wrapper():
        print("Decorator One Start")

        function()

        print("Decorator One End")

    return wrapper


def decorator_two(function):

    def wrapper():
        print("Decorator Two Start")

        function()

        print("Decorator Two End")

    return wrapper


@decorator_one
@decorator_two
def demo():
    print("Inside Demo")


demo()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 12 : PRESERVING FUNCTION METADATA")
print("=" * 60)

from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Executing Function")
        return function(*args, **kwargs)

    return wrapper


@logger
def square(number):
    """Returns square of a number."""
    return number * number


print("Function Name :", square.__name__)
print("Docstring :", square.__doc__)
print("Square =", square(5))

print()

# ------------------------------------------------------------

print("=" * 60)
print("HOW @DECORATOR WORKS")
print("=" * 60)

print("""
When Python sees:

@decorator
def hello():
    pass

It automatically converts it to:

def hello():
    pass

hello = decorator(hello)
""")

print()

# ------------------------------------------------------------

print("=" * 60)
print("INTERVIEW QUESTIONS")
print("=" * 60)

print("""
Q1. What is a Decorator?
A.
A decorator is a function that adds extra functionality
to another function without modifying its source code.

Q2. Why use Decorators?
- Logging
- Authentication
- Timing
- Validation
- Caching
- Exception Handling

Q3. What does @ mean?
A.
It is syntactic sugar for:

function = decorator(function)

Q4. What is a Wrapper Function?
A.
The inner function that executes before/after the original
function.

Q5. Why use *args and **kwargs?
A.
To make decorators work with functions having any number
of positional and keyword arguments.

Q6. Why use functools.wraps?
A.
To preserve the original function's metadata like:
- __name__
- __doc__
- __module__

Q7. Can multiple decorators be applied?
A.
Yes.

@A
@B
def test():

Equivalent to:

test = A(B(test))

Execution order:
A -> B -> Function -> B -> A
""")

print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)