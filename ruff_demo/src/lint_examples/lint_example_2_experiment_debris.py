import matplotlib.pyplot as plt
import seaborn as sns
import random

# Old experiment code
# def run_old_exp(data):
#     for i in range(10):
#         print(i, data[i])
#     return None


def process(data):
    result = []
    for i in range(len(data)):
        result.append(data[i] * 2)
    return result


def process(data):  # duplicated function
    res = []
    for d in data:
        res.append(d + 1)
    return res


def unused_func(x):
    return x ** 2


# Main script flow
data = [1, 2, 3, 4, 5]
x = 5
x = "now a string"
y = 3.14
y = y * 2
magic = 42
for i in range(5):
    print("Iteration", i)
    temp = process(data)
    # temp is reused
    temp = unused_func(i)

# Unused function, never called


def never_called():
    print("I am never used")

# More debris
# def another_old_func():
#     pass
