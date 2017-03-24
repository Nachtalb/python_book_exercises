from chapter_27.required._stack import Stack

s1 = Stack()
s2 = Stack()

# fill stack s1
for i in range(10):
    s1.push(i)

# reverse stack s1 to s2 and print top s2, which was top s1
while not s1.empty():
    s2.push(s1.pop())
    print(s2.top())

# save s2 as s1, so s1 is reversed
s1 = s2

print("-" * 10)
# print reversed s1
helping = Stack()
while not s1.empty():
    print(s1.pop())

# save s2 as s1 again so s1 is reset
s1 = s2
