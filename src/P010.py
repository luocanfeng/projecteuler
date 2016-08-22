'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
# -*- coding: utf-8 -*
import GetPrimes

def f(n):
    print(sum(GetPrimes.getPrimes(n - 1)))

f(2000000)
