"""Third_Party_Libraries: examples using common packages from requirements.txt."""

import numpy as np
import pandas as pd
import seaborn as sns


def numpy_example():
    array = np.array([1, 2, 3, 4, 5])
    return array * 2, np.mean(array), np.std(array)


def pandas_example():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "score": [95, 82, 77],
    })
    return df.describe(), df["score"].mean()


def seaborn_example():
    data = sns.load_dataset("tips")
    return data.head()


if __name__ == "__main__":
    doubled, mean, std = numpy_example()
    print("NumPy doubled:", doubled)
    print("NumPy mean:", mean, "std:", std)

    describe, average_score = pandas_example()
    print("Pandas describe:\n", describe)
    print("Pandas average score:", average_score)

    print("Seaborn dataset sample:\n", seaborn_example())
