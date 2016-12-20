#!/usr/bin/python
import sys
i = len(sys.argv[0])
if i < 1:
  print('usage: python3 solution.py PARAM')
elif i != 0:
  print(sys.argv[0])
