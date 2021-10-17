#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 10
S = 0

for i in range(7):
    x = x + 0.1*x
    S += x

print(f"The athlete will run {S} km in 7 days")
