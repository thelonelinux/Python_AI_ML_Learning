"""Context-manager demonstration: detailed examples and comments.

A context manager is a Python construct that defines setup and cleanup logic
for a resource. It is usually used with the `with` statement.

The `with` statement ensures that the resource is properly released, even if an
exception occurs while the resource is in use. Context managers can be implemented
using a class with `__enter__` and `__exit__`, or by using the `contextlib`
module with a generator function.
"""

from contextlib import contextmanager


class FileOpener:
    """Custom context manager implementing __enter__ and __exit__ methods."""

    def __init__(self, filename: str, mode: str = "r"):
        # Store the file path and mode for later use when entering the block.
        self.filename = filename
        self.mode = mode
        # Initialize the file handle variable; it will hold the opened file.
        self.file = None

    def __enter__(self):
        # Open the file when entering the with block.
        # This is where resource acquisition happens.
        self.file = open(self.filename, self.mode, encoding="utf-8")
        # Return the opened file object so it can be used inside the with block.
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # This method runs when exiting the with block, whether an exception occurred
        # or not. It is responsible for cleaning up the resource.
        if self.file:
            self.file.close()
        # If __exit__ returns True, any exception is suppressed.
        # Returning False lets exceptions propagate normally.
        return False


@contextmanager
def simple_context(message: str):
    """Context manager built with a generator using contextlib."""
    # Code before yield runs on entering the with block.
    print(f"Entering context with message: {message}")
    try:
        # The value yielded here is assigned to the variable after `as`.
        yield message
    finally:
        # Code after yield runs on exit, regardless of success or exception.
        print(f"Exiting context with message: {message}")


def read_write_example():
    """Example showing a built-in context manager for file I/O."""
    # open() returns a file object that implements __enter__/__exit__.
    with open("example.txt", "w", encoding="utf-8") as file_handle:
        # The file is open inside the with block.
        file_handle.write("Line one\n")
        file_handle.write("Line two\n")
    # The file is automatically closed after the block.

    with open("example.txt", "r", encoding="utf-8") as file_handle:
        # Read file content while the file is still open.
        content = file_handle.read()
    # File handle is closed here.
    return content


def custom_manager_example():
    """Example using the custom FileOpener context manager."""
    # FileOpener uses __enter__ and __exit__ behind the scenes.
    with FileOpener("example.txt", "r") as file_handle:
        # The opened file object is available as file_handle here.
        return file_handle.read()


def generator_context_example():
    """Example using a generator-based context manager."""
    with simple_context("demo context") as value:
        # The yielded value from simple_context is accessible in this block.
        print("Inside generator-based context, value =", value)
        return f"Returned from {value}"


if __name__ == "__main__":
    # Demonstrate the built-in context manager behavior.
    file_contents = read_write_example()
    print("Read from example.txt:\n", file_contents)

    # Demonstrate the custom FileOpener class as context manager.
    read_back = custom_manager_example()
    print("Read using custom FileOpener:\n", read_back)

    # Demonstrate the generator-based context manager.
    returned_value = generator_context_example()
    print(returned_value)
