"""Iteration: demonstrate for loops, while loops, and iterator protocol."""


def for_loop_example(items):
    return [item.upper() for item in items]


def while_loop_example(limit):
    values = []
    n = 0
    while n < limit:
        values.append(n)
        n += 1
    return values


def iterator_protocol_example(iterable):
    iterator = iter(iterable)
    values = []
    while True:
        try:
            values.append(next(iterator))
        except StopIteration:
            break
    return values


if __name__ == "__main__":
    items = ["apple", "banana", "cherry"]
    print("For loop example:", for_loop_example(items))
    print("While loop example:", while_loop_example(5))
    print("Iterator protocol example:", iterator_protocol_example(items))
