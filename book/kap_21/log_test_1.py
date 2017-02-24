#----------------------------------------------------
# Dateiname:  log_test.py 
# Programm demonstriert einige Funktionen des Moduls logging
#
# Objektorientierte Programmierung mit Python
# Kap. 21
# Michael Weigend 3. 11. 09
#----------------------------------------------------
# log_test_1.py
import logging, sys
logging.basicConfig(file=sys.stdout)    #1

log = logging.getLogger("Modul 1")
log.setLevel(logging.INFO)
log.debug("nicht so wichtig")           #2
log.info("wichtig")

