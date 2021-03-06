# ----------------------------------------------------
# Dateiname:  kap32_aufgabe2.py
# Das Programm sucht einige 14-stellige Primzahlen
# in parallelen Prozessen und dokumentiert den Zeitbedarf.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 32
# Michael Weigend 24.10.2016
# ----------------------------------------------------
from math import ceil, sqrt
from multiprocessing import Pool
from random import randint
from time import time


def prime(n):
    """ Prüft, ob die Zahl n eine Primzahl ist
        >>> prime(7)
        True
        >>> prime(8)
        False
    """
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    N = 200
    big_numbers = [randint(10 ** 13, 10 ** 14) for i in range(N)]
    start = time()
    p = Pool()
    result = p.map(prime, big_numbers)
    p.close()
    p.join()
    seconds = time() - start
    primes = [big_numbers[i]
              for i in range(N) if result[i]]
    print("Gefundene Primzahlen:")
    for pr in primes:
        print(pr)
    print("Bearbeitungszeit: %f Sekunden" % seconds)
