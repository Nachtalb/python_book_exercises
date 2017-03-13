# Extend Cancel of Events

## Description 
Extend the musical class to be able to cancel an event,<br>

## Code / Answer
```python
def storniere(self, datum):
    """Storniere eine Vorstellung"""
    vorstellung = self.getVorstellung(datum)
    if not vorstellung:
        return "Keine Vorstellung gefunden"
    else:
        text = "Die Vorstellung am " + vorstellung.datum + " um " + vorstellung.beginn + " wird ausfallen." \
            " Sie können die Zuschauer mit den Folgenden Daten kontaktieren:"
        for zuschauer in vorstellung.getZuschauer():
            text += "\n* Name: " + zuschauer.name + "\t\tTelefonNr.: " + zuschauer.tel
        self.vorstellungen.remove(vorstellung)
        return text
    pass
```

## Example use
```
Die Vorstellung am 1. 10. 2010 um 20.00 Uhr wird ausfallen. Sie können die Zuschauer mit den Folgenden Daten kontaktieren:
 * Name: Müller		TelefonNr.: 22323432
 * Name: Schmidt		TelefonNr.: 02303 89917
 * Name: Schmidt		TelefonNr.: 02303 89917
 * Name: Kastens		TelefonNr.: 02305234
 * Name: Kastens		TelefonNr.: 02305234
 * Name: Meyer		TelefonNr.: 02334 5005
 * Name: Meyer		TelefonNr.: 02334 5005
 * Name: Nick		TelefonNr.: 078
 * Name: Nick		TelefonNr.: 078
 * Name: Nick		TelefonNr.: 078
 * Name: Nick		TelefonNr.: 078
```