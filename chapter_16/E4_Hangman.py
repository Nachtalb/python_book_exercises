from tkinter import *
from random import *
import re


class Game:
    def __init__(self):
        self.window = Tk()
        self.hangman = Hangman(self)
        self.gui = Gui(self)
        self.hangman.post_init()
        self.window.mainloop()

class Hangman:
    wordlist = {"de": "", "en": ""}

    def __init__(self, _game):
        self.game = _game
        self.gui = None
        self.__read_files()
        self.word = ""

    def new_word(self, reset_score=TRUE):
        if reset_score:
            self.gui.update_score(0)

        lang = self.gui.language.get()
        self.word = choice(self.wordlist.get(lang))
        self.gui.hangman_text.set("-" * len(self.word))
        print(self.word)

    def check_word(self):
        letter = self.gui.entry_text.get()

        if letter != "" and letter in self.word:
            idxs = [m.start() for m in re.finditer(letter, self.word)]
            hangman_word = self.gui.hangman_text.get()
            for idx in idxs:
                hangman_word = hangman_word[:idx] + letter + hangman_word[idx + 1:]

            self.gui.hangman_text.set(hangman_word)

            if hangman_word == self.word:
                self.new_word(False)
                self.gui.update_score(5)
                self.gui.entry_text.set("")
                return

            self.gui.update_score(1)
        else:
            self.gui.update_score(-1)

        self.gui.entry_text.set("")

    def __read_files(self):
        de = open("./data/germanText.txt")
        en = open("./data/englishText.txt")

        reg = re.compile('([?!,.:;\\-\\)]\s|\s\()', re.I)
        de_text = reg.sub(" ", de.read()).lower().split(" ")
        en_text = reg.sub(" ", en.read()).lower().split(" ")

        self.wordlist["de"] = de_text
        self.wordlist["en"] = en_text

        de.close()
        en.close()

    def post_init(self):
        self.gui = self.game.gui
        self.new_word()

    def change_lang(self):
        pass


class Gui:
    def __init__(self, _game, ):
        self.score_text = StringVar()
        self.score_text.set("0")

        self.hangman_text = StringVar()
        self.hangman_text.set("")

        self.entry_text = StringVar()
        self.language = StringVar()

        self.title = Label(_game.window, text="Hangman", font=("Verdana", 20))
        self.score = Label(_game.window, textvariable=self.score_text, font=("Verdana", 20))
        self.hangman_text_label = Label(_game.window, textvariable=self.hangman_text, bg="lightgrey",
                                        font=("Verdana", 20))
        self.language_frame = Frame(_game.window)
        self.german = Radiobutton(self.language_frame, text="German", value="de", variable=self.language,
                                  command=_game.hangman.change_lang)
        self.english = Radiobutton(self.language_frame, text="English", value="en", variable=self.language,
                                   command=_game.hangman.change_lang)
        self.new = Button(_game.window, text="New", command=_game.hangman.new_word)
        self.entry = Entry(_game.window, textvariable=self.entry_text)
        self.ok = Button(_game.window, text="Ok", command=_game.hangman.check_word)

        self.german.select()

        self.entry.bind("<KeyRelease>", self.only_one_letter)

        self.title.grid(row=0, column=0, columnspan=4)
        self.score.grid(row=0, column=3)
        self.hangman_text_label.grid(row=2, column=0, columnspan=4, sticky=N + E + S + W)
        self.language_frame.grid(row=3, column=0)
        self.german.grid(row=0, column=0)
        self.english.grid(row=1, column=0)
        self.new.grid(row=3, column=1)
        self.entry.grid(row=3, column=2)
        self.ok.grid(row=3, column=3)

    def update_score(self, amount):
        if not amount:
            self.score_text.set("15")
            return
        score = int(self.score_text.get())
        score += amount
        self.score_text.set(str(score))

    def only_one_letter(self, *args):
        text = self.entry_text.get()
        if len(text) > 1:
            self.entry_text.set(text[:1])
        elif text.isnumeric():
            self.entry_text.set("")


game = Game()
