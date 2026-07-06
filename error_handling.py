"""Error_Handling: manage exceptions and cleanup with try/except/finally."""


class ValidationError(Exception):
    """Custom exception type for validation failures."""
    pass


def divide(a: float, b: float) -> float:
    """Raise an error when dividing by zero."""
    if b == 0:
        raise ValidationError("Cannot divide by zero")
    return a / b


def parse_integer(value: str) -> int:
    """Demonstrate exception handling during parsing."""
    try:
        return int(value)
    except ValueError as exc:
        raise ValidationError(f"Invalid integer: {value}") from exc


if __name__ == "__main__":
    inputs = ["10", "0", "abc"]

    for value in inputs:
        try:
            number = parse_integer(value)
            result = divide(10, number)
        except ValidationError as error:
            print(f"Validation error for input {value}: {error}")
        except Exception as unexpected:
            print(f"Unexpected error: {unexpected}")
        else:
            print(f"10 / {number} = {result}")
        finally:
            print("Finished processing", value)

    assert divide(4, 2) == 2, "Basic division should work"
