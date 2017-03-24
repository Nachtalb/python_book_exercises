# ----------------------------------------------------
# Dateiname: bankleitzahl.py
# Suche nach Bankleitzahl in einem Text
#
# Python 3, 6. Auflage mitp 2016
# Kap. 13
# Michael Weigend 20.8.2016
# ----------------------------------------------------
from re import *


def blzcheck(email):
    re = compile('(Bankleitzahl|BLZ):?\s*\d+', I)  # 1
    if re.search(email):  # 2
        return 'Danke für die Konto-Angabe.'
    else:
        return 'Leider fehlt die Bankleitzahl!'


email1 = """Hallo, hier ist meine Kontonummer:
SSK Bonn Kto-Nr. 443443525. MfG T."""

email2 = """Hallo,
bitte überweisen Sie das Honorar auf folgendes Konto:
Sparkasse Witten BLZ 45250035, Kontonr. 1234567. Gruß M."""

print(blzcheck(email1))
print(blzcheck(email2))

input('Beenden mit <ENTER>')
