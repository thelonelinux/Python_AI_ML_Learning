"""
====================================================================
                    LAMBDA FUNCTIONS IN PYTHON
====================================================================

Definition
----------
A Lambda Function is a small anonymous (nameless) function
created using the 'lambda' keyword.

Unlike normal functions, lambda functions:

1. Have no function name.
2. Can have any number of arguments.
3. Can have only ONE expression.
4. Automatically return the result.

Syntax
------

lambda arguments : expression

Example:

lambda x : x * x

Equivalent Normal Function:

def square(x):
    return x * x

Advantages
----------
1. Short and concise code.
2. Useful for one-time operations.
3. Commonly used with map(), filter(), sorted(), reduce().
4. Improves code readability for simple operations.

====================================================================
"""

print("=" * 70)
print("1. NORMAL FUNCTION")
print("=" * 70)

"""
Normal function using def.
"""


def square(number):
    return number * number


print(square(5))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("2. SIMPLE LAMBDA FUNCTION")
print("=" * 70)

"""
The same square function using lambda.

lambda x : x * x

x -> Parameter
x*x -> Expression (Automatically Returned)
"""

square = lambda x: x * x

print(square(5))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("3. LAMBDA WITH MULTIPLE ARGUMENTS")
print("=" * 70)

"""
Lambda functions can accept multiple arguments.
"""

add = lambda a, b: a + b

multiply = lambda a, b: a * b

print("Addition :", add(10, 20))
print("Multiplication :", multiply(10, 20))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("4. LAMBDA WITH CONDITIONAL EXPRESSION")
print("=" * 70)

"""
Lambda supports conditional expressions.

Syntax

lambda x :
    value_if_true if condition else value_if_false
"""

maximum = lambda a, b: a if a > b else b

print(maximum(10, 50))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("5. USING LAMBDA WITH map()")
print("=" * 70)

"""
map(function, iterable)

Applies a function to every element.
"""

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("6. USING LAMBDA WITH filter()")
print("=" * 70)

"""
filter(function, iterable)

Keeps only elements for which
the function returns True.
"""

numbers = [10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("7. USING LAMBDA WITH sorted()")
print("=" * 70)

"""
sorted()

Sort objects using a custom key.
"""

students = [

    ("Vicky", 80),

    ("Rahul", 95),

    ("Amit", 75)

]

sorted_students = sorted(

    students,

    key=lambda student: student[1]

)

print(sorted_students)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("8. USING LAMBDA WITH max()")
print("=" * 70)

employees = [

    {"name": "A", "salary": 40000},

    {"name": "B", "salary": 80000},

    {"name": "C", "salary": 60000}

]

highest = max(

    employees,

    key=lambda employee: employee["salary"]

)

print(highest)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("9. USING LAMBDA WITH min()")
print("=" * 70)

lowest = min(

    employees,

    key=lambda employee: employee["salary"]

)

print(lowest)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("10. USING LAMBDA WITH reduce()")
print("=" * 70)

"""
reduce()

Applies the function repeatedly
to reduce a sequence into one value.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(

    lambda x, y: x + y,

    numbers

)

print(total)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("11. SORTING BY STRING LENGTH")
print("=" * 70)

words = [

    "Python",

    "Java",

    "C",

    "JavaScript"

]

result = sorted(

    words,

    key=lambda word: len(word)

)

print(result)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("12. LAMBDA INSIDE ANOTHER FUNCTION")
print("=" * 70)

"""
Lambda can be returned from functions.
"""


def multiplier(number):

    return lambda x: x * number


double = multiplier(2)

triple = multiplier(3)

print(double(10))

print(triple(10))

print()

# -------------------------------------------------------------------

print("=" * 70)
print("13. IMMEDIATELY INVOKED LAMBDA")
print("=" * 70)

"""
Lambda can be called immediately.
"""

print(

    (lambda x, y: x + y)(100, 200)

)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("14. LIST COMPREHENSION vs map()")
print("=" * 70)

numbers = [1, 2, 3, 4]

square1 = list(map(lambda x: x * x, numbers))

square2 = [x * x for x in numbers]

print(square1)

print(square2)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("15. LIMITATIONS OF LAMBDA")
print("=" * 70)

print("""

Lambda Function Limitations

1. Only one expression

Correct

lambda x: x*x

Wrong

lambda x:
    print(x)
    return x*x

Use normal function instead.

2. No multiple statements

3. Less readable for complex logic

4. Cannot contain loops directly

""")

print()

# -------------------------------------------------------------------

print("=" * 70)
print("16. NORMAL FUNCTION vs LAMBDA")
print("=" * 70)

print("""

Normal Function

def add(a,b):
    return a+b

Lambda

lambda a,b:a+b

Use Lambda

✓ Small logic
✓ One-time use
✓ map()
✓ filter()
✓ sorted()
✓ reduce()

Use Normal Function

✓ Large logic
✓ Multiple statements
✓ Better readability
✓ Reusable functions

""")

print()

# -------------------------------------------------------------------

print("=" * 70)
print("17. REAL WORLD EXAMPLE")
print("=" * 70)

"""
Sort employees by age.
"""

employees = [

    {"name": "Vicky", "age": 27},

    {"name": "Rahul", "age": 24},

    {"name": "Amit", "age": 30}

]

employees = sorted(

    employees,

    key=lambda emp: emp["age"]

)

for employee in employees:

    print(employee)

print()

# -------------------------------------------------------------------

print("=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

print("""

Q1. What is Lambda Function?

A Lambda Function is an anonymous function
created using the lambda keyword.

--------------------------------------------------

Q2. Why is it called Anonymous?

Because it has no function name.

--------------------------------------------------

Q3. Syntax?

lambda arguments : expression

--------------------------------------------------

Q4. Can Lambda contain multiple statements?

No.

Only one expression.

--------------------------------------------------

Q5. Does Lambda use return?

No.

The expression result is automatically returned.

--------------------------------------------------

Q6. Where is Lambda commonly used?

map()

filter()

sorted()

reduce()

max()

min()

--------------------------------------------------

Q7. Difference between Lambda and Normal Function?

Lambda
-------
Anonymous
One expression
Short

Normal Function
---------------
Named
Multiple statements
Reusable

--------------------------------------------------

Q8. Can Lambda take multiple arguments?

Yes.

Example

lambda a,b,c:a+b+c

--------------------------------------------------

Q9. Can Lambda replace every function?

No.

It should only be used for simple expressions.

--------------------------------------------------

Q10. Which keyword creates Lambda Function?

lambda

""")

print("=" * 70)
print("END OF PROGRAM")
print("=" * 70)