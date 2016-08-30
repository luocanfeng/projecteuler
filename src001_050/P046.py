'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime 
and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
# -*- coding: utf-8 -*
import Primes

def f():
    primes = Primes.getPrimes(1000000)
    twiceSquares = set([2 * n * n for n in range(1, 10000)])
    
    o = 9
    flag = False
    while True:
        if o in primes:
            o += 2
            continue
        for p in primes:
            if o < p:
                flag = True
                break
            if o - p in twiceSquares:
                flag = False
                break
        if flag:
            print(o)
            return o
        o += 2
    return True

f()
