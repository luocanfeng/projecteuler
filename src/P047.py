'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
# -*- coding: utf-8 -*
import GetPrimes

def f():
    primes = GetPrimes.getPrimes(1000000)
    n = 2 * 3 * 5 * 7
    _count = 0
    while True:
        c = countDistinctPrimes(n, primes)
        if c == 4:
            _count += 1
        else:
            _count = 0
        if _count == 4:
            print(n - 3)
            return n - 3
        n += 1

def countDistinctPrimes(n, primes):
    distinctPrimes = set()
    for prime in primes:
        while n % prime == 0:
            distinctPrimes.add(prime)
            n = n // prime
        if n == 1:
            break
    return len(distinctPrimes)

f()
