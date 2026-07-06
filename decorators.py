"""Decorators: wrap functions or methods to modify behavior without changing the original code."""

from functools import wraps


def log_call(func):
    """A simple decorator that logs function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


def repeat(times: int):
    """A decorator factory that repeats calls to a function."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator


@log_call
def add(a: int, b: int) -> int:
    """Example function wrapped by a decorator."""
    return a + b


@repeat(3)
def greet(name: str) -> str:
    """Greeting function repeated three times by the decorator."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(add(2, 3))
    print(greet("Alice"))
