"""file1.py: defines a reusable function that can be imported from other modules."""


def greet_person(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to the imported function example."


if __name__ == "__main__":
    # This code runs only when file1.py is executed directly.
    print(greet_person("Alice"))
