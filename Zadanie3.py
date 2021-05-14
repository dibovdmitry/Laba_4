#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
d = 0
r = 0
m = 0

for i in range(100, 1000):
    d = i//100
    r = i % 100//10
    m = i % 10
    o = d + r + m
    n = d * r * m
    if o == n:
        print(i)
