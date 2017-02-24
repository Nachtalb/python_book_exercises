#----------------------------------------------------
# Dateiname: plattform.py
# Ermittelt Python-Version und Systemplattform.
#
# Python 3, 6. Auflage, mitp 2016
# Kap. 14
# Michael Weigend 20.08.2016
#----------------------------------------------------
# plattform.py
import sys
print('Ihre Systemplattform ist',sys.platform) 
print('Python-Version:')
print('Python '+ sys.version)
if sys.version_info.major < 2:                        #1
    print('Sie benötigen für dieses Skript eine neuere Version')
else:
    print('Die Python-Version ist für dieses Skript ausreichend.')



input('Beenden mit <ENTER>')
