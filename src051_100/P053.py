'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, C(5,3) = 10.

In general,

C(n,r) = n!/(r!(n−r)!), where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.

How many, not necessarily distinct, values of  C(n,r), for 1 ≤ n ≤ 100, are greater than one-million?
'''
# -*- coding: utf-8 -*

def f():
    factorials = [1]
    for i in range(1, 101):
        factorials.append(factorials[i - 1] * i)
    
    _count = 0
    for n in range(1, 101):
        for r in range(2, n + 1):
            cl = factorials[n] // factorials[r] // factorials[n - r]
            if cl > 1000000:
                _count += 1
    print(_count)

f()
