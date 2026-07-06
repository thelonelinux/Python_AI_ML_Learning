"""Collections: built-in container types for storing ordered or unordered data."""

from collections import Counter, defaultdict, deque, namedtuple


def list_example():
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    return numbers


def tuple_example():
    coordinates = (10, 20)
    return coordinates


def set_example():
    unique_names = {"Alice", "Bob", "Alice"}  # duplicates are removed
    return unique_names


def dict_example():
    student_scores = {"Alice": 90, "Bob": 85}
    student_scores["Charlie"] = 92
    return student_scores


def advanced_collections_example():
    # Counter counts occurrences of items
    sample = ["apple", "banana", "apple", "orange", "banana"]
    counts = Counter(sample)

    # defaultdict returns a default value for missing keys
    grouped = defaultdict(list)
    for fruit in sample:
        grouped[fruit].append(len(fruit))

    # deque is a double-ended queue optimized for pushes/pops from both ends
    queue = deque([1, 2, 3])
    queue.appendleft(0)
    queue.append(4)

    Point = namedtuple("Point", ["x", "y"])
    point = Point(x=3, y=4)

    return counts, grouped, list(queue), point


if __name__ == "__main__":
    print("List example:", list_example())
    print("Tuple example:", tuple_example())
    print("Set example:", set_example())
    print("Dict example:", dict_example())
    counts, grouped, queue_state, point = advanced_collections_example()
    print("Counter example:", counts)
    print("Defaultdict example:", grouped)
    print("Deque example:", queue_state)
    print("Namedtuple example:", point)
