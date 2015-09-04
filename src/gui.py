from PIL import ImageTk
from tkinter import *


class MainWindow:
    def __init__(self, img, size=3):
        self.root = Tk()
        self.im = []
        for i in range(size):
            self.im.append(ImageTk.PhotoImage(img[i]))
        self.label = []
        for i in range(size):
            im = ImageTk.PhotoImage(img[i])
            self.label.append(Label(image=self.im[i]))
            self.label[i].pack()

        self.root.title('Gaussian filter')

    def show(self):
        self.root.mainloop()


__author__ = 'kitsu'
