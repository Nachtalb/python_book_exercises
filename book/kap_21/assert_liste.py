# ----------------------------------------------------
# Dateiname:  assert_liste.py 
# Beispiel für assert-Anweisung zum Testen von Vorbedingungen
#
# Objektorientierte Programmierung mit Python 3
# Kap. 21
# Michael Weigend 25.01.2013
# ----------------------------------------------------


def entferneMin(s):
    assert type(s) == list
    assert len(s) > 0
    m = min(s)
    s.remove(m)
