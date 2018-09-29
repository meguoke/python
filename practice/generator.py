#!/usr/bin/env python
# -*- coding:utf-8 -*-


def fab(n):
    a = 0
    b = 1
    while n > 0:
        yield b
        a, b, n = b, a+b, n-1

if __name__ == "__main__":
    print "斐波那契 function generator"
    for x in fab(5):
        print x


