from tkinter import *
from tkinter import filedialog
import os

from PIL import Image, ImageTk


class GalleryApp:
    def __init__(self, imagelist=None):
        self.window = Tk()
        self.window.title = "Photo Gallery"
        self.photo_frame = PhotoFrame(self)

        self.next_btn = Button(self.window, text="Next", command=self.photo_frame.next_image)
        self.next_btn.pack(side=BOTTOM)

        if imagelist:
            self.photo_frame.imagelist = imagelist
        else:
            self.photo_frame.open_image_folder()
        self.photo_frame.next_image()

        self.window.update()
        self.window.minsize(720, 480)
        self.window.mainloop()


class PhotoFrame:
    accepted_formats = ["jpg", "jpeg", "png", ".gif"]

    def __init__(self, parent):
        self.parent = parent

        self.imagelist = []
        self.current_idx = -1

        self.frame = Frame(self.parent.window)
        self.frame.pack(expand=1, fill=BOTH)

        self.image_canvas = Canvas(self.frame)
        self.image_canvas.pack(expand=1, fill=BOTH)

        self.description = StringVar()
        self.description_label = Label(self.frame, textvariable=self.description, width=50)
        self.description_label.pack(side=BOTTOM)

        self.current_image = None

    def open_image_folder(self):
        self.parent.window.update()
        folderpath = filedialog.askdirectory()
        filelist = os.listdir(folderpath)

        for file in filelist:
            if any(ext in file for ext in self.accepted_formats):
                self.imagelist.append(os.path.join(folderpath, file))

    def next_image(self):
        if self.current_idx + 1 >= len(self.imagelist):
            self.current_idx = -1

        if isinstance(self.imagelist[self.current_idx + 1], tuple):
            img = Image.open(self.imagelist[self.current_idx + 1][0])
            text = self.imagelist[self.current_idx + 1][1]
        else:
            img = Image.open(self.imagelist[self.current_idx + 1])
            text = "No Description available"

        self.description.set(text)
        self.current_image = ImageTk.PhotoImage(img)

        pos = (self.image_canvas.winfo_width() / 2 - self.current_image.width() / 2,
               self.image_canvas.winfo_height() / 2 - self.current_image.height() / 2)

        self.image_canvas.create_image(pos[0], pos[1], anchor=NW, image=self.current_image)

        self.current_idx += 1


imagelist = [
    ("/Users/nickespig/Projects/Exercise/python_book_exercises/book/kap_17/bildergalerie/bilder/bodrum.png",
     "Some Text"),
    ("/Users/nickespig/Projects/Exercise/python_book_exercises/book/kap_17/bildergalerie/bilder/dalton.gif",
     "Some Text 2"),
    ("/Users/nickespig/Projects/Exercise/python_book_exercises/book/kap_17/bildergalerie/bilder/futurium.png",
     "Some Text 3"),
    ("/Users/nickespig/Projects/Exercise/python_book_exercises/book/kap_17/bildergalerie/bilder/museum.gif",
     "Some Text 4"),
    ("/Users/nickespig/Projects/Exercise/python_book_exercises/book/kap_17/bildergalerie/bilder/weiter.gif",
     "Some Text 5")
]

gallery = GalleryApp()
