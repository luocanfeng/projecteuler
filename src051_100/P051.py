'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 
56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime 
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with 
the same digit, is part of an eight prime value family.
'''
# -*- coding: utf-8 -*
import Primes
import itertools

def f():
    primes = list(filter(lambda p:p > 1000, Primes.getPrimes(1000000)))
    primesSet = set(primes)
    
    # 要替换的数字个数必定为3/6/9，因为如果替换1/2/4/5/7/8/10...，替换为0-9这些数字，取其中8个数字，
    # 其中必定至少有一个能被3整除，不是素数
    
    chars = list(map(str, range(10)))
    
    primeFamilies = {}
    for p in primes:
        strp = str(p)
        digits = len(strp)
        if digits < 4:
            break
        
        digitIndexs = {}
        for i in range(len(strp)):
            if strp[i] not in digitIndexs.keys():
                digitIndexs[strp[i]] = []
            digitIndexs[strp[i]].append(i)
        
        for v in digitIndexs.values():
            if len(v) >= 3:
                for idx in itertools.combinations(v, 3):
                    numbers = []
                    discard = 0
                    for c in chars:
                        repl = strp[:idx[0]] + c + strp[idx[0] + 1:idx[1]] + c + strp[idx[1] + 1:idx[2]] \
                                    + c + strp[idx[2] + 1:]
                        if repl[0] != '0' and int(repl) in primesSet:
                            numbers.append(int(repl))
                        else:
                            discard += 1
                            if discard > 2:
                                break
                    if len(numbers) >= 8 and numbers[0] not in primeFamilies.keys():
                        primeFamilies[numbers[0]] = numbers
    
    print(min(primeFamilies.keys()))

f()
