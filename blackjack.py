import random

cards = []
suits = ["spades", "clubs", "hearts", "diamonds"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_delt = []
    for x in range(number):
        card = cards.pop()
        cards_delt.append(card)
    return cards_delt

shuffle()
cards_delt = deal(2)
print(cards_delt)