'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
# -*- coding: utf-8 -*
from functools import reduce

def f(n):
    factorial = reduce(lambda x, y:x * y, range(2, n + 1))
    print(sum(map(int, str(factorial))))

f(100)
