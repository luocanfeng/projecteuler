'''
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) 
numbers and are generated by the following formulae:

Triangle                P(3,n)=n(n+1)/2           1, 3, 6, 10, 15, ...
Square                  P(4,n)=n^2                   1, 4, 9, 16, 25, ...
Pentagonal          P(5,n)=n(3n−1)/2         1, 5, 12, 22, 35, ...
Hexagonal           P(6,n)=n(2n−1)             1, 6, 15, 28, 45, ...
Heptagonal         P(7,n)=n(5n−3)/2         1, 7, 18, 34, 55, ...
Octagonal            P(8,n)=n(3n−2)            1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

1、The set is cyclic, in that the last two digits of each number is the first two digits of the next number 
(including the last number with the first).
2、Each polygonal type: triangle (P(3,127)=8128), square (P(4,91)=8281), and pentagonal (P(5,44)=2882), 
is represented by a different number in the set.
3、This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, 
square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''
# -*- coding: utf-8 -*

def f():
    ps = []
    ps.append(list(filter(lambda x:x >= 1000 and x < 10000, map(lambda n:n * (n + 1) // 2, range(1, 10000)))))
    ps.append(list(filter(lambda x:x >= 1000 and x < 10000, map(lambda n:n * n, range(1, 10000)))))
    ps.append(list(filter(lambda x:x >= 1000 and x < 10000, map(lambda n:n * (3 * n - 1) // 2, range(1, 10000)))))
    ps.append(list(filter(lambda x:x >= 1000 and x < 10000, map(lambda n:n * (2 * n - 1), range(1, 10000)))))
    ps.append(list(filter(lambda x:x >= 1000 and x < 10000, map(lambda n:n * (5 * n - 3) // 2, range(1, 10000)))))
    ps.append(list(filter(lambda x:x >= 1000 and x < 10000, map(lambda n:n * (3 * n - 2), range(1, 10000)))))

    results = []
    indexLeft = range(6)
    
    for p1 in ps[5]:
        _indexLeft = list(indexLeft)
        _indexLeft.remove(5)
        dfs(results, ps, _indexLeft, [p1])
    print(results)
    print(min(map(sum, results)))

def dfs(results, ps, indexLeft, currentResult):
    currentP = currentResult[len(currentResult) - 1]
    for idx in indexLeft:
        for nextP in ps[idx]:
            if currentP % 100 == nextP // 100:
                _currentResult = list(currentResult)
                _currentResult.append(nextP)
                if len(_currentResult) == 6:
                    if nextP % 100 == _currentResult[0] // 100:
                        results.append(_currentResult)
                else:
                    _indexLeft = list(indexLeft)
                    _indexLeft.remove(idx)
                    dfs(results, ps, _indexLeft, _currentResult)

f()
