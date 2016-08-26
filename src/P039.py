'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions 
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
# -*- coding: utf-8 -*

def f(p):
    numberOfSolutionsDict = {i: 0 for i in range(5, p)}
    # a < b < c
    maxp = 0
    maxNumber = 0
    for n in range(5, p):
        for a in range(1, n // 3 + 1):
            # a^2 + b^2 = (n - a - b)^2 ---> b = n * (n - 2 * a) / (2 * (n - a))
            if n * (n - 2 * a) % (2 * (n - a)) == 0:
                numberOfSolutionsDict[n] += 1
        if numberOfSolutionsDict[n] > maxNumber:
            maxp = n
            maxNumber = numberOfSolutionsDict[n]
    print(maxp)

f(1000)
