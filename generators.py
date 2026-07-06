"""Generators: create iterators with lazy evaluation using yield."""


def countdown(n: int):
    """Yield numbers from n down to 1 lazily."""
    while n > 0:
        yield n
        n -= 1


def fibonacci(limit: int):
    """Yield Fibonacci numbers until the limit is reached."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def generate_squares(nums):
    """Generator comprehension example."""
    return (x * x for x in nums)


if __name__ == "__main__":
    print("Countdown:", list(countdown(5)))
    print("Fibonacci up to 20:", list(fibonacci(20)))
    squares = generate_squares([1, 2, 3, 4, 5])
    print("Squares:", list(squares))
