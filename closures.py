"""Closures: functions that remember values from their enclosing lexical scope.

A closure is created when an inner function captures variables from its outer function
and retains access to them even after the outer function has finished executing.
That captured state becomes part of the inner function's environment, allowing the
inner function to keep using those values later.

Closures are useful for:
- building functions with customized behavior (function factories)
- keeping private state without using classes or global variables
- wrapping behavior while preserving context information
"""


def make_multiplier(factor: int):
    """Return a function that multiplies its input by the captured factor.

    The returned function keeps access to `factor` even after make_multiplier() returns.
    This captured data belongs to the closure.
    """
    def multiplier(value: int) -> int:
        # `factor` is not a local variable of multiplier(), but it is available
        # because multiplier() closes over the environment where it was defined.
        return value * factor

    return multiplier


def make_adder(amount: int):
    """Return a function that adds the captured amount to its input."""
    def adder(value: int) -> int:
        # `amount` is preserved inside this returned function.
        return value + amount
    return adder


def make_counter():
    """Return a counter function with private state.

    `count` is stored in the enclosing scope and updated with nonlocal.
    This makes the closure stateful across calls.
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def make_prefix_logger(prefix: str):
    """Return a logger function that uses the captured prefix."""
    def logger(message: str) -> None:
        print(f"{prefix}: {message}")
    return logger


def make_functions():
    """Demonstrate the common closure trap with loop variables.

    In Python, closures capture variables by reference. If we create functions
    inside a loop that refer to the loop variable, all functions may end up
    referring to the final value of that variable.
    """
    functions = []
    for i in range(3):
        def show_i():
            return i
        functions.append(show_i)
    return functions


def make_functions_fixed():
    """Fix the loop closure trap by binding the current loop value as a default."""
    functions = []
    for i in range(3):
        def show_i(bound_i=i):
            return bound_i
        functions.append(show_i)
    return functions


if __name__ == "__main__":
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print("double(5)", double(5))  # 10
    print("triple(5)", triple(5))  # 15

    add_five = make_adder(5)
    print("add_five(10)", add_five(10))  # 15

    counter_a = make_counter()
    print("counter_a()", counter_a())  # 1
    print("counter_a()", counter_a())  # 2

    logger = make_prefix_logger("DEBUG")
    logger("This is a closure example")

    functions = make_functions()
    print("Closure trap values:", [f() for f in functions])

    fixed_functions = make_functions_fixed()
    print("Fixed closure values:", [f() for f in fixed_functions])
