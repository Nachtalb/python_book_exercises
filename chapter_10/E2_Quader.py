from chapter_10.E1_Class import Ding


class Quader(Ding):
    def __init__(self, symbol, length, width, height):
        Ding.__init__(self, (length * width * height), symbol)
        self.__length = length
        self.__width = width
        self.__height = height

    def __str__(self):
        return Ding.__str__(self) + "\t" + str(self.__length) + "\t" + str(self.__width) + "\t" + str(self.__height)

    def __eq__(self, other):
        return self.getMass() == other.getMass()

    def __ge__(self, other):
        return self.getMass() >= other.getMass()

    def __gt__(self, other):
        return self.getMass() > other.getMass()
