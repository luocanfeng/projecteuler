'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
# -*- coding: utf-8 -*

lenOfChainDict = {}
lenOfChainDict[1] = 1
lenOfChainDict[2] = 2

def f(n):
    for i in range(3, n):
        getLenOfChain(i)
    
    _len = 0
    theNumber = 0
    for i in range(3, n):
        if lenOfChainDict[i] > _len:
            _len = lenOfChainDict[i]
            theNumber = i
    print(theNumber)

def getLenOfChain(n):
    _next = n // 2 if n % 2 == 0 else n * 3 + 1
    if _next in lenOfChainDict.keys():
        lenOfChainDict[n] = lenOfChainDict[_next] + 1
    else:
        lenOfChainDict[n] = getLenOfChain(_next) + 1
    return lenOfChainDict[n]

f(1000000)
