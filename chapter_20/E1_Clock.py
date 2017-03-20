from _thread import *
from tkinter import *
from time import *


class Clock:
    def __init__(self):
        self.window = Tk()
        self.time = StringVar()
        self.clock = Label(self.window, textvariable=self.time)
        self.clock.pack()

        start_new_thread(self.update, ())
        self.window.mainloop()

    def update(self):
        while True:
            self.time.set(strftime("%X"))
            sleep(1)

clock = Clock()
