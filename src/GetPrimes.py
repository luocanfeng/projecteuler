'''
return the primes array not larger than the given number.
'''
# -*- coding: utf-8 -*
import math

def getPrimes(n):
    boolArr = list(map(lambda x:x % 2 != 0, range(1, n + 1)))
    
    boolArr[0] = False  # 1 is not a prime number
    boolArr[1] = True  # 2 is a prime number
    
    sqrt = int(math.sqrt(n))
    for i in range(3, sqrt + 1)[::2]:
        if boolArr[i - 1]:
            for j in range(i + i, n + 1)[::i]:
                boolArr[j - 1] = False
    
    primeArr = []
    for i in range(n):
        if boolArr[i]:
            primeArr.append(i + 1)
    return primeArr

# print(len(getPrimes(1000000)))
