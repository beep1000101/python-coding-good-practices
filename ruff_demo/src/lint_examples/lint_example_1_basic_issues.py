import os
import numpy as np
import pandas as pd  # unused


def add(x, y, debug=False):
    resut = x + y  # typo
    tmp = 42  # unused
    if debug == True:
        print("Result is", result)  # result undefined
    value = 10
    value = 20  # redefined
    try:
        risky = x / y
    except:
        risky = None
    return resut


def unused_arg(a, b, unused_param):
    return a * b


def check_flag(flag):
    if flag == True:
        return "Flag is True"
    else:
        return "Flag is False"


def unused_vars():
    a = 1
    b = 2
    c = a + b  # unused
    return a
