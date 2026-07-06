"""file2.py: imports and calls a function defined in file1.py."""

# Import the greet_person function from file1.py.
# Python uses the module name without the .py extension.
from file1 import greet_person


def main():
    # Call the imported function as if it were defined in this module.
    greeting = greet_person("Bob")
    print(greeting)


if __name__ == "__main__":
    # Run the demonstration when file2.py is executed directly.
    main()
