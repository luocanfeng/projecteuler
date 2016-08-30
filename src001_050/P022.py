'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
# -*- coding: utf-8 -*

def f():
    _text = open('../data/p022_names.txt').read()
    nameArr = list(map(lambda s:s.replace("\"", "").upper(), _text.split(",")))
    nameArr.sort()
    
    print(sum(map(lambda i:sum(map(lambda c:ord(c) - 64, nameArr[i])) * (i + 1), range(len(nameArr)))))

f()
