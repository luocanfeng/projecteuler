'''
Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
However, when n=40, 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41, 
41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive 
values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number 
of primes for consecutive values of n, starting with n=0.
'''
# -*- coding: utf-8 -*
from GetPrimes import getPrimes
import time

def f(n):
    start = time.time()
    calRangeDepth = 12  # the depth every time calculating range of a
    
    primesArrs = []
    for i in range(calRangeDepth):
        primesArrs.append(getPrimes((i + 1) * n + i * i - 1))
    
    theBigPrimesArr = getPrimes(2 * n * n + n)
    
    x, y, z = 0, 0, 0  # record the a, b, n which has the max n
    for b in primesArrs[0]:  # while n starts with 0, the number b must be a prime, and positive
        aRange = set(range(-1000, 1000))
        for d in range(1, calRangeDepth):
            # because of n^2 + an + b is a prime, we can decrease the range of number a
            aRange = aRange.intersection(set(map(lambda p:int((p - b - d * d) / d), primesArrs[d])))
        
        for a in aRange:
            for n in range(1, 10000):
                if n * n + n * a + b not in theBigPrimesArr:
                    if n > z:
                        x, y, z = a, b, n
                    # print("a=%d, b=%d, n=%d" % (a, b, n))
                    break

    print(x * y)
    end = time.time() - start
    print("Cost %.3fs" % (end))

f(1000)
