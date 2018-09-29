#!/usr/bin/env python
# -*- code:utf-8 -*-


map = {"1":12,"2":"haha","4":12123}
print {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['1']

for x in map:
    print ("key:%s value:%s" % (x, map.get(x)))
    #map.pop(x)
print "map iterator the value"
for v in map.itervalues():
    print "value=", v
print "map iterator the key and value "
for k,v in map.iteritems():
    print k,v
print '''list iterator
fisrt 
test 
multi 
lint 
'''
print "iterator the list and the index "
for i,v in enumerate([1,2,3,4]):
    print "index:", i,"\tvalue:", v

# list in set
set = ([1,2,3,4,5])
print "iterator the set:"
for x in set:
    print x
    #set.pop(x)
# constant set
constantSet = (1,2,3,4,4,5,6,7)
print "length of the constantSet:",len(constantSet)
