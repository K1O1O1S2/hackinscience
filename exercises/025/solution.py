#!/usr/bin/python
import time
import datetime
n = datetime.datetime.now()
print("Today is %s-%s-%s and it is %s:%s:%S") % (n.year, n.month, n.day, n.hour, n.minute, n.second)
