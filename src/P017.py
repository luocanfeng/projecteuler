'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

def f():
    # 1-19, one two three four five six seven eight nine ten
    # eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
    d19 = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # 10-100, ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    d90 = [3, 6, 6, 5, 5, 5, 7, 6, 6]
    # 100, hundred
    d100 = 7
    # 1000, thousand
    d1000 = 8
    # and
    d_and = 3
    
    sum9 = 0
    for i in range(1, 10):
        sum9 += d19[i - 1]
    
    sum10_19 = 0
    for i in range(10, 20):
        sum10_19 += d19[i - 1]
    
    sum99 = sum9 + sum10_19
    for i in range(2, 10):
        sum99 += d90[i - 1] * 10 + sum9
    
    sum1000 = 0
    for i in range(10):
        if i != 0:  # 100-999
            sum1000 += (d19[i - 1] + d100 + d_and) * 100 - d_and
        sum1000 += sum99
    sum1000 += d19[0] + d1000
    print(sum1000)

f()
