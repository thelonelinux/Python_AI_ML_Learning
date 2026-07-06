"""
============================================================
            ERROR HANDLING IN PYTHON
============================================================

Definition
----------
Error Handling is the process of detecting and handling
runtime errors so that the program continues to execute
gracefully instead of terminating unexpectedly.

Python uses:
try
except
else
finally
raise

Advantages
----------
1. Prevents program crashes.
2. Improves user experience.
3. Makes applications robust.
4. Helps in debugging.
5. Ensures proper resource cleanup.

============================================================
"""

print("=" * 60)
print("EXAMPLE 1 : PROGRAM WITHOUT ERROR HANDLING")
print("=" * 60)

print("Program Started")

# Uncomment the next line to see the crash.
# print(10 / 0)

print("Program Finished")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 2 : BASIC try-except")
print("=" * 60)

try:
    number = 10 / 0
    print(number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Program Continues")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 3 : HANDLING MULTIPLE EXCEPTIONS")
print("=" * 60)

try:
    numbers = [10, 20, 30]

    print(numbers[5])

except ZeroDivisionError:
    print("Division by zero occurred.")

except IndexError:
    print("Index is out of range.")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 4 : MULTIPLE EXCEPTIONS IN ONE BLOCK")
print("=" * 60)

try:
    value = int("ABC")

except (ValueError, TypeError):
    print("Invalid value or type.")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 5 : USING else")
print("=" * 60)

try:
    result = 100 / 10

except ZeroDivisionError:
    print("Cannot divide.")

else:
    print("Division Successful")
    print("Result =", result)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 6 : USING finally")
print("=" * 60)

try:
    file = open("sample.txt", "w")
    file.write("Python Error Handling")

except Exception as error:
    print(error)

finally:
    file.close()
    print("File Closed Successfully")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 7 : COMPLETE try-except-else-finally")
print("=" * 60)

try:
    number = int(input("Enter a Number: "))
    answer = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Answer =", answer)

finally:
    print("Execution Completed.")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 8 : CAPTURING EXCEPTION OBJECT")
print("=" * 60)

try:
    value = int("Python")

except ValueError as error:
    print("Error Message :", error)
    print("Exception Type :", type(error))

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 9 : GENERIC EXCEPTION")
print("=" * 60)

try:
    data = {"name": "Vicky"}

    print(data["age"])

except Exception as error:
    print("Exception Caught :", error)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 10 : RAISING AN EXCEPTION")
print("=" * 60)

def check_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible")


try:
    check_age(15)

except ValueError as error:
    print(error)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 11 : CUSTOM EXCEPTION")
print("=" * 60)

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance")

    print("Withdrawal Successful")


try:
    withdraw(5000, 7000)

except InsufficientBalanceError as error:
    print(error)

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 12 : NESTED try-except")
print("=" * 60)

try:

    try:
        print(100 / 0)

    except ZeroDivisionError:
        print("Inner Exception Handled")

except Exception:
    print("Outer Exception Handled")

print()

# ------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 13 : ASSERT")
print("=" * 60)

def divide(a, b):

    assert b != 0, "Denominator cannot be zero."

    return a / b


try:
    print(divide(10, 2))

    # Uncomment to test assertion.
    # print(divide(10, 0))

except AssertionError as error:
    print(error)

print()

# ------------------------------------------------------------

print("=" * 60)
print("COMMON BUILT-IN EXCEPTIONS")
print("=" * 60)

print("""
ZeroDivisionError
ValueError
TypeError
IndexError
KeyError
FileNotFoundError
ImportError
AttributeError
NameError
AssertionError
RuntimeError
""")

print()

# ------------------------------------------------------------

print("=" * 60)
print("FLOW OF ERROR HANDLING")
print("=" * 60)

print("""
try
 │
 │
 ├── No Exception?
 │       │
 │       ▼
 │      else
 │
 └── Exception?
         │
         ▼
      except
         │
         ▼
      finally
""")

print()

# ------------------------------------------------------------

print("=" * 60)
print("INTERVIEW QUESTIONS")
print("=" * 60)

print("""
Q1. What is Exception?
A.
An exception is a runtime error that interrupts the normal
flow of program execution.

Q2. Difference between Syntax Error and Exception?

Syntax Error
------------
Occurs before execution.

Exception
----------
Occurs during execution.

Q3. Purpose of try block?
A.
Contains code that may generate an exception.

Q4. Purpose of except block?
A.
Handles the exception.

Q5. Purpose of else block?
A.
Executes only when no exception occurs.

Q6. Purpose of finally block?
A.
Always executes whether an exception occurs or not.
Used for cleanup activities.

Q7. What does raise do?
A.
Creates and throws an exception explicitly.

Q8. Why create custom exceptions?
A.
To represent application-specific errors clearly.

Q9. Difference between Exception and BaseException?

BaseException
-------------
Root class of all exceptions.

Exception
---------
Most user-defined and application exceptions inherit from it.

Q10. What is AssertionError?
A.
Raised when an assert statement fails.
""")

print("=" * 60)
print("END OF PROGRAM")
print("=" * 60)