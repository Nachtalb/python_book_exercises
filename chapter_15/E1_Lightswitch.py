from tkinter import *

window = Tk()
onoff = 1

def light_switch():
    global light, onoff
    if onoff:
        light.config(text="Light on", bg="white", fg="black")
        onoff = 0
    else:
        light.config(text="Light off", bg="black", fg="white")
        onoff = 1


light = Label(window, text="Light off", width=10, height=2)
switcher = Button(window, text="0 / 1", command=light_switch)

light.pack()
switcher.pack()

window.mainloop()