# Exercise 1

## Question 
There are 4 women, 4 men and one dance teacher in the lesson. How much dancingpairs are possible if every pair has to
contain 1 woman and 1 man. The teacher can play the role of a man or a woman. 

## Code / Answer 
```python
women = set("ABCD")
men = set("abcd")
teacher = set("X")

pairs = set((w, m)
            for w in women|teacher
            for m in men|teacher
            if w != m
            )

for p in pairs:
    print(p, end=" ")
```

## Output
    ('B', 'd') ('A', 'a') ('C', 'a') ('X', 'c') ('D', 'b') ('D', 'a') ('B', 'a') ('B', 'X') ('A', 'd') ('B', 'b') ('C', 'd') ('X', 'b') ('A', 'X') ('C', 'X') ('D', 'd') ('A', 'c') ('C', 'c') ('X', 'a') ('D', 'X') ('D', 'c') ('B', 'c') ('A', 'b') ('C', 'b') ('X', 'd') 

