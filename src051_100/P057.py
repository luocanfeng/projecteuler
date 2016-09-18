'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, 
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''
# -*- coding: utf-8 -*

def f():
    numerator, denominator = 3, 2
    _count = 0;
    for i in range(2, 1001):
        tmp_n = numerator + denominator + denominator
        tmp_d = numerator + denominator
        numerator, denominator = tmp_n, tmp_d
        if len(str(numerator)) > len(str(denominator)):
            _count += 1
    print(_count)

f()
