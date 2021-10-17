#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    x = int(input("Enter the number of the day of the week:"))

    if x == 1:
        print("Monday")
    elif x == 2:
        print("Tuesday")
    elif x == 3:
        print("Wednesday")
    elif x == 4:
        print("Thursday")
    elif x == 5:
        print("Friday")
    elif x == 6:
        print("Saturday")
    elif x == 7:
        print("Sunday")
    else:
        print("Error!", file=sys.stderr)
        exit(1)
