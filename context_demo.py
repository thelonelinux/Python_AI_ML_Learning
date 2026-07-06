"""Context-demo: using context managers to manage resources safely."""

from contextlib import contextmanager


class FileOpener:
    """Custom context manager using __enter__ and __exit__."""
    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        # Returning False means any exception will be propagated
        return False


@contextmanager
def simple_context(message: str):
    """A generator-based context manager using contextlib."""
    print(f"Entering: {message}")
    yield message
    print(f"Exiting: {message}")


if __name__ == "__main__":
    # Built-in context manager for file handling
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Hello from context_demo.py\n")

    # Custom context manager class
    with FileOpener("example.txt", "r") as file_handle:
        content = file_handle.read().strip()
        print("Read using custom context manager:", content)

    # Generator-based context manager
    with simple_context("demo") as value:
        print("Inside context with value:", value)
