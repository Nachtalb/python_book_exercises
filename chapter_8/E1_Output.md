# Exercise 1

## Question 
What does the following code print out

## Code
```python
d = {'E260' : 'Essigsäure', 'E200' : 'Sorbinsäure', 'E210' : 'Benzosäure'}

print(d['E210'])

print(list(d.keys()))

del d['E210']
print(list(d.values()))

for k in d.keys():
    print(k+ ': '+d[k])

d['E239'] = 'Kaliumnitrit'
for k in d.keys(): print(k)
```

## Answer
    >>> "Benzosäure"
    
    >>> ['E260', 'E200', 'E210']
    
    >>> ['Essigsäure', 'Sorbinsäure']
    
    >>> 'E260: Essigsäure'
    >>> 'E200: Sorbinsäure'
    
    >>> 'E260'
    >>> 'E200'
    >>> 'E239'