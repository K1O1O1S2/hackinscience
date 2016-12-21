#!/usr/bin/python
import sys
i = len(sys.argv[1])
if i == 1:
   print('usage: python3 solution.py PARAM')
elif i != 1:
   print(sys.argv[1])
