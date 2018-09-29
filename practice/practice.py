#!/usr/bin/env python
# -*- coding: utf-8 -*-

for suffix in range(9):
    column = 0
    lineResult =""
    #if line == suffix :
    while column <= suffix :
            lineResult = lineResult+("%d x %d\t" % (column+1,suffix+1))
            column = column+1
    print lineResult
