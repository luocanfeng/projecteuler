'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, 
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
# -*- coding: utf-8 -*
import GetPrimes

def f(n):
    primes = GetPrimes.getPrimes(n)
    primesSet = set(primes)
    count = 2  # 2 and 5
    for p in primes:
        strp = str(p)
        if '0' not in strp and '2' not in strp and '4' not in strp and '5' not in strp and '6' not in strp and '8' not in strp:
#             rotationsSet = rotations(p)
            rotationsSet = set(map(lambda i:int(strp[i:] + strp[:i]), range(len(strp))))
            if rotationsSet <= primesSet:
#                 print(rotationsSet)
                count += len(rotationsSet)
            primesSet -= rotationsSet
    print(count)

# def rotations(n):
#     strn = str(n)
#     rotationsSet = set([n])
#     for i in range(len(strn)):
#         rotationsSet.add(int(strn[i:] + strn[:i]))
#     return rotationsSet

f(1000000)
