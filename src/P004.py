'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def f():
    for i in range(100001, 1000000)[::-1]:
        string = str(i)
        if string == string[::-1]:
            for j in range(100, 1000):
                if i % j == 0:
                    r = i / j
                    if r >= 100 and r <= 999:
                        print(i)
                        return i

f()
