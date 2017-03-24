from chapter_27.required._queue import Queue

menutext = """(A)dd new customer
(P)rocess next customer
(E)nd
"""
queue = Queue()
inp = "x"
while inp is not "":
    inp = input(menutext)

    if inp in "Aa":
        queue.enqueue(input("License plate: "))
    elif inp in "Pp":
        if not queue.empty():
            print(queue.dequeue(), "processed!")
        else:
            print("Queue is empty")
    elif inp in "Ee":
        if not queue.empty():
            print("Queue is not empty yet!")
            inp = "x"
        else:
            print("bye bye")
            inp = ""
    else:
        inp = "x"
