# Exercise 1

## Question 
What does the following code print out?

## Code 
```python
liste = ["mond", "stoff", "treib", "raum", "schiff"]
print(liste[0])
print(liste[2] + liste[1])
print(liste[-2] + liste[-1])
for wort in liste:
    if wort[0] == "s":
        print(wort)

for wort in liste:
    print(wort[1])

liste = liste + ["gestein"]
print(liste[0] + liste[-1])
```

## Answer
    >>> mond
    >>> treibstoff
    >>> raumschiff
    >>> stoff
    >>> schiff
    >>> o
    >>> t
    >>> r
    >>> a
    >>> c
    >>> mondgestein
    