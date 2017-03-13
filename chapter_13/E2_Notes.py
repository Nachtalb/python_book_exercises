import pickle
import re


class Note(object):
    __importantWords = [
        "important",
        "danger",
        "attention",
    ]

    def __init__(self, name, text):
        self.__name = name
        self.__text = text
        self.__priotity = self.setPriorityAuto()

    def setPriorityAuto(self):
        imp_words = "|".join(self.__importantWords)
        imp_re = re.compile("(" + imp_words + ")", re.I)

        amount_of_symboles = self.__text.count('!')
        amount_impo_words = len(imp_re.findall(self.__text))

        return amount_impo_words + amount_of_symboles

    def getName(self):
        return self.__name

    def getPriority(self):
        return self.__priotity

    def getText(self):
        return self.__text


class Pinnwall(object):
    __file = "./ntoes.dat"

    __mainMenu = """
    (A)dd new note
    (R)emove note
    (D)elete most important note
    (L)ist all nodes by priority
    : """

    __noteList = {}
ﬁ
    def __init__(self):
        print(" Welcome to your pinnwall ".center(40, "-"))
        self.readFromFile()
        menu = "x"
        while menu != "":
            menu = input(self.__mainMenu)
            if menu in ["A", "a"]:
                self.addNote()
            elif menu in ["R", "r"]:
                self.removeNote()
            elif menu in ["D", "d"]:
                self.removeNote(True)
            elif menu in ["L", "l"]:
                self.listNotes(True)

    def addNote(self):
        name = ""
        while name == "":
            name = input("Set a unique name for the note: ")
            if name in list(self.__noteList.keys()):
                name = ""
        text = input("Content: ")
        self.__noteList[name] = (Note(name, text))

        self.saveNotesToFile()

    def removeNote(self, mostImp=0):

        if mostImp:
            if len(self.__noteList) == 0:
                print("There are no notes in on your pinnwall")
            else:
                most_imp_note, most_imp_note_idx = 0, 0
                for key in list(self.__noteList.keys()):
                    priority = self.__noteList[key].getPriority()
                    if priority > most_imp_note:
                        most_imp_note_idx = key
                        most_imp_note = priority
                if most_imp_note_idx == 0:
                    most_imp_note_idx = next(iter(self.__noteList))
                if input("Are you sure you want to delete {} (y/n): ".format(
                        self.__noteList[most_imp_note_idx].getName())) in ["y", "Y"]:
                    del self.__noteList[most_imp_note_idx]
        else:
            self.listNotes(False)

            to_remove = ""
            while to_remove == "":
                to_remove = input("Which one do you want to remove: ")
                if to_remove == "":
                    to_remove = -1
                if to_remove not in list(self.__noteList.keys()):
                    to_remove = ""

            if to_remove != -1 and input(
                    "Are you sure you want to delete {} (y/n): ".format(self.__noteList[to_remove].getName())) in \
                    ["y", "Y"]:
                del self.__noteList[to_remove]

        self.saveNotesToFile()

    def listNotes(self, byImp=1):
        if len(self.__noteList) == 0:
            print("There are no notes on your pinnwall.")
        elif byImp:
            imp_list = []
            for key in list(self.__noteList.keys()):
                imp_list.append([self.__noteList[key].getPriority(), key])
            imp_list = sorted(imp_list, key=lambda x: x[0], reverse=True)
            for prio, key in imp_list:
                print("{name}: {text}".format(name=self.__noteList[key].getName(), text=self.__noteList[key].getText()))
            pass
        else:
            for key in list(self.__noteList.keys()):
                print("{name}: {text}".format(name=self.__noteList[key].getName(), text=self.__noteList[key].getText()))

    def saveNotesToFile(self):
        f = open(self.__file, "wb")
        pickle.dump(self.__noteList, f)
        f.close()

    def readFromFile(self):
        try:
            f = open(self.__file, "rb")
            self.__noteList = pickle.load(f)
            f.close()
        except:
            self.__noteList = {}


Pinnwall()
