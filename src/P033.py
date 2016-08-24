'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it 
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
# -*- coding: utf-8 -*

def f():
    result = []
    for i in range(1, 10):
        for n in range(1, 10):
            for d in range(n + 1, 10):  # numerator must less than denominator
                if (10 * i + n) * d == (10 * d + i) * n:
                    result.append((n, d))
                if (10 * n + i) * d == (10 * i + d) * n:
                    result.append((n, d))
    # print(result)
    
    numerator, denominator = 1, 1
    for (n, d) in result:
        numerator *= n
        denominator *= d
    
    _gcd = gcd(numerator, denominator)
    print(denominator // _gcd)

def gcd(a, b):
    x, y = max(a, b), min(a, b)
    if y == 0:
        return x
    elif x % y == 0:
        return y
    else:
        return gcd(y, x % y)

f()
