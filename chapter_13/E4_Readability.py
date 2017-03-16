from re import *


class TextAnalyser(object):
    def __init__(self, path):
        self.path = path
        self.text = self.__read_file().replace("\n", " ")

    def analyse_text(self):
        word_amount = self.__count_words()
        asl = float(word_amount / self.__count_sentences())
        asw = float(self.__count_syllables() / word_amount)

        return int(206.835 - 1.015 * asl - 84.6 * asw)

    def __count_words(self):
        return len(self.text.split(" "))

    def __count_sentences(self):
        re = compile("[;:.!?]+")
        return len(re.split(self.text))

    def __count_syllables(self):
        re = compile("[aeiou]+", I)
        return len(re.split(self.text))

    def __read_file(self):
        try:
            f = open(self.path)
            text = f.read()
            f.close()
            return text
        except:
            print("There was an error when opening and reading file")
            return ""

    def __str__(self):
        return "The readability of the text from \"{}\" is {}".format(self.path, self.analyse_text())


# Programm start
print(TextAnalyser("./text.txt"))
