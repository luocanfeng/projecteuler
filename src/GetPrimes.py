'''
return the primes array not larger than the given number.
'''
import math

def getPrimes(n):
    boolArr = [True, False] * int(n / 2)
    if n % 2 != 0:
        boolArr.append(True)
    boolArr[1 - 1] = False
    boolArr[2 - 1] = True
    sqrt = int(math.sqrt(n))
    for i in range(3, sqrt + 1)[::2]:
        if boolArr[i - 1]:
            for j in range(i + i, n + 1)[::i]:
                boolArr[j - 1] = False
    primeArr = []
    length = len(boolArr)
    for i in range(length):
        if boolArr[i]:
            primeArr.append(i + 1)
    return primeArr
