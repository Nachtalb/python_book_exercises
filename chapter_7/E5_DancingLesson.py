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
