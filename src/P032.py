'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 
1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
# -*- coding: utf-8 -*

def f():
    # the length of multiplicand, multiplier and product tuple can be (1,4,4), (2,3,4) or (4,1,4), (3,2,4)
    # we can just try the length tuple (1,4,4) and (2,3,4)
    
    # try length tuple (1,4,4)
    result = set()
    for mc in range(2, 9 + 1):
        for m in range(1234, 9876 + 1):
            p = mc * m
            if p >= 1234 and p <= 9876:
                string = str(mc) + str(m) + str(p)
                s = set(string)
                if len(s) == 9 and '0'not in s:
                    print("%d*%d=%d" % (mc, m, p))
                    result.add(p)
                    
    # try length tuple (2,3,4)
    for mc in range(12, 98 + 1):
        for m in range(123, 987 + 1):
            p = mc * m
            if p >= 1234 and p <= 9876:
                string = str(mc) + str(m) + str(p)
                s = set(string)
                if len(s) == 9 and '0'not in s:
                    print("%d*%d=%d" % (mc, m, p))
                    result.add(p)
                    
    print(sum(result))

f()
