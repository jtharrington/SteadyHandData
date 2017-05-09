#! /usr/bin/python

import sys

for line in sys.stdin:
 line = line.strip()
 num = float(line)
 num = num**2
print num
