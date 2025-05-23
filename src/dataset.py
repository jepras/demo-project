"""def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


a = 10
b = 5

print(add(a, b))
"""

import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [24, 27]}

df = pd.DataFrame(data)

df.head(2)
