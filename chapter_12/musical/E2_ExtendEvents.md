# Extend Events Class

## Description 
Extend the events class (Vorstellungen) in musical.py with a method which gives you all a list
with the whole audience. The name must be "getZuschauer()"<br>

## Code / Answer
```python
def getZuschauer(self):
    """Liefert eine liste aller Zuschauer"""
    zuschauerliste = []
    for reihe in self.saalbelegung.belegung:
        for platz in reihe:
            if platz.belegt():
                zuschauerliste += [platz.zuschauer]
    return zuschauerliste
```

## Example use
``
<musical.Zuschauer object at 0x101aa09b0>
<musical.Zuschauer object at 0x101aa0a90>
<musical.Zuschauer object at 0x101aa0a90>
<musical.Zuschauer object at 0x101aa0c88>
<musical.Zuschauer object at 0x101aa0c88>
<musical.Zuschauer object at 0x101aa0da0>
<musical.Zuschauer object at 0x101a`a0da0>
<chapter_12.musical.musical.Zuschauer object at 0x101aa8080>
<chapter_12.musical.musical.Zuschauer object at 0x101aa8080>
<chapter_12.musical.musical.Zuschauer object at 0x101aa8080>
<chapter_12.musical.musical.Zuschauer object at 0x101aa8080>
```