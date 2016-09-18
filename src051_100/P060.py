'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them 
in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
# -*- coding: utf-8 -*
import Primes
import time

def f():
    startTime = time.time()
    
    primes = set(Primes.getPrimes(100000000))
    print("Get primes under 100M cost %.3fs." % (time.time() - startTime))
    
    primes1w = Primes.getPrimes(50000)
    primes1w.remove(2)
    primes1w.remove(5)
    
#     print(len(primes1w))
    
    tuples2 = []
    for p1 in primes1w:
        larger = list(filter(lambda p: p > p1, primes1w))
        for p2 in larger:
            if int(''.join([str(p1), str(p2)])) in primes and int(''.join([str(p2), str(p1)])) in primes:
                tuples2.append((p1, p2))
#     print(len(tuples2))
    
    dict1 = {}
    for p1, p2 in tuples2:
        if p1 in dict1.keys():
            dict1[p1].append(p2)
        else:
            dict1[p1] = [p2]
        if p2 in dict1.keys():
            dict1[p2].append(p1)
        else:
            dict1[p2] = [p1]

    # 1 -> 4+
    while True:
        flag = False
        keys = [k1 for k1, v in dict1.items() if len(v) < 4]
        for k1 in keys:
            if len(dict1[k1]) < 4:
                dict1.pop(k1)
                for v in dict1.values():
                    if k1 in v:
                        v.remove(k1)
                        if len(v) < 4:
                            flag = True
        if not flag:
            break
#     print(dict1)

    # 2 -> 3+
    dict2 = {}
    for k1, v in dict1.items():
        for k2 in v:
            if k2 > k1:
                _list = list(filter(lambda x:x > k1 and x > k2, set(v) & set(dict1[k2])))
                if len(_list) >= 3:
                    _list.sort()
                    dict2[(k1, k2)] = _list
#     print(dict2)
    
    # 3 -> 2+
    dict3 = {}
    for (k1, k2), v in dict2.items():
        for k3 in v:
            _list = list(filter(lambda x:x > k1 and x > k2 and x > k3, set(v) & set(dict1[(k3)])))
            if len(_list) >= 2:
                _list.sort()
                dict3[(k1, k2, k3)] = _list
#     print(dict3)
    
    # 4 -> 1+
    dict4 = {}
    tuples = []
    for (k1, k2, k3), v in dict3.items():
        for k4 in v:
            _list = list(filter(lambda x:x > k1 and x > k2 and x > k3 and x > k4, set(v) & set(dict1[(k4)])))
            if len(_list) >= 1:
                _list.sort()
                dict4[(k1, k2, k3, k4)] = _list
                for k5 in _list:
                    _list = [k1, k2, k3, k4, k5]
                    _tuple = tuple(_list)
                    tuples.append(_tuple)
#     print(tuples)
    print(min(map(lambda t:sum(t), tuples)))
    endTime = time.time()
    print("Totally cost %.3fs." % (endTime - startTime))

f()
