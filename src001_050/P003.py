'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
# -*- coding: utf-8 -*
import math
import Primes

def f(n):
    sqrt = int(math.sqrt(n))
    primes = Primes.getPrimes(sqrt)
    # print(primes)

    for prime in primes[::-1]:
        if n % prime == 0:
            print(prime)
            return prime

f(600851475143)
