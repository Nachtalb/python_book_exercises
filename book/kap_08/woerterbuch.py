# ----------------------------------------------------
# Dateiname:  woerterbuch.py
# 
# 
# Objektorientierte Programmierung mit Python
# Kap. 8 
# Michael Weigend 15. 9. 2009
# ----------------------------------------------------
def erschaffeWoerterbuch():
    # Aufbau eines englisch-deutschen Wörterbuchs
    d = {}
    englisch = input('Englisches Wort: ')
    while englisch:  # 1
        deutsch = input('Deutsche Übersetzung: ')
        d[englisch] = deutsch
        englisch = input('Englisches Wort: ')
    return d


print(erschaffeWoerterbuch())
