# ---------------------------------------------------
# Dateiname: baum.py
# Rekursives Zeichnen eines Baums mit Turtle-Grafik
# Objektorientierte Programmierung mit Python 3
# Kap. 6 
# Michael Weigend Januar 2013
# ----------------------------------------------------


def baum(x):
    if x < 5:
        return  # 1
    else:
        forward(x)
        left(45)
        baum(x / 2)  # 2
        right(90)
        baum(x / 2)  # 3
        left(45)
        backward(x)  # 4
    return


left(90)  # 5
baum(100)
hideturtle()
