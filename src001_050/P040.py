'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
# -*- coding: utf-8 -*
import math
from functools import reduce

def f(n):
    # 1-9 -> 9
    # 10-99 -> 90*2
    # 100-999 -> 900*3
    # 1000-9999 -> 9000*4
    # 10000-99999 -> 90000*5
    # 100000-999999 -> 900000*6
    d = 1
    while True:
        if 9 * int(''.join(map(str, range(1, d + 1)[::-1]))) > n:
            break
        else:
            d += 1
    print(d)
    print(math.ceil((n - 9 * int(''.join(map(str, range(1, d)[::-1])))) / d) + 10 ** (d - 1))
    s = ''.join(map(str, range(math.ceil((n - 9 * int(''.join(map(str, range(1, d)[::-1])))) / d) + 10 ** (d - 1))))
    print(reduce(lambda x, y:x * y, map(lambda i:int(s[10 ** i]), range(6 + 1))))

f(1000000)
