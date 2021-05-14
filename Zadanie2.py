#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

x = int(input("Введите число x "))
y = int(input("Введите число y "))
mx = 0
mn = 0
s = 0
if x > y:
    mx = pow(x, 2), y
    mn = x - y
else:
    mx = x, pow(y, 2)
    mn = x + 2 * y
    s = mx + mn
    print(s)
