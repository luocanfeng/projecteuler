'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
# -*- coding: utf-8 -*
import Primes
import itertools

def f():
    primes = list(filter(lambda p:p > 1000, Primes.getPrimes(9999)))
    for p in primes:
        s = set(filter(lambda x:x > 1000 and x in primes, \
                       map(lambda item:int(''.join(item)), itertools.permutations(str(p)))))
        if len(s) < 3:
            continue
        s = list(s)
        s.sort()
        for item in itertools.combinations(range(len(s)), 3):
            if s[item[0]] + s[item[2]] == 2 * s[item[1]] and s[item[0]] != 1487:
                print('%d%d%d' % (s[item[0]], s[item[1]], s[item[2]]))
                return True

f()
