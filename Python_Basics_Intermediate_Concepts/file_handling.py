"""
====================================================================
                    FILE HANDLING IN PYTHON
====================================================================

Definition
----------
File Handling is the process of creating, reading, writing,
updating, and deleting files using Python.

Why File Handling?
------------------
1. Store data permanently.
2. Read existing data.
3. Update data.
4. Process large datasets.
5. Generate reports and logs.

====================================================================
"""

import os

print("=" * 70)
print("1. CREATING A FILE")
print("=" * 70)

# "w" mode creates a new file.
# If the file already exists, its content will be overwritten.

with open("student.txt", "w") as file:
    file.write("Name : Vicky\n")
    file.write("Course : Python\n")
    file.write("Experience : 3 Years\n")

print("student.txt created successfully.\n")

# ------------------------------------------------------------------

print("=" * 70)
print("2. READING ENTIRE FILE")
print("=" * 70)

# "r" mode opens the file for reading.

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# ------------------------------------------------------------------

print("=" * 70)
print("3. READ FIRST N CHARACTERS")
print("=" * 70)

# read(n) reads only n characters.

with open("student.txt", "r") as file:
    print(file.read(10))

print()

# ------------------------------------------------------------------

print("=" * 70)
print("4. READ ONE LINE")
print("=" * 70)

# readline() reads one line at a time.

with open("student.txt", "r") as file:
    print(file.readline())
    print(file.readline())

# ------------------------------------------------------------------

print("=" * 70)
print("5. READ ALL LINES")
print("=" * 70)

# readlines() returns a list of all lines.

with open("student.txt", "r") as file:
    lines = file.readlines()

print(lines)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("6. ITERATE THROUGH FILE")
print("=" * 70)

# Best way for large files.

with open("student.txt", "r") as file:

    for line in file:
        print(line.strip())

print()

# ------------------------------------------------------------------

print("=" * 70)
print("7. APPEND DATA")
print("=" * 70)

# "a" mode appends new data.
# Existing content is preserved.

with open("student.txt", "a") as file:
    file.write("Location : Delhi\n")

print("Data appended successfully.\n")

# ------------------------------------------------------------------

print("=" * 70)
print("8. OVERWRITE FILE")
print("=" * 70)

# "w" mode overwrites existing content.

with open("student_overwrite.txt", "w") as file:
    file.write("Old data removed.\n")
    file.write("New data added.\n")

print("student_overwrite.txt created.\n")

# ------------------------------------------------------------------

print("=" * 70)
print("9. READ AND WRITE MODE (r+)")
print("=" * 70)

# r+ allows reading and writing.
# File must already exist.

with open("student.txt", "r+") as file:

    print(file.readline())

    file.write("Age : 27\n")

print("Read and Write completed.\n")

# ------------------------------------------------------------------

print("=" * 70)
print("10. WRITE AND READ MODE (w+)")
print("=" * 70)

# w+ creates a new file or truncates an existing one.

with open("sample1.txt", "w+") as file:

    file.write("Hello Python")

    # Move cursor to beginning before reading.
    file.seek(0)

    print(file.read())

print()

# ------------------------------------------------------------------

print("=" * 70)
print("11. APPEND AND READ MODE (a+)")
print("=" * 70)

# a+ appends data and allows reading.

with open("sample2.txt", "a+") as file:

    file.write("Learning File Handling\n")

    # Move cursor to beginning.
    file.seek(0)

    print(file.read())

print()

# ------------------------------------------------------------------

print("=" * 70)
print("12. FILE POINTER")
print("=" * 70)

# tell() returns current cursor position.
# seek() moves cursor.

with open("student.txt", "r") as file:

    print("Initial Position :", file.tell())

    print(file.read(5))

    print("Current Position :", file.tell())

    file.seek(0)

    print("After seek :", file.tell())

print()

# ------------------------------------------------------------------

print("=" * 70)
print("13. COPYING FILE")
print("=" * 70)

with open("student.txt", "r") as source:

    data = source.read()

with open("student_copy.txt", "w") as destination:

    destination.write(data)

print("File copied successfully.\n")

# ------------------------------------------------------------------

print("=" * 70)
print("14. RENAMING FILE")
print("=" * 70)

# Rename only if destination does not exist.

if os.path.exists("student_copy.txt"):

    os.rename("student_copy.txt", "student_backup.txt")

    print("File renamed.\n")

# ------------------------------------------------------------------

print("=" * 70)
print("15. CHECK IF FILE EXISTS")
print("=" * 70)

if os.path.exists("student.txt"):
    print("File exists.")
else:
    print("File not found.")

print()

# ------------------------------------------------------------------

print("=" * 70)
print("16. FILE INFORMATION")
print("=" * 70)

with open("student.txt", "r") as file:

    print("File Name :", file.name)
    print("Mode :", file.mode)
    print("Readable :", file.readable())
    print("Writable :", file.writable())
    print("Closed :", file.closed)

print()

# ------------------------------------------------------------------

print("=" * 70)
print("17. DELETE FILE")
print("=" * 70)

# Delete only if file exists.

if os.path.exists("sample2.txt"):

    os.remove("sample2.txt")

    print("sample2.txt deleted.")

print()

# ------------------------------------------------------------------

print("=" * 70)
print("18. EXCEPTION HANDLING")
print("=" * 70)

try:

    with open("unknown.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("Requested file does not exist.")

print()

# ------------------------------------------------------------------

print("=" * 70)
print("19. BINARY FILE")
print("=" * 70)

# Writing binary data.

with open("binary.dat", "wb") as file:

    file.write(b"Python Binary Data")

print("Binary file written.\n")

# Reading binary data.

with open("binary.dat", "rb") as file:

    print(file.read())

print()

# ------------------------------------------------------------------

print("=" * 70)
print("20. FILE MODES")
print("=" * 70)

print("""
r   -> Read
w   -> Write (Overwrite)
a   -> Append
x   -> Create new file only
r+  -> Read + Write
w+  -> Write + Read
a+  -> Append + Read
rb  -> Read Binary
wb  -> Write Binary
ab  -> Append Binary
""")

# ------------------------------------------------------------------

print("=" * 70)
print("INTERVIEW QUESTIONS")
print("=" * 70)

print("""
Q1. What is File Handling?
A.
Process of reading and writing data to files.

Q2. Why use 'with'?
A.
Automatically closes the file even if an exception occurs.

Q3. Difference between read(), readline(), and readlines()?

read()
-------
Reads entire file.

readline()
-----------
Reads one line.

readlines()
------------
Returns all lines as a list.

Q4. Difference between write() and writelines()?

write()
--------
Writes a string.

writelines()
-------------
Writes multiple strings from a list.
(No newline is added automatically.)

Q5. Difference between 'w' and 'a'?

w
-
Overwrites file.

a
-
Appends to existing file.

Q6. What do seek() and tell() do?

seek()
------
Moves file pointer.

tell()
------
Returns current file pointer position.

Q7. Which mode is safest for reading?
A.
'r'

Q8. Which mode creates a file if it doesn't exist?
A.
'w', 'a', 'w+', 'a+', 'x'

Q9. Why use binary mode?
A.
To read/write non-text files such as images, videos,
PDFs, or serialized objects.
""")

print("=" * 70)
print("END OF PROGRAM")
print("=" * 70)