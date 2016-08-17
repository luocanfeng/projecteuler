'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
import GetPrimes

def f(n):
    sqrt = int(math.sqrt(n))
    primes = GetPrimes.getPrimes(sqrt)
    print(primes)

    primes.reverse()
    for prime in primes:
        if n % prime == 0:
            print(prime)
            return prime

f(600851475143)
