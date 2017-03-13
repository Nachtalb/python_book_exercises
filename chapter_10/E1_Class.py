class Ding(object):
    _density = {'Au': ('Gold', 19.32), 'Fe': ('Iron', 7.87), 'Ag': ('Silver', 10.5)}

    def __init__(self, volume, symbol):
        self.__volume = volume
        self._symbol = symbol

    def getMass(self):
        return self.__volume / self._density[self._symbol][1]

    def getVolume(self):
        return self.__volume

    def __str__(self):
        return self._symbol + "\t" + str(self._density[self._symbol][0]) + "\t" + str(self.__volume)
