'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
# -*- coding: utf-8 -*

def f(n):
    print(sumOfMultipleOfNBelowM(n, 3) + sumOfMultipleOfNBelowM(n, 5) - sumOfMultipleOfNBelowM(n, 15))

def sumOfMultipleOfNBelowM(m, n):
    # anotner arithmetic
    # return sum(range(n, m)[::n])
    times = int(m / n)
    return 0 if times == 0 else int(n * (times + 1) * times / 2)

f(1000)
