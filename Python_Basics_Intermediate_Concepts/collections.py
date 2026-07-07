"""Collections: built-in container types for grouping, storing, and organizing data.

Python collections include basic containers like list, tuple, set, and dict,
plus specialized containers in the `collections` module for more advanced use cases.
This file shows examples and explanations for each kind.
"""

from collections import Counter, defaultdict, deque, namedtuple


def list_example():
    """List: ordered, mutable, and allows duplicates."""
    numbers = [1, 2, 3, 4, 5]
    # append adds a new item to the end of the list
    numbers.append(6)
    # insert adds an item at a specific position
    numbers.insert(0, 0)
    # list can be modified in place
    numbers[2] = 10
    return numbers


def tuple_example():
    """Tuple: ordered, immutable, and can contain mixed types."""
    coordinates = (10, 20)
    # tuples are immutable, so you cannot assign coordinates[0] = 5
    return coordinates


def set_example():
    """Set: unordered collection of unique items."""
    colors = {"red", "green", "blue", "red"}
    # duplicates are removed automatically
    colors.add("yellow")
    # membership tests are fast
    return colors


def dict_example():
    """Dict: mapping of keys to values, using hashable keys."""
    student_scores = {"Alice": 90, "Bob": 85}
    # add or update a key/value pair
    student_scores["Charlie"] = 92
    # safe retrieval with .get() avoids KeyError
    bob_score = student_scores.get("Bob")
    missing_score = student_scores.get("Diana", "Not found")
    return student_scores, bob_score, missing_score


def advanced_collections_example():
    """Specialized containers from the collections module."""
    # Counter: counts how often each item appears
    sample = ["apple", "banana", "apple", "orange", "banana"]
    counts = Counter(sample)
    # defaultdict: automatically creates missing keys with a default type
    grouped = defaultdict(list)
    for fruit in sample:
        grouped[fruit].append(len(fruit))
    # deque: double-ended queue with fast appends and pops from both ends
    queue = deque([1, 2, 3])
    queue.appendleft(0)
    queue.append(4)
    # namedtuple: lightweight object-like tuple with named fields
    Point = namedtuple("Point", ["x", "y"])
    point = Point(x=3, y=4)
    return counts, grouped, list(queue), point

# The following block runs only when this file is executed directly.
# When you import this module from another script, __name__ is set to
# the module name (for example, 'classes'), so the code below is skipped.
# The block runs only when the file is executed directly
# importing the file does not execute that demonstration code
if __name__ == "__main__":
    print("List example:", list_example())
    print("Tuple example:", tuple_example())
    print("Set example:", set_example())
    student_scores, bob_score, missing_score = dict_example()
    print("Dict example:", student_scores)
    print("Bob's score:", bob_score)
    print("Missing score message:", missing_score)
    counts, grouped, queue_state, point = advanced_collections_example()
    print("Counter example:", counts)
    print("Defaultdict example:", grouped)
    print("Deque example:", queue_state)
    print("Namedtuple example:", point)
