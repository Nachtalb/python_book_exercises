def quer(zahl):
    # Quersumme einer Zahl
    zahlstring = str(zahl)
    summe = 0
    for c in zahlstring:
        summe += int(c)
    return summe


def quersumme(*zahl):
    # Summe von Quersummen
    summe = 0
    for x in zahl:  # 1
        summe += quer(x)
    return summe
