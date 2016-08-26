'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits 
from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
# -*- coding: utf-8 -*
import GetPrimes

def f():
    primes = set(GetPrimes.getPrimes(1000000))
    
    # a truncatable prime must not contains 0, and have to be end by 3 or 7
    subPrimes = set(filter(lambda p:(p % 10 == 3 or p % 10 == 7) and '0' not in str(p), primes)) - set([3, 7])
    
    truncatablePrimes = list(filter(lambda p:isTruncatablePrime(p, primes), subPrimes))
    # print(truncatablePrimes)
    print(sum(truncatablePrimes))

def isTruncatablePrime(n, primes):
    strn = str(n)
    for i in range(1, len(strn)):
        if int(strn[i:]) not in primes:
            return False
        if int(strn[:i]) not in primes:
            return False
    return True

f()
