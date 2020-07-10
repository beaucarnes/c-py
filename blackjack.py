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
    card = cards.pop()
    return cards_delt

shuffle()
cards_delt = deal(2)
print(cards_delt)