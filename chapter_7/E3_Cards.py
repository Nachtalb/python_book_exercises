import random

types = ["Hearts", "Spades", "Diamonds", "Clubs"]
subtypes = ["Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven"]

cards = [(i, j) for i in types for j in subtypes]
print(cards)

numberToMix = random.randint(20, 40)
for i in range(numberToMix):
    card1 = random.randint(0, 31)
    card2 = random.randint(0, 31)
    cards[card1], cards[card2] = cards[card2], cards[card1]

print(cards)
