'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, 
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
# -*- coding: utf-8 -*
import Primes

def f(n):
    primes = Primes.getPrimes(n)
    primesSet = set(primes)
    
    # maxLen=546, sum(primes[:546])=997661, sum(primes[:547])=1001604
    maxLen = 0
    while True:
        if sum(primes[:maxLen]) > n:
            break
        maxLen += 1
    maxLen -= 1
#     print(maxLen)
    
    # minLen=536, sum(primes[:536]=958577为素数
    minLen = 0
    for i in range(maxLen)[::-1]:
        _sum = sum(primes[:i])
        if _sum < n and _sum in primesSet:
            minLen = i
#             print(i, minLen, _sum)
            break
    
    # 接下来循环
    diff = maxLen - minLen
    theLen = 0
    theNumber = 0
    for i in range(minLen, maxLen + diff):
        for d in range(diff):
            _sum = sum(primes[d:i])
            tempLen = i - d + 1
            if _sum < n and _sum in primesSet:
#                 print(d, i, tempLen, _sum)
                if tempLen > theLen:
                    theLen = tempLen
                    theNumber = _sum
                    break
    print(theNumber)

f(1000000)
