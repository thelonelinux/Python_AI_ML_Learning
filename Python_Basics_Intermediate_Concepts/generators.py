"""
====================================================================
                    GENERATORS IN PYTHON
====================================================================

Definition
----------
A Generator is a special type of function that returns
values one at a time using the 'yield' keyword instead of
return.

Unlike a normal function, a generator does NOT execute
completely in one call.

It pauses its execution at each 'yield' statement and
resumes from the same point when next() is called again.

Advantages
----------
1. Memory Efficient
2. Lazy Evaluation (Generate values only when needed)
3. Faster for large datasets
4. Used in File Processing
5. Used in Data Streaming
6. Used in Pipelines

====================================================================
"""

print("=" * 70)
print("1. NORMAL FUNCTION")
print("=" * 70)

"""
A normal function executes completely and returns only once.
After 'return' is executed, the function ends.
"""


def normal_function():
    return 10


print(normal_function())

print()

# -------------------------------------------------------------------

print("=" * 70)
print("2. SIMPLE GENERATOR")
print("=" * 70)

"""
A generator uses 'yield' instead of 'return'.

Every time next() is called,
execution resumes from the previous yield.
"""


def numbers():
    yield 1
    yield 2
    yield 3


g = numbers()

print(next(g))
print(next(g))
print(next(g))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("3. GENERATOR EXECUTION FLOW")
print("=" * 70)

"""
Execution Flow

yield 10
   ↓ pause

yield 20
   ↓ pause

yield 30
   ↓ pause

Function Ends
"""


def demo():
    print("Started")

    yield 10

    print("Resumed")

    yield 20

    print("Resumed Again")

    yield 30

    print("Generator Finished")


obj = demo()

print(next(obj))
print(next(obj))
print(next(obj))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("4. USING FOR LOOP")
print("=" * 70)

"""
Instead of repeatedly calling next(),
a for-loop automatically calls next()
until StopIteration occurs.
"""


def fruits():

    yield "Apple"

    yield "Banana"

    yield "Mango"


for fruit in fruits():
    print(fruit)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("5. GENERATOR WITH LOOP")
print("=" * 70)

"""
Generators are commonly used with loops.
"""


def count(n):

    for i in range(1, n + 1):
        yield i


for value in count(5):
    print(value)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("6. FIBONACCI GENERATOR")
print("=" * 70)

"""
Produces Fibonacci numbers one by one.
"""


def fibonacci(limit):

    a = 0
    b = 1

    for _ in range(limit):

        yield a

        a, b = b, a + b


for number in fibonacci(10):
    print(number)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("7. GENERATOR EXPRESSION")
print("=" * 70)

"""
Generator Expression

Looks similar to List Comprehension
but uses () instead of [].
"""

square = (x * x for x in range(5))

for value in square:
    print(value)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("8. LIST vs GENERATOR")
print("=" * 70)

"""
List creates ALL values immediately.

Generator creates values ONLY when needed.
"""

numbers_list = [x for x in range(5)]

numbers_generator = (x for x in range(5))

print("List :", numbers_list)

print("Generator :", numbers_generator)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("9. MEMORY COMPARISON")
print("=" * 70)

"""
Generators consume much less memory because
they don't store all values.
"""

import sys

list_data = [x for x in range(10000)]

generator_data = (x for x in range(10000))

print("List Size :", sys.getsizeof(list_data))

print("Generator Size :", sys.getsizeof(generator_data))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("10. INFINITE GENERATOR")
print("=" * 70)

"""
Infinite generators never stop on their own.

Always use a break condition.
"""


def infinite():

    number = 1

    while True:

        yield number

        number += 1


g = infinite()

for value in g:

    print(value)

    if value == 5:
        break

print()

# -------------------------------------------------------------------

print("=" * 70)
print("11. FILE READING USING GENERATOR")
print("=" * 70)

"""
Generators are excellent for reading
large files line by line.
"""

with open("sample.txt", "w") as file:

    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")


def read_file(filename):

    with open(filename, "r") as file:

        for line in file:

            yield line.strip()


for line in read_file("sample.txt"):
    print(line)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("12. STOPITERATION")
print("=" * 70)

"""
After all yields are exhausted,
calling next() raises StopIteration.
"""


def demo():

    yield 100

    yield 200


obj = demo()

print(next(obj))

print(next(obj))

try:

    print(next(obj))

except StopIteration:

    print("Generator Finished")

print()

# -------------------------------------------------------------------

print("=" * 70)
print("13. RETURN IN GENERATOR")
print("=" * 70)

"""
return immediately ends the generator.
"""


def example():

    yield 1

    yield 2

    return

    yield 3


for value in example():
    print(value)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("14. REAL-WORLD EXAMPLE")
print("=" * 70)

"""
Imagine millions of customer records.

Instead of loading all records into memory,
a generator produces one customer at a time.
"""


def customers():

    for i in range(1, 6):

        yield f"Customer {i}"


for customer in customers():
    print(customer)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("15. GENERATOR OBJECT")
print("=" * 70)

"""
Calling a generator function does NOT execute it.

It returns a Generator Object.
"""


def hello():

    yield "Hello"


obj = hello()

print(type(obj))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

print("""
Q1. What is Generator?

A Generator is a special function that uses
yield to produce values one at a time.

--------------------------------------------------

Q2. Difference between return and yield?

return
-------
Ends function permanently.

yield
------
Pauses function and remembers state.

--------------------------------------------------

Q3. Why use Generators?

- Less Memory
- Lazy Evaluation
- Large Data Processing
- Faster Execution
- Streaming Data

--------------------------------------------------

Q4. What is Generator Expression?

Uses ()

Example:

(x*x for x in range(5))

--------------------------------------------------

Q5. What happens after all yields finish?

StopIteration exception is raised.

--------------------------------------------------

Q6. Can a generator be reused?

No.

Once exhausted,
a generator cannot be restarted.
Create a new generator object.

--------------------------------------------------

Q7. Difference between List and Generator?

List
----
Stores all values.

Generator
----------
Produces values on demand.

--------------------------------------------------

Q8. Which keyword creates Generator?

yield
""")

print("=" * 70)
print("END OF PROGRAM")
print("=" * 70)