'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

def f(n):
    r = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(0)
        r.append(arr)
    r[0][0] = 2
    r[1][0] = 3
    r[0][1] = 3
    r[1][1] = 6
    for i in range(2, n):
        # (i, 0)
        r[i][0] = r[i - 1][0] + 1
        r[0][i] = r[i][0]
        # (i, 1) -> (i, i - 1)
        for j in range(1, i):
            r[i][j] = r[i - 1][j] + r[i][j - 1]
            r[j][i] = r[i][j]
        # (i, i)
        r[i][i] = r[i][i - 1] * 2
    print(r)
    print(r[n - 1][n - 1])

f(20)
