'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
# -*- coding: utf-8 -*
import Primes

def f(n):
    _range = int(n ** (3 / 2))
    primes = Primes.getPrimes(_range)
    if len(primes) >= n:
        print(primes[n - 1])
    return True

f(10001)
