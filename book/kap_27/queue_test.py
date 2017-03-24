# ----------------------------------------------------
# Dateiname:  queue_test.py
# Simulation eines Producer-Consumer-Systems
# 
# Objektorientierte Programmierung mit Python
# Kapitel 27
# Michael Weigend 19. 11. 2009
# ----------------------------------------------------
# queue_test.py
from queue_ import Queue

q = Queue()

for i in range(5):
    q.enqueue(i)

while not q.empty():
    item = q.dequeue()
    print(item, end=" ")
