#----------------------------------------------------
# Dateiname:  zeitexperiment.py
# Der Zeitbeadrf für die parallele Ausführung von
# Prozessen wird gemessen.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 32
# Michael Weigend 24.10.2016
#----------------------------------------------------
from multiprocessing import Pool
from time import time, sleep

def f(x):
    sleep(1)
    return x**2


if __name__ == '__main__':
    
    p = Pool(4)
    start = time()
    result = p.map(f, range(8))
    print(result, "Zeit parallel: ", time() - start)
    start = time()
    result = map(f, range(8))
    print(list(result), "Zeit seriell: ", time() - start)
    
