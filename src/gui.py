from tkinter import *
from PIL import ImageTk
import main

root = Tk()
root.title('Gaussian filter')


class MainWindow(Frame):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.im = []
        self.label = []
        self.canvas = []
        self.frame = Frame(self)
        self.sigma_label = Label(self, text="Sigma:")
        self.filter_label = Label(self, text="Filter types:")
        self.img_path_label = Label(self, text="Image path:")
        self.img_file_label = Label(self, text="File image:")
        self.img_ext_label = Label(self, text="Image extension:")

        self.sigma_entry = Entry(self)
        self.filter_entry = Entry(self)
        self.img_path_entry = Entry(self)
        self.img_file_entry = Entry(self)
        self.img_ext_entry = Entry(self)

        self.btn = Button(self, text="Gaussian", command=self.add_img)

        self.draw_menu()
        self.pack()

    def draw_menu(self):
        self.sigma_label.grid(row=0, column=0)
        self.filter_label.grid(row=0, column=1)
        self.img_path_label.grid(row=0, column=2)
        self.img_file_label.grid(row=0, column=3)
        self.img_ext_label.grid(row=0, column=4)

        self.sigma_entry.grid(row=1, column=0)
        self.filter_entry.grid(row=1, column=1)
        self.img_path_entry.grid(row=1, column=2)
        self.img_file_entry.grid(row=1, column=3)
        self.img_ext_entry.grid(row=1, column=4)

        self.btn.grid(row=2, column=2)

    def show(self):
        self.mainloop()

    def add_img(self):
        filters = 1
        buffer = main.calc_buffer(img_dir=self.img_path_entry.get(),
                                  file=self.img_file_entry.get(),
                                  ext=self.img_ext_entry.get(),
                                  sigma=float(self.sigma_entry.get()),
                                  filters=int(self.filter_entry.get()))
        self.grid_forget()
        self.im = []
        for i in range(filters):
            # self.canvas.append(Canvas(master=self.frame))
            # img = ImageTk.PhotoImage(buffer[i])
            # self.canvas[i].create_image(0, 0, image=img)
            # self.canvas[i].pack()
            self.im.append(ImageTk.PhotoImage(buffer[i]))
            self.label.append(Label(image=self.im[i]))
            self.label[i].pack()
        self.pack()


__author__ = 'kitsu'
