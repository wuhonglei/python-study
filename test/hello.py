#!/usr/bin/python3

import keyword
from pprint import pprint

line1 = 1
line2 = 2
line3 = 3
total = [1,
         2,
         3]
print(total)
total.insert(1, 'new')
print(total.__class__)
