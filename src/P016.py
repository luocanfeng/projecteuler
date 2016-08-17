'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def f():
    s = str(2 ** 1000)
    sum99 = 0
    for c in s:
        sum99 += int(c)
    print(sum99)

f()
