# Exercise 1

## Question 
What do the values s1, s2 and s3 after you run this code?

## Code 
```python
s1 = [1]
s1 = [1, s1]
s1 = [1, s1]

A = ["Haus", "Garten"]
B = ["bau", "tier", "pflanze"]
s2 = [i+j for i in A for j in B]

A = [1, 2, 3, 4]
B = [2, 3, 4, 5]
s3 = [i for i in A+B if ( i not in A) or ( i not in B )]

```

## Answer
    s1 = [1, [1, [1]]]
    s2 = ["Hausbau", "Haustier", "Hauspflanze", "Gartenbau", "Gartentier", "Gartenbau"]
    s3 = [1, 5]
