'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def f(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    #    while product % 10 == 0:
    #        product = int(product / 10)
    #print(product)
    
    _sum = 0
    for s in str(product):
        _sum += int(s)
    print(_sum)

f(100)
