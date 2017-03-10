# Exercise 1

## Question 
Find all triangles with a 90° angle which edges lengths added together are 20 or less (has to be integers, no floating point numbers )

## Code / Answer 
```python
triangels = set((a, b, c)
                for a in range(1, 20)
                for b in range(1, 20)
                for c in range(1, 20)
                if a ** 2 + b ** 2 == c ** 2
                )
print(triangels)
```

## Output
    {(5, 12, 13), (4, 3, 5), (8, 15, 17), (15, 8, 17), (9, 12, 15), (12, 5, 13), (12, 9, 15), (3, 4, 5), (8, 6, 10), (6, 8, 10)}
