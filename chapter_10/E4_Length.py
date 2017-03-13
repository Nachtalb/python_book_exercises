class Length(object):
    __meter = {'m': 1.0, 'mil': 1609, 'yd': 0.9143, 'ft': 0.3048, ' in ': 0.0254}

    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def getMeter(self):
        return self.amount * self.__meter[self.unit]
    def __add__(self, other):
        return self.getMeter() + other.getMeter()

    def __gt__(self, other):
        return self.getMeter() > other.getMeter()

    def __ge__(self, other):
        return self.getMeter() >= other.getMeter()

    def __eq__(self, other):
        return self.getMeter() == other.getMeter()

    def __str__(self):
        return self.unit + " " + str(self.amount)
