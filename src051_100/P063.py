'''
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, 
is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
# -*- coding: utf-8 -*

def f():
    maxN = 1
    while True:
        maxN += 1
        if 9 ** maxN < 10 ** (maxN - 1):
            maxN -= 1
            break
        
    _count = 0
    for digits in range(1, maxN + 1):
        for x in range(1, 10):
            if len(str(x ** digits)) == digits:
                _count += 1
    print(_count)

f()
