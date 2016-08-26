'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
# -*- coding: utf-8 -*
import GetPrimes

# print(16 * 9 * 5 * 7 * 11 * 13 * 17 * 19)

def f(n):
    primes = GetPrimes.getPrimes(n)
    result = 1
    for p in primes:
        m = 2
        while True:
            if p ** m > n:
                result *= p ** (m - 1)
                break
            else:
                m += 1
    print(result)
    
f(20)
