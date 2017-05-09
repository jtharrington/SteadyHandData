#! /usr/bin/python


vals = [0.5, 1.0, 1.5]
print vals

vals.append(2.0)
print "--"
print vals

print "--"
print vals[0]
print vals[-1]

print "--"
for val in vals:
 print val


print "--"
print len(vals)


print "--"
for i in range(len(vals)):
 print i,vals[i]


print "--"
print range(10)
print range(2,10)

vals.pop(0)
print vals
