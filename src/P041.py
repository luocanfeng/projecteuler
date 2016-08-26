'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
# -*- coding: utf-8 -*
import GetPrimes
import math
import itertools

def f():
    # 9-digit number would not be a prime, because it can be divided by 9 with no remainder
    sqrt = math.ceil(math.sqrt(87654321))
    primes = GetPrimes.getPrimes(sqrt)
    for d in range(1, 9)[::-1]:
        permutations = list(map(lambda item:int(''.join(item)), itertools.permutations(map(str, range(1, d + 1)))))
        permutations.sort()
        for n in permutations[::-1]:
            if n not in primes and isPrime(n, primes):
                print(n)
                return n
#         pandigitalPrimes = list(filter(lambda n:isPrime(n, primes), \
#                           map(lambda item:int(''.join(item)), itertools.permutations(map(str, range(1, d + 1))))))
#         if len(pandigitalPrimes) != 0:
#             print(max(pandigitalPrimes))
#             return True

def isPrime(n, primes):
    for p in primes:
        sqrt = math.ceil(math.sqrt(n))
        if p > sqrt:
            return True
        if n % p == 0:
            return False
    return True

f()
