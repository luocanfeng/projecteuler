'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
# -*- coding: utf-8 -*

def f():
    factorials = [1, 1]  # It's very important that the factorial of 0 is 1
    for i in range(2, 10):
        factorials.append(factorials[i - 1] * i)
    print(factorials)
    
    digits = 1
    while True:
        if factorials[9] * digits < 10 ** (digits - 1)  :
            digits -= 1
            break
        else:
            digits += 1
    print(digits)

    _sum = 0
    for i in range(10, factorials[9] * digits + 1):
        if sum(map(lambda c:factorials[int(c)], str(i))) == i:
            print(i)
            _sum += i
    print(_sum)

f()
