'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 
66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits 
which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
# -*- coding: utf-8 -*

def f():
    cubesDict = {}
    for i in [n ** 3 for n in range(1, 10000)]:
        l = list(str(i))
        l.sort()
        s = ''.join(l)
        if s in cubesDict.keys():
            cubesDict[s].append(i)
        else:
            cubesDict[s] = [i]

    print(min([v[0] for v in cubesDict.values() if len(v) == 5]))

f()
