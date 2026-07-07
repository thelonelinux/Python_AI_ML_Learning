"""StandardLibraries: examples using built-in Python standard libraries."""

import math
import datetime
import json
import random
import os
import sys


def math_example():
    return {
        "pi": math.pi,
        "sqrt_16": math.sqrt(16),
        "isfinite": math.isfinite(1 / 3),
    }


def datetime_example():
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    return {
        "now": now.isoformat(),
        "tomorrow": tomorrow.isoformat(),
    }


def json_example():
    data = {"name": "Alice", "active": True, "scores": [95, 82, 77]}
    return json.dumps(data), json.loads(json.dumps(data))


def random_example():
    return {
        "choice": random.choice(["red", "green", "blue"]),
        "shuffle": random.sample([1, 2, 3, 4, 5], 3),
    }


def os_sys_example():
    return {
        "cwd": os.getcwd(),
        "python_version": sys.version,
        "path_count": len(sys.path),
    }


if __name__ == "__main__":
    print("Math example:", math_example())
    print("Datetime example:", datetime_example())
    json_string, json_data = json_example()
    print("JSON string:", json_string)
    print("JSON data:", json_data)
    print("Random example:", random_example())
    print("OS/Sys example:", os_sys_example())
