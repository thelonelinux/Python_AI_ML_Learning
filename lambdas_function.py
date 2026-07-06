"""Lambdas_Function: small anonymous functions and higher-order function usage."""


def apply_operation(values, operation):
    """Apply a function to each value in the list."""
    return [operation(value) for value in values]


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]

    doubled = apply_operation(values, lambda x: x * 2)
    print("Doubled:", doubled)

    even_values = list(filter(lambda x: x % 2 == 0, values))
    print("Even values:", even_values)

    squares = list(map(lambda x: x * x, values))
    print("Squares:", squares)

    sorted_by_length = sorted(["pear", "apple", "banana"], key=lambda word: len(word))
    print("Sorted by length:", sorted_by_length)
