"""
=========================================================
            PYTHON CLOSURES - COMPLETE NOTES
=========================================================

Definition:
-----------
A closure is a function that remembers the variables from
its enclosing (outer) function even after the outer
function has finished executing.

Formula:
--------
Closure = Inner Function + Remembered Outer Variables

Why use Closures?
-----------------
1. Preserve state without global variables.
2. Data hiding (Encapsulation).
3. Create configurable functions.
4. Used in Decorators.
5. Used in Callbacks and Event Handling.

Requirements for a Closure:
---------------------------
1. There must be an outer function.
2. There must be an inner function.
3. The inner function must use a variable from the outer function.
4. The outer function must return the inner function.

=========================================================
"""

print("=" * 60)
print("EXAMPLE 1 : Basic Closure")
print("=" * 60)


def outer():
    message = "Hello from Closure"

    def inner():
        print(message)

    return inner


func = outer()
func()

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 2 : Greeting Example")
print("=" * 60)


def greeting(name):
    def say_hello():
        print(f"Hello {name}")

    return say_hello


greet = greeting("Vicky")
greet()

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 3 : Counter using Closure")
print("=" * 60)


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c())
print(c())
print(c())

print("\n")

"""
Explanation:
------------
Without 'nonlocal', Python creates a new local variable
named count, causing an UnboundLocalError.

nonlocal tells Python to use the variable from the
enclosing function.
"""

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 4 : Multiplier Factory")
print("=" * 60)


def multiplier(n):
    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)
triple = multiplier(3)

print("Double of 10 =", double(10))
print("Triple of 10 =", triple(10))

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 5 : Logger Example")
print("=" * 60)


def logger(level):
    def log(message):
        print(f"[{level}] {message}")

    return log


info = logger("INFO")
error = logger("ERROR")

info("Application Started")
error("Database Connection Failed")

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 6 : Inspecting Closure")
print("=" * 60)


def outer_function():
    x = 100

    def inner_function():
        print(x)

    return inner_function


closure_function = outer_function()

print("Closure Object :", closure_function.__closure__)
print("Captured Value :", closure_function.__closure__[0].cell_contents)

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 7 : Closure vs Normal Function")
print("=" * 60)


def add(x, y):
    return x + y


print("Normal Function :", add(10, 20))


def add_closure(x):
    def inner(y):
        return x + y

    return inner


plus_five = add_closure(5)

print("Closure Function :", plus_five(10))

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 8 : Multiple Closures")
print("=" * 60)


def power(exponent):
    def calculate(number):
        return number ** exponent

    return calculate


square = power(2)
cube = power(3)

print("Square of 5 :", square(5))
print("Cube of 5   :", cube(5))

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 9 : Closure Maintains State")
print("=" * 60)


def bank_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        print("Current Balance =", balance)

    return deposit


account = bank_account(1000)

account(500)
account(200)
account(300)

print("\n")

# -------------------------------------------------------------

print("=" * 60)
print("INTERVIEW QUESTIONS")
print("=" * 60)

"""
Q1. What is Closure?
A. A closure is a function object that remembers variables
   from its enclosing scope even after the outer function
   has finished execution.

Q2. Why use Closures?
A.
- Maintain State
- Data Hiding
- Decorators
- Function Factory
- Callbacks

Q3. What keyword is used to modify outer variables?
A. nonlocal

Q4. Difference between Global and Nonlocal?

global
------
Accesses global variables.

nonlocal
---------
Accesses variables from the enclosing function.

Q5. What are the requirements of a Closure?

1. Outer function
2. Inner function
3. Inner function uses outer variable
4. Outer returns inner function
"""
