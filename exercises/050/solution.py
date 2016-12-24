#!/usr/bin/python
a = range(0, 999, 3)
b = range(0, 999, 5)
c = set(a) - set(b)
print(sum(c))
