'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def f():
    '''
    常见的勾股数公式有：
    1、3n、4n、5n
    2、2n + 1、2n^2 + 2n、2n^2 + 2n + 1
    3、4(n + 1)、4(n + 1)^2 - 1、4(n + 1)^2 + 1
    4、m^2 - n^2、2mn、m^2 + n^2
    由于a + b + c = 1000 = 2^3 * 5^3，根据以上公式求解只有公式4有解，m=20, n=5, a=375, b=200, c=425
    '''
    print(375 * 200 * 425)

f()
