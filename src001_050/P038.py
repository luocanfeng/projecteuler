'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer 
with (1,2, ... , n) where n > 1?
'''
# -*- coding: utf-8 -*

def f():
    pandigitals = set([918273645])
    
    # 9 * (1,2,3,4) product 918273645
    # 9* * (1,2,3,4) will product 2+3+3+3=11(digits)
    # 9** * (1,2,3) will product 3+4+4=11(digits)
    # 9*** * (1,2) will product 4+5=9(digits)
    for d in range(9182, 9876 + 1)[::-1]:
        if len(set(str(d) + str(d * 2)) & set(map(str, range(1, 10)))) == 9:
            pandigitals.add(int(str(d) + str(d * 2)))
    
    # print(pandigitals)
    print(max(pandigitals))

f()
