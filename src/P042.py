'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values 
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common 
English words, how many are triangle words?
'''
# -*- coding: utf-8 -*

def f():
    _text = open('../data/p042_words.txt').read()
    nameArr = list(map(lambda s:s.replace("\"", "").upper(), _text.split(",")))
    
    wordValues = list(map(lambda i:sum(map(lambda c:ord(c) - 64, nameArr[i])), range(len(nameArr))))
    
    triangleNumbers = list(filter(lambda n:n <= max(wordValues), map(lambda i:i * (i + 1) // 2, range(1, 1000))))
#     print(triangleNumbers)
    
    print(len(list(filter(lambda n:n in triangleNumbers, wordValues))))

f()
