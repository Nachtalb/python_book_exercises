from threading import *
from tkinter import *
from time import *
from random import *


class Space(object):
    meteorites = []
    winner = []

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width='10c',
                             height='7c', bg='black')
        self.canvas.pack()
        self.ship = None

        self.m = [PhotoImage(file='assets/metgross.gif'), PhotoImage(file='assets/metklein.gif')]

        self.load()

        self.window.mainloop()

    def load(self, *args):
        self.canvas.delete("all")
        for i in range(8):
            self.add_metorite(only_small=True)

        self.add_metorite(winner=True, only_big=True, x=250, y=95)

        self.ship = Spaceship(self)
        self.ship.start()

        self.window.bind("<space>", self.load)

    def add_metorite(self, winner=False, only_big=False, only_small=False, x=-1, y=-1):
        if x == -1:
            x = randint(0, 250)

        if y == -1:
            y = randint(0, 190)

        if only_big and not only_small:
            meteorite = self.m[0]
        elif only_small and not only_big:
            meteorite = self.m[1]
        else:
            meteorite = choice(self.m)

        if winner:
            self.winner.append(self.canvas.create_image(x, y, image=meteorite))
        else:
            self.meteorites.append(self.canvas.create_image(x, y, image=meteorite))

    def collide(self, x, y, winner=False):
        if winner:
            check = self.winner
        else:
            check = self.meteorites

        for checker in check:
            try:
                if checker in self.canvas.find_overlapping(x - 20, y - 5, x + 0, y + 5):
                    return True
            except:
                pass
        return False

    def message(self, loose=True):
        if loose:
            message = "Game Over"
        else:
            message = "You Won!!"
        self.canvas.create_text(self.window.winfo_width() / 2, self.window.winfo_height() / 3, text=message, font=("Courier New", 20), fill="White")


class Spaceship(Thread):
    def __init__(self, space):
        Thread.__init__(self)
        self.space = space

        self.image = PhotoImage(file="assets/schiff.gif")
        self.x = 0.0
        self.y = 95.0
        self.vx = 0.0
        self.vy = 0.0
        self.ship = self.space.canvas.create_image(self.x, self.y, image=self.image)
        self.space.window.bind("<Any-KeyPress>", self.move)

    def run(self):
        while not self.space.collide(self.x, self.y):
            sleep(0.1)
            self.x += self.vx
            self.y += self.vy
            self.space.canvas.move(self.ship, self.vx, self.vy)

            if self.space.collide(self.x, self.y, True):
                self.space.message(False)
                return

            if self.vx >= 0.5 or self.vx <= -0.5:
                self.vx = self.vx * .9
            else:
                self.vx = 0
            if self.vy >= 0.5 or self.vy <= -0.5:
                self.vy = self.vy * .9
            else:
                self.vy = 0
        self.space.message()

    def move(self, event):
        if event.keysym_num == 65362:
            self.vy -= 0.5  # Up
        elif event.keysym_num == 65364:
            self.vy += 0.5  # Down
        elif event.keysym_num == 65363:
            self.vx += 0.5  # Right
        elif event.keysym_num == 65361:
            self.vx -= 0.5  # Left


w = Space()
