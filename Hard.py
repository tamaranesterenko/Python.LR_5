#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)

    a = (8*x) / 9
    S, n = a, 0

while math.fabs(a) > EPS:
    a *= ((2*n + 2)**2) / (x * (2*n +1)**2)
    S += a
    n += 1

print(f"Shi(x) = ", S)
