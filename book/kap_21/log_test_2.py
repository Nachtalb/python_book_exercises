# ----------------------------------------------------
# Dateiname:  log_test_2.py 
# Programm demonstriert einige Funktionen des Moduls logging
#
# Objektorientierte Programmierung mit Python
# Kap. 21
# Michael Weigend 3. 11. 09
# ----------------------------------------------------

import logging

logging.basicConfig(filename="tmp/logging.txt",
                    format='%(asctime)s -> %(message)s')

logging.critical("Wassereinbruch in Laufwerk E")
