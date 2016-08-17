'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import GetPrimes

def f(n):
    primes = GetPrimes.getPrimes(n)
    sum99 = 0
    for prime in  primes:
        sum99 += prime
    print(sum99)

f(2000000)
