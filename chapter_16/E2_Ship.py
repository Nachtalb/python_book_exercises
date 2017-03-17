from tkinter import *
from random import *


class Cell:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.button = Label(self.game.window, text="   ", relie="groove", width=2)
        self.button.bind("<Button-1>", self.press)
        self.button.grid(column=x, row=y)

    def press(self, *args):
        check = self.game.playfield.checkHit
        if check(self.x, self.y):
            self.button.config(bg="blue")
        else:
            self.button.config(bg="grey")


class Playfield:
    ships = [
        (4, 1),  # 4 times 1x1
        (3, 2),  # 3 times 1X2
        (2, 3),  # 2 times 1x3
        (1, 4)  # 1 time  1x4
    ]

    playfield_size = 12

    def __init__(self):
        self.d = {}
        for i in range(self.playfield_size):
            for j in range(self.playfield_size):
                self.d[(i, j)] = 0
        for ship in self.ships:
            for k in range(ship[0]): self.setBoatPos(ship[1])

    def setBoatPos(self, length):
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

    def checkHit(self, x, y):
        return self.d[x, y]


class Game:
    def __init__(self):
        self.window = Tk()
        self.playfield = Playfield()
        for x in range(self.playfield.playfield_size):
            for y in range(self.playfield.playfield_size):
                button = Cell(self, x, y)
        self.window.mainloop()


game = Game()
