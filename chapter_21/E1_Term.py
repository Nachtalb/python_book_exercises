import math as m


def calculate(p, q):
    assert (p / 2) ** 2 - q >= 0
    x1 = -p / 2 + m.sqrt((p / 2) ** 2 - q)
    x2 = -p / 2 - m.sqrt((p / 2) ** 2 - q)
    assert (x1 ** 2 + p * x1 + q == 0) and (x2 ** 2 + p * x2 + q == 0)
    return x1, x2

