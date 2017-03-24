# ----------------------------------------------------
# Dateiname:  print_no_lock.py
# Parallele Prozesse geben einen Text aus
# ohne Synchronisation.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 32
# Michael Weigend 24.10.2016
# ----------------------------------------------------
from multiprocessing import Process


def f(i):
    print('Hallo!')
    print('Das ist Prozess', i)


if __name__ == '__main__':

    for i in range(10):
        Process(target=f, args=(i,)).start()
