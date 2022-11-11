import random
cards = []
suits = ['spades', 'clubs', 'diamonds', 'hearts']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])
def shuffle():
    random.shuffle(cards)
def deal():
    card = cards.pop()
    return card
shuffle()
card = deal()
print(card)