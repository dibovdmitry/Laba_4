#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    n = int(input("value of n? "))
    x = float(input("value of x? "))

    S= 0.0

    for k in range(1, n+1):
        a = math.log(k*x)
        S += a

        print(f"S = {S}")