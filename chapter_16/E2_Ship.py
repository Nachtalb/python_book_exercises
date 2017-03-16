from tkinter import *
from random import randint


class App:
    ships = [
        (4, 1),  # 4 times 1x1
        (3, 2),  # 3 times 1X2
        (2, 3),  # 2 times 1x3
        (1, 4)  # 1 time  1x4
    ]

    playfield_size = (12, 12)

    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x400")

        self.playfield = [[0 for y in range(self.playfield_size[0])] for x in range(self.playfield_size[1])]

        self.ship_positions = {}

        #self.generate_ships()

    def reset(self):
        # self.result.config(text="")
        pass

    def pack(self):
        # self.leftSide.pack(side=LEFT, fill=Y)
        # self.rightSide.pack(side=RIGHT, fill=Y)
        # self.scale.pack(fill=X)
        # self.check.pack()
        # self.reset.pack()
        # self.result.pack()
        pass

    def generate_ships(self):
        for i, ship in enumerate(self.ships):
            self.ship_positions[i] = ""
            while self.ship_positions[i] == "":
                horizontal = randint(0, 1)
                if horizontal:
                    start_position = (randint(0, self.playfield_size[0] - ship[1]), randint(0, self.playfield_size[1]))
                else:
                    start_position = (randint(0, self.playfield_size[0]), randint(0, self.playfield_size[1] - ship[1]))

                test = True
                temp_position = []
                try:
                    if horizontal:
                        for j in range(ship[1]):
                            if self.playfield[start_position[0]][start_position[1] + j] == 0:
                                temp_position[j] = (start_position[0], start_position[1] + j)
                            else:
                                test = False
                        if test:
                            self.ship_positions[i] = [temp_position]
                        print(temp_position)

                    else:
                        for j in range(ship[1]):
                            if self.playfield[start_position[0 + j]][start_position[1]] == 0:
                                temp_position[j] = (start_position[0] + j, start_position[1])
                            else:
                                test = False
                        if test:
                            self.ship_positions[i] = [temp_position]
                        print(temp_position)
                except:
                    print(start_position)
                    pass
        for ship in self.ship_positions:
            self.playfield[ship[0]][ship[1]] = 1

    def __str__(self):
        text = ""
        for idx, x in enumerate(self.playfield):
            text += str(idx) + " " + str(x) + "\n"
        return text


app = App()
print(app)
app.generate_ships()
print(app)
