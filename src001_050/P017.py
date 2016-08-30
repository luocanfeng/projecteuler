'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''
# -*- coding: utf-8 -*

def f():
    # 1-19, one two three four five six seven eight nine ten
    # eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
    d19 = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # 10-90, ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    d90 = [3, 6, 6, 5, 5, 5, 7, 6, 6]
    # 100, hundred
    d100 = 7
    # 1000, thousand
    d1000 = 8
    # and
    d_and = 3
    
    sum9 = sum(d19[0:9])  # 1-9
    sum10_19 = sum(d19[9:19])  # 10-19
    sum99 = sum9 * 9 + sum10_19 + sum(d90[1:9]) * 10  # 1-99
    sum999 = sum9 * 100 + d100 * 900 + d_and * (900 - 9) + sum99 * 10  # 1-999
    sum1000 = sum999 + d19[0] + d1000  # 1000
    print(sum1000)

f()
