'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
for example, both players have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1                    Player 2                    Winner
1               5H 5C 6S 7S KD      2C 3S 8S 8D TD       Player 2
                 Pair of Fives             Pair of Eights

2               5D 8C 9S JS AC       2C 5C 7D 8S QH     Player 1
                 Highest card Ace   Highest card Queen

3               2D 9C AS AH AC     3D 6D 7D TD QD    Player 2
                 Three Aces               Flush with Diamonds

4               4D 6S 9H QH QC     3D 6D 7H QD QS   Player 1
                 Pair of Queens         Pair of Queens
                 Highest card Nine  Highest card Seven

5               2H 2D 4C 4D 4S       3C 3D 3S 9S 9D     Player 1
                 Full House                 Full House
                With Three Fours      with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards 
and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand 
is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
# -*- coding: utf-8 -*
from collections import Counter

def f():
    _text = open('../data/p054_poker.txt').read()
    lines = list(map(lambda s:s.upper(), _text.split("\n")))
    win = 0
    for line in lines:
        if '' != line and getCardsValue(line.split(' ')[:5]) > getCardsValue(line.split(' ')[5:]):
            win += 1
    print(win)

# 用A代表10，B代表J，C代表Q，D代表K，E代表A，方便排序
allCards = '23456789ABCDE'
straights = [allCards[i:i + 5] for i in range(9)]
def getCardsValue(cards):
    '''
        0: Royal Flush，同花大顺
        1: Straight Flush，同花顺
        2: Four of a Kind，四条（铁支）
        3: Full House，俘虏
        4: Flush，同花
        5: Straight，顺子
        6: Three of a Kind，三条
        7: Two Pairs，两对
        8: One Pair，对子
        9: High Card，散牌
    '''
    value = ['00' for i in range(10)]
    value[7] = '000'
    value[8] = '000'
    isFlush = len(set(map(lambda card:card[1], cards))) == 1  # 同花
    cardsStr = ''.join(sorted(list(map(lambda card:card[0].upper()\
                                       .replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A'), cards))))
    isStraight = cardsStr in straights
    if isFlush:
        value[4] = '1' + cardsStr[4]
        if isStraight:
            value[1] = '1' + cardsStr[4]
            if cardsStr == straights[8]:
                value[0] = '11'
    elif isStraight:
        value[5] = '1' + cardsStr[4]
    else:
        c = Counter(cardsStr)
        cs = c.most_common(3)
        for i in range(len(cs)):
            if cs[0][1] == 4:
                value[2] = '1' + cs[0][0]
            elif cs[0][1] == 3:
                if cs[1][1] == 2:
                    value[3] = '1' + cs[0][0]
                else:
                    value[6] = '1' + cs[0][0]
            elif cs[0][1] == 2:
                if cs[1][1] == 2:
                    value[7] = '1' + max(cs[0][0], cs[1][0]) + min(cs[0][0], cs[1][0])
                else:
                    value[8] = '1' + cs[0][0] + cardsStr.replace(cs[0][0], '')[2]
            else:
                value[9] = '1' + cardsStr[4]
    
    return ''.join(value)

f()
