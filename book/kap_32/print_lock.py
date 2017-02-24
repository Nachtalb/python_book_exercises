#----------------------------------------------------
# Dateiname:  print_lock.py
# Parallele Prozesse geben einen Text aus
# mit Synchronisation.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 32
# Michael Weigend 24.10.2016
#----------------------------------------------------
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    print ('Das ist Prozess', i)
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for i in range(4):
         Process(target=f, args=(lock, i)).start()

    
