#!/usr/bin/python
import math


def sqrt(num):
    if num == 0:
        return 0
    elif num < 0:
        return -num ** 0.5
    else:
        return num ** 0.5
