#!/usr/bin/python
a = range(0, 1000, 3)
b = range(0, 1000, 5)
c = [x for x in a if x not in b]
print(sum(c) + sum(b))
