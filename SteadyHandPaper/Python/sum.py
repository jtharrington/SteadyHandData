#! /usr/bin/python

import fileinput

sum = 0

for line in fileinput.input():
 line = line.strip()
 num = float(line)
 sum += num 

print sum
