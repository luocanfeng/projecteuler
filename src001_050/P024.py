'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
# -*- coding: utf-8 -*

def f(n):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    factorials = [1]
    for i in range(1, 9):
        factorials.append(factorials[i - 1] * (i + 1))
    
    result = []
    r = n - 1
    for i in range(10):
        f = factorials[10 - i - 2]
        c = r // f
        result.append(digits[c])
        digits.remove(digits[c])
        r %= f
    print(''.join(list(map(str, result))))

f(1000000)
