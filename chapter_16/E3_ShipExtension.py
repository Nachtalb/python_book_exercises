from tkinter import *
from tkinter import messagebox
from random import *


class Cell:
    def __init__(self, _game, x, y):
        self.x = x
        self.y = y
        self.game = _game
        self.button = Label(self.game.window, text="   ", relie="groove", width=2, bg="white")
        self.button.bind("<Button-1>", self.press)
        self.button.grid(column=x, row=y)

    # noinspection PyUnusedLocal
    def press(self, *args):
        if self.button.cget("bg") == "white":
            check = self.game.playfield.check_hit
            if check(self.x, self.y):
                self.game.score.update_score(1)
                self.button.config(bg="blue")
            else:
                self.game.score.update_score(0)
                self.button.config(bg="grey")

            all_hit = self.game.playfield.check_all()
            if all_hit:
                self.game.reset(1)


class Playfield:
    ships = [
        (4, 1),  # 4 times 1x1
        (3, 2),  # 3 times 1X2
        (2, 3),  # 2 times 1x3
        (1, 4)  # 1 time  1x4
    ]

    playfield_size = 12

    def __init__(self, game):
        self.d = {}
        self.game = game
        for i in range(self.playfield_size):
            for j in range(self.playfield_size):
                self.d[(i, j)] = 0
        for ship in self.ships:
            for k in range(ship[0]):
                self.set_boat_pos(ship[1])

    def set_boat_pos(self, length):
        _max = self.playfield_size - 1 - length
        ok = 0

        while not ok:
            if choice([0, 1]):  # vertical
                y = randint(1, self.playfield_size - 2)
                x = randint(1, _max)
                if self.check(x, y, x + length - 1, y):
                    for x in range(x, x + length):
                        self.d[(x, y)] = 1
                    ok = 1
            else:  # horizontal
                x = randint(1, self.playfield_size - 2)
                y = randint(1, _max)
                if self.check(x, y, x, y + length - 1):
                    for y in range(y, y + length):
                        self.d[(x, y)] = 1
                    ok = 1

    def check(self, x1, y1, x2, y2):
        ok = 1
        for x in range(x1 - 1, x2 + 2):
            for y in range(y1 - 1, y2 + 2):
                if self.d[x, y]:
                    ok = 0
        return ok

    def check_all(self):
        hits = 0
        for button in self.game.buttons:
            if button.button.cget("bg") == "blue":
                hits += 1
        ship_amount = 0
        for ship in self.ships:
            ship_amount += ship[0] * ship[1]

        return ship_amount == hits

    def check_hit(self, x, y):
        return self.d[x, y]


class Score:
    def __init__(self, _game):
        self.game = _game
        self.score = StringVar()
        self.score.set("0")
        self.title = Label(self.game.window, text="Score: ")
        self.scoretext = Label(self.game.window, textvariable=self.score)

        self.title.grid(row=self.game.playfield.playfield_size + 1, columnspan=2)
        self.scoretext.grid(row=self.game.playfield.playfield_size + 1, column=2)

    def update_score(self, hit=0):
        if not hit:
            self.score.set(str(int(self.score.get()) + -1))
        else:
            self.score.set(str(int(self.score.get()) + 3))


class Game:
    def __init__(self):
        self.window = Tk()
        self.reset()
        self.window.mainloop()

    def reset(self, new_game=0):
        if new_game:
            messagebox.showinfo("Finished", "You hit all enemy ships!")
        self.playfield = Playfield(self)
        self.score = Score(self)
        self.buttons = []
        for x in range(self.playfield.playfield_size):
            for y in range(self.playfield.playfield_size):
                # noinspection PyUnusedLocal
                self.buttons.append(Cell(self, x, y))



game = Game()
