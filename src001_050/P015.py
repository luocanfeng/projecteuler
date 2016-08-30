'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
# -*- coding: utf-8 -*

def f(n):
    r = [[0 for col in range(n + 1)] for row in range(n + 1)]
    for i in  range(1, n + 1):
        r[0][i] = 1
        r[i][0] = 1
        for j in range(1, i):
            r[i][j] = r[i - 1][j] + r[i][j - 1]
            r[j][i] = r[i][j]
        r[i][i] = r[i][i - 1] + r[i - 1][i]
    print(r[n][n])

f(20)
