"""
===========================================================
            CONTEXT MANAGER IN PYTHON
===========================================================

Definition
----------
A Context Manager is one of the most important Python concepts and is frequently asked in interviews. 
It is commonly used for resource management (files, database connections, network sockets, locks, etc.).

A Context Manager is an object that automatically manages
resources by performing setup before a block of code and
cleanup after the block finishes.

It ensures resources are released properly, even if an
exception occurs.

Most commonly used with the 'with' statement.

Syntax
------
with context_manager as variable:
    # code

Advantages
----------
1. Automatic resource management
2. No need to manually close resources
3. Prevents memory/resource leaks
4. Handles exceptions safely
5. Cleaner and more readable code

===========================================================
"""

print("=" * 60)
print("EXAMPLE 1 : WITHOUT CONTEXT MANAGER")
print("=" * 60)

"""
Opening a file manually.

Problem:
If an exception occurs before file.close(),
the file may remain open.
"""

file = open("sample.txt", "w")

file.write("Hello Python\n")

file.close()

print("File Closed Successfully")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 2 : USING CONTEXT MANAGER")
print("=" * 60)

"""
The 'with' statement automatically closes the file.
"""

with open("sample.txt", "a") as file:
    file.write("Learning Context Manager\n")
    print("Writing into file...")

print("File Closed Automatically")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 3 : READING FILE")
print("=" * 60)

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 4 : WHAT HAPPENS INTERNALLY?")
print("=" * 60)

"""
with open(...) as file

Internally behaves like:

manager = open(...)

manager.__enter__()

try:
    # your code

finally:
    manager.__exit__()

"""

print("Context Manager internally calls __enter__() and __exit__().")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 5 : CREATING OUR OWN CONTEXT MANAGER")
print("=" * 60)

class Demo:

    def __enter__(self):
        print("Entering Context")
        return self

    def display(self):
        print("Inside Context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving Context")


with Demo() as obj:
    obj.display()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 6 : EXCEPTION HANDLING")
print("=" * 60)

class Test:

    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleanup Executed")

        print("Exception Type :", exc_type)
        print("Exception Value:", exc_value)

        # Returning False means exception will continue propagating.
        return False

try:
    with Test():
        print(10 / 0)

except ZeroDivisionError:
    print("ZeroDivisionError handled outside")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 7 : USING contextlib.contextmanager")
print("=" * 60)

from contextlib import contextmanager

@contextmanager
def message():

    print("Before Yield")

    yield

    print("After Yield")


with message():
    print("Inside with block")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 8 : DATABASE CONNECTION (SIMULATION)")
print("=" * 60)

class Database:

    def __enter__(self):
        print("Database Connected")
        return self

    def execute(self):
        print("Executing Query")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Database Connection Closed")


with Database() as db:
    db.execute()

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 9 : LOCK MANAGEMENT (SIMULATION)")
print("=" * 60)

class Lock:

    def __enter__(self):
        print("Lock Acquired")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Lock Released")


with Lock():
    print("Critical Section")

print()

# ------------------------------------------------------------

print("=" * 60)
print("INTERVIEW NOTES")
print("=" * 60)

print("""
What is Context Manager?
------------------------
An object that automatically manages resources using
the with statement.

Which methods are required?
---------------------------
1. __enter__()
2. __exit__()

What does __enter__() do?
-------------------------
Runs before entering the with block.
Returns the object assigned after 'as'.

What does __exit__() do?
------------------------
Runs after leaving the with block.
Performs cleanup.
Receives exception information if one occurred.

What does the 'with' statement do?
----------------------------------
1. Calls __enter__()
2. Executes the block
3. Calls __exit__()
4. Cleans up resources automatically

Can we create our own Context Manager?
--------------------------------------
Yes.
Either:
1. Implement __enter__() and __exit__()
OR
2. Use @contextmanager from contextlib

Common Uses
-----------
- File handling
- Database connections
- Network sockets
- Thread locks
- Temporary resources
- Transactions

Advantages
----------
- Cleaner code
- Automatic cleanup
- Better exception handling
- Prevents resource leaks
""")

print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)