'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 
in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''
# -*- coding: utf-8 -*

def f():
    p = [2, 3, 5, 7, 11, 13, 17]
    d3 = list(map(lambda i:possible3DigitsNumbers(p[i]), range(7)))
    possibleDigits = d3[6]
    for i in range(3, 9):
        possibleDigits = joinDigitsNumbers(possibleDigits, i, d3[8 - i])
    pandigitalNumbers = list(map(lambda d:int((list(set('0123456789') - set(str(d))))[0] + str(d)), possibleDigits))
#     print(pandigitalNumbers)
    print(sum(pandigitalNumbers))
    
def possible3DigitsNumbers(divisible):
    return list(filter(lambda x:len(set(str(x))) == 3 or (x < 100 and x % 11 != 0), \
                       map(lambda m:m * divisible, range(1, 1000 // divisible))))
    
def joinDigitsNumbers(rDigitsNumbers, rDigits, lDigitsNumbers):
    joined = []
    m = 10 ** (rDigits - 2)
    for r in rDigitsNumbers:
        for l in lDigitsNumbers:
            if l < 100 and len(str(r)) < rDigits:
                continue
            if r // m == l % 100 and str(l // 100) not in str(r):
                joined.append(l * m + r % m)
    return joined
    
f()
