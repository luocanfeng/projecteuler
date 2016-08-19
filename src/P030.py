'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def f():
    _sum = 0
    
    digits = 1
    while True:
        if (9 ** 5) * digits < 10 ** (digits - 1)  :
            digits -= 1
            break
        else:
            digits += 1
    print(digits)
    
    stop = 10 ** digits
    for n in range(2, stop):
        if n == sum(map(lambda x:int(x) ** 5, str(n))):
            _sum += n
    print(_sum)

f()
