# Exercise 1

## Question 
Create a set of tuples with all playcards (Hearts, Spades, Diamonds, Clubs with each contain Ace, King, Queen, Jack, 
Ten, Nine, Eight, Seven).

After you created them automatically, mix them up and print the tuples out. 

## Code / Answer
```python
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
```

## Output
    [('Hearts', 'Ace'), ('Hearts', 'King'), ('Hearts', 'Queen'), ('Hearts', 'Jack'), ('Hearts', 'Ten'), ('Hearts', 'Nine'), ('Hearts', 'Eight'), ('Hearts', 'Seven'), ('Spades', 'Ace'), ('Spades', 'King'), ('Spades', 'Queen'), ('Spades', 'Jack'), ('Spades', 'Ten'), ('Spades', 'Nine'), ('Spades', 'Eight'), ('Spades', 'Seven'), ('Diamonds', 'Ace'), ('Diamonds', 'King'), ('Diamonds', 'Queen'), ('Diamonds', 'Jack'), ('Diamonds', 'Ten'), ('Diamonds', 'Nine'), ('Diamonds', 'Eight'), ('Diamonds', 'Seven'), ('Clubs', 'Ace'), ('Clubs', 'King'), ('Clubs', 'Queen'), ('Clubs', 'Jack'), ('Clubs', 'Ten'), ('Clubs', 'Nine'), ('Clubs', 'Eight'), ('Clubs', 'Seven')]
    [('Diamonds', 'Ace'), ('Diamonds', 'Nine'), ('Hearts', 'Ace'), ('Hearts', 'Jack'), ('Diamonds', 'Eight'), ('Hearts', 'Nine'), ('Hearts', 'Queen'), ('Hearts', 'Seven'), ('Spades', 'King'), ('Diamonds', 'Queen'), ('Diamonds', 'Jack'), ('Hearts', 'Eight'), ('Hearts', 'King'), ('Spades', 'Nine'), ('Hearts', 'Ten'), ('Clubs', 'Nine'), ('Spades', 'Eight'), ('Clubs', 'Seven'), ('Clubs', 'Ten'), ('Spades', 'Jack'), ('Clubs', 'Jack'), ('Diamonds', 'Ten'), ('Spades', 'Seven'), ('Clubs', 'King'), ('Clubs', 'Eight'), ('Clubs', 'Queen'), ('Diamonds', 'King'), ('Spades', 'Queen'), ('Clubs', 'Ace'), ('Spades', 'Ace'), ('Spades', 'Ten'), ('Diamonds', 'Seven')]
