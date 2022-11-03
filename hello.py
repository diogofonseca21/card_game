import random
import numpy as np


def checkSuite(card):
    if card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return int(card)

def SumDeck(deck):
    totalSum = 0
    for card in deck:
        totalSum += checkSuite(card)
    return totalSum

def CompareDeck(deck1, deck2):
    sum1 = SumDeck(deck1)
    sum2 = SumDeck(deck2)

    comparer = 0

    if sum1 > sum2:
        comparer = 1
    elif sum1 < sum2:
        comparer = -1
    else:
        comparer = 0

    print(str(comparer))
    return comparer



playerDeck = np.array([1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"])
compDeck = np.array([1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"])


print("The original order...")

print (playerDeck,compDeck)

print("Now the new order...")

np.random.shuffle(playerDeck)
np.random.shuffle(compDeck)
print (playerDeck,compDeck)

lasttwoplayer = playerDeck[-2:]
lasttwocomp = compDeck[-2:]

print(str(SumDeck(lasttwoplayer)))
print(str(SumDeck(lasttwocomp)))

myCompare = CompareDeck(lasttwoplayer, lasttwocomp)


#print (lasttwoplayer)
#print ("ESPACO ESPACO ESPACO ESPACO")
#print (lasttwocomp)

a = 0

""" npccard1= lasttwocomp[1]
if (npccard1 != lasttwoplayer[1])
    print("HELLO") """

