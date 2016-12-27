#!/usr/bin/python
import sys
i = len(sys.argv)
if i == 1:
    print('usage: python3 solution.py OP1 OP2')
elif i != 1:
    print(int(sys.argv[1]) - int(sys.argv[2]))
