"""
====================================================================
                    ITERATION IN PYTHON
====================================================================

Definition
----------
Iteration is the process of accessing one element at a time
from a collection such as a list, tuple, string, dictionary,
set, or any iterable object.

Python performs iteration using:

1. for loop
2. while loop
3. Iterator Protocol (__iter__ and __next__)

Examples of Iterables
---------------------
List
Tuple
String
Dictionary
Set
Generator
File Object

Advantages
----------
1. Process data one item at a time.
2. Memory efficient.
3. Simple and readable code.
4. Used in loops, generators, file handling, etc.

====================================================================
"""

print("=" * 70)
print("1. ITERATING OVER A LIST")
print("=" * 70)

"""
A list is an iterable.

The for loop automatically gets each element
one by one.
"""

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("2. ITERATING OVER A TUPLE")
print("=" * 70)

"""
Tuples are also iterable.
"""

languages = ("Python", "Java", "C++")

for language in languages:
    print(language)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("3. ITERATING OVER A STRING")
print("=" * 70)

"""
Strings are iterable.

Each iteration returns one character.
"""

name = "Python"

for character in name:
    print(character)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("4. ITERATING OVER A DICTIONARY")
print("=" * 70)

student = {
    "Name": "Vicky",
    "Age": 27,
    "Course": "Python"
}

print("Dictionary Keys")

for key in student:
    print(key)

print()

print("Dictionary Values")

for value in student.values():
    print(value)

print()

print("Dictionary Key-Value Pairs")

for key, value in student.items():
    print(key, ":", value)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("5. ITERATING OVER A SET")
print("=" * 70)

"""
Sets are iterable.

Order is not guaranteed.
"""

fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("6. ITERATING USING while LOOP")
print("=" * 70)

numbers = [100, 200, 300]

index = 0

while index < len(numbers):

    print(numbers[index])

    index += 1

print()

# ------------------------------------------------------------------

print("=" * 70)
print("7. WHAT IS AN ITERABLE?")
print("=" * 70)

"""
Iterable
--------
An object capable of returning an iterator.

Examples
--------
list
tuple
set
dictionary
string
generator
"""

numbers = [1, 2, 3]

print("Iterable Object :", numbers)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("8. CREATING AN ITERATOR")
print("=" * 70)

"""
iter() converts an iterable into an iterator.
"""

numbers = [10, 20, 30]

iterator = iter(numbers)

print(iterator)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("9. USING next()")
print("=" * 70)

"""
next() returns one value at a time.

Each call moves the iterator forward.
"""

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print()

# ------------------------------------------------------------------

print("=" * 70)
print("10. StopIteration EXCEPTION")
print("=" * 70)

"""
When no elements remain,
next() raises StopIteration.
"""

numbers = [1, 2]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))

except StopIteration:
    print("No more elements.")

print()

# ------------------------------------------------------------------

print("=" * 70)
print("11. HOW for LOOP WORKS INTERNALLY")
print("=" * 70)

"""
for number in numbers:

Internally behaves like:

iterator = iter(numbers)

while True:

    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break
"""

numbers = [5, 10, 15]

iterator = iter(numbers)

while True:

    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        break

print()

# ------------------------------------------------------------------

print("=" * 70)
print("12. CREATING A CUSTOM ITERATOR")
print("=" * 70)

"""
A custom iterator must implement

1. __iter__()
2. __next__()
"""

class Counter:

    def __init__(self, maximum):
        self.current = 1
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.maximum:

            value = self.current

            self.current += 1

            return value

        raise StopIteration


counter = Counter(5)

for number in counter:
    print(number)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("13. ITERATOR OBJECT")
print("=" * 70)

numbers = [11, 22, 33]

iterator = iter(numbers)

print(type(iterator))

print()

# ------------------------------------------------------------------

print("=" * 70)
print("14. ITERATING OVER FILE")
print("=" * 70)

"""
Files are iterable objects.

Each iteration returns one line.
"""

with open("sample.txt", "w") as file:

    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")

with open("sample.txt", "r") as file:

    for line in file:
        print(line.strip())

print()

# ------------------------------------------------------------------

print("=" * 70)
print("15. ITERATION USING enumerate()")
print("=" * 70)

"""
enumerate() gives

index + value
"""

subjects = ["Python", "Java", "SQL"]

for index, subject in enumerate(subjects):

    print(index, subject)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("16. ITERATION USING zip()")
print("=" * 70)

"""
zip() combines multiple iterables.
"""

names = ["A", "B", "C"]

marks = [80, 90, 95]

for name, mark in zip(names, marks):

    print(name, mark)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("17. ITERATOR vs ITERABLE")
print("=" * 70)

print("""

Iterable
--------
Can create an iterator.

Examples
List
Tuple
Dictionary
String

Iterator
--------
Object that actually returns values
using next().
""")

print()

# ------------------------------------------------------------------

print("=" * 70)
print("18. REAL-WORLD EXAMPLE")
print("=" * 70)

"""
Imagine processing 1 million customer records.

Instead of loading all records simultaneously,
iteration processes one customer at a time.
"""

customers = ["Customer1", "Customer2", "Customer3"]

for customer in customers:
    print(customer)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

print("""
Q1. What is Iteration?

Iteration means accessing elements one by one
from an iterable object.

--------------------------------------------------

Q2. What is Iterable?

An object capable of returning an iterator.

--------------------------------------------------

Q3. What is Iterator?

An object that returns one element at a time
using next().

--------------------------------------------------

Q4. Difference between Iterable and Iterator?

Iterable
---------
Can create an iterator.

Iterator
---------
Can produce values one by one.

--------------------------------------------------

Q5. Which function creates an iterator?

iter()

--------------------------------------------------

Q6. Which function returns the next value?

next()

--------------------------------------------------

Q7. Which exception ends iteration?

StopIteration

--------------------------------------------------

Q8. Which methods are required for a custom iterator?

__iter__()
__next__()

--------------------------------------------------

Q9. Does every iterator implement __iter__()?

Yes.

It returns itself.

--------------------------------------------------

Q10. Are Generators Iterators?

Yes.

Every generator is an iterator,
but not every iterator is a generator.
""")

print("=" * 70)
print("END OF PROGRAM")
print("=" * 70)