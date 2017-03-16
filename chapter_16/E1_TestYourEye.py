from tkinter import *
from random import randint


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("720x480")

        self.rand_colour = 0
        self.user_colour = 0

        self.leftSide = Label(self.window, width=10)
        self.rightSide = Label(self.window, width=10)
        self.scale = Scale(self.window, command=self.set_right_colour, from_=0, to=255, orient=HORIZONTAL)
        self.check = Button(self.window, command=self.check_colours, text="Check")
        self.reset = Button(self.window, command=self.reset, text="Reset")
        self.result = Label(self.window)

        self.set_left_colour()
        self.pack()

        self.window.mainloop()

    def reset(self):
        self.set_left_colour()
        self.set_right_colour()
        self.result.config(text="")

    def set_left_colour(self):
        self.rand_colour = randint(0, 255)
        rcolour = "#{c:02x}{c:02x}{c:02x}".format(c=self.rand_colour)
        self.leftSide.config(bg=rcolour)

    def set_right_colour(self, newcolour=255):
        self.user_colour = int(newcolour)
        colour = "#{c:02x}{c:02x}{c:02x}".format(c=self.user_colour)
        self.rightSide.config(bg=colour)

    def pack(self):
        self.leftSide.pack(side=LEFT, fill=Y)
        self.rightSide.pack(side=RIGHT, fill=Y)
        self.scale.pack(fill=X)
        self.check.pack()
        self.reset.pack()
        self.result.pack()

    def check_colours(self):
        if self.user_colour > self.rand_colour:
            message = "Too bright"
        elif self.user_colour < self.rand_colour:
            message = "Too dark"
        else:
            message = "Perfect"
        self.result.config(text=message)

App()
