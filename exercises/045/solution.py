#!/usr/bin/python
import math


def sqrt(num):
    if num == 0:
        print(0)
    elif num < 0:
        print(abs(num) ** 0.5)
    else:
        print(num ** 0.5)
