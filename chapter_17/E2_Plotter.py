from tkinter import *


class Plotter:
    def __init__(self):
        window = Tk()

        frame = Frame(window)
        frame.pack(padx=5, pady=5)

        self.term = StringVar()
        self.term.set("0")

        Label(frame, text="f(y)= ").pack(side=LEFT)

        self.entry = Entry(frame, width=12, textvariable=self.term, font=("courir", 10))
        self.entry.pack(side=LEFT)

        Button(frame, text="Plot", command=self.plot).pack(side=RIGHT, padx=5)

        self.canvas = Canvas(frame, width=160, height=160, bg="white")
        self.canvas.pack(pady=5)
        self.canvas.create_line(10, 80, 150, 80, arrow=LAST, fill="grey")
        self.canvas.create_line(80, 10, 80, 150, arrow=FIRST, fill="grey")
        self.canvas.create_text(90, 90, text="1")
        self.line = self.canvas.create_line(30, 80, 130, 80, width=2)

        window.mainloop()

    def plot(self):
        f = {}

        try:
            for x in range(-5, 6, 1):
                f[x] = 80 - 10 * eval(self.term.get())
            self.canvas.coords(self.line,
                               30, f[-5], 40, f[-4], 50, f[-3], 60, f[-2],
                               70, f[-1], 80, f[0], 90, f[1], 100, f[2],
                               110, f[3], 120, f[4], 130, f[5]
                               )
        except:
            self.term.set("Ung\xfcltig!")


p = Plotter()
