'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''
# -*- coding: utf-8 -*

def f():
    maximumDigitalSum = 0
    for i in range(1, 100):
        for j in range(1, 100):
            s = sum(map(int, str(i ** j)))
            if s > maximumDigitalSum:
                maximumDigitalSum = s
    print(maximumDigitalSum)

f()
