'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''
# -*- coding: utf-8 -*

def f(n):
    candidates = [200, 100, 50, 20, 10, 5, 2, 1]
    print(ways(n, candidates))

def ways(n, candidates):
    candidate = candidates[0]
    times = n // candidate
    if len(candidates) == 2:
        return times + 1
    
    count = 0
    for i in range(times + 1)[::-1]:
        remainder = n - candidate * i
        if remainder == 0:
            count += 1
        else:
            count += ways(remainder, candidates[1:len(candidates)])
    return count

f(200)
