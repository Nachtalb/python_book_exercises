from tkinter import *

window = Tk()
density = StringVar()
combustibility = StringVar()
bwb = [StringVar(), StringVar(), StringVar()]

title_font = ("Verdana", 20)

elements = {"11011": "Polyethylene (PE)", "01100": "Polystyrene (PS)",
            "00000": "Polyvinyl chloride (PVC)"}


def which_element(*args):
    global elements, elementLabel

    d = density.get()
    c = combustibility.get()
    b1, b2, b3 = bwb[0].get(), bwb[1].get(), bwb[2].get()
    code = d + c + b1 + b2 + b3

    elementLabel.config(text=elements.get(code, "Nothing"))


densityLabel = Label(window, text="Density", font=title_font, height=2)
combustibilityLabel = Label(window, text="Combustibility", font=title_font, height=2)
bwbLabel = Label(window, text="Behavior when burning", font=title_font, height=2)
elementLabel = Label(window, text="It is ...", font=title_font, height=2, width=25)

density_swims = Radiobutton(window, text="Does swim", value="1", variable=density, command=which_element)
density_not_swims = Radiobutton(window, text="Does not sim", value="0", variable=density, command=which_element)
density_swims.select()

combustibility_burns = Radiobutton(window, text="Does burn", value="1", variable=combustibility, command=which_element)
combustibility_not_burns = Radiobutton(window, text="Does not burn", value="0", variable=combustibility,
                                       command=which_element)
combustibility_burns.select()

bwb_sooty_flame = Checkbutton(window, text="Sooty flame", onvalue="1", offvalue="0", variable=bwb[0],
                              command=which_element)
bwb_dripping_flame = Checkbutton(window, text="Dripping flame", onvalue="1", offvalue="0", variable=bwb[1],
                                 command=which_element)
bwb_smellin_flame = Checkbutton(window, text="Smells like wax", onvalue="1", offvalue="0", variable=bwb[2],
                                command=which_element)
bwb_sooty_flame.deselect()
bwb_dripping_flame.deselect()
bwb_smellin_flame.deselect()

densityLabel.pack()
density_swims.pack()
density_not_swims.pack()

combustibilityLabel.pack()
combustibility_burns.pack()
combustibility_not_burns.pack()

bwbLabel.pack()
bwb_sooty_flame.pack()
bwb_dripping_flame.pack()
bwb_smellin_flame.pack()

elementLabel.pack()
window.mainloop()
