from chapter_27.required._stack import Stack


def recursive_stack_length(stack):
    if stack.empty():
        return 0
    else:
        length = 0
        helping = Stack()
        while not stack.empty():
            length += 1
            helping.push(stack.pop())
            if isinstance(stack.top(), Stack):
                length += recursive_stack_length(stack.top())
        while not helping.empty():
            stack.push(helping.pop())
        return length


def stack_length(stack):
    i = 0
    helping = Stack()
    while not stack.empty():
        i += 1
        helping.push(stack.pop())
    while not stack.empty():
        stack.push(helping.pop())
    return i


s1 = Stack()
s2 = Stack()

for k in range(100):
    new = Stack()
    for l in range(k):
        new.push(l)
    s1.push(new)


for m in range(10):
    s2.push(m)

print(recursive_stack_length(s1))
print(stack_length(s1))
print(recursive_stack_length(s2))
print(stack_length(s2))
