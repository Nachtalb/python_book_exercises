# log_test_3.py
import logging

logging.basicConfig(filename="tmp/logging.txt",
                    level=logging.DEBUG,
                    format='%(module)s, Zeile %(lineno)d: %(message)s')
for i in range(4):
    logging.debug("Meldung {}.".format(i))
