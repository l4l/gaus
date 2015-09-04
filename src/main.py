import manager
import gui

__author__ = 'kitsu'

def_img_dir = "img/"
def_proc_dir = "proc/"
def_file = "jY4lqBT0ygI"
def_ext = ".jpg"
def_sigma = 1
def_filters = 1


def main():
    win = gui.MainWindow()
    win.show()


def calc_buffer(img_dir=def_img_dir,
                proc_dir=def_proc_dir,
                file=def_file,
                ext=def_ext,
                sigma=1, filters=1) -> []:
    if img_dir == "":
        img_dir = def_img_dir
    if proc_dir == "":
        proc_dir = def_proc_dir
    if file == "":
        file = def_file
    if ext == "":
        ext = def_ext
    proc_dir = img_dir + proc_dir
    return manager.init(img_dir, proc_dir, file, ext, sigma, filters)


if __name__ == "__main__":
    main()
