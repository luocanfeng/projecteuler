'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
# -*- coding: utf-8 -*
from collections import Counter

def f():
    n = 11
    while True:
        n += 1
        c = Counter(str(n))
        if c == Counter(str(n * 2)) and c == Counter(str(n * 3)) and c == Counter(str(n * 4)) \
                and c == Counter(str(n * 5)) and c == Counter(str(n * 6)):
            print(n)
            return n

f()
