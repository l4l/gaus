from PIL import Image
from src import gaus, threader, gui

__author__ = 'kitsu'


def main():
    im = Image.open("img/Noise.png")
    buffer = Image.new("RGB", (im.width, im.height))

    # sigma = int(input())
    sigma = 2
    size = sigma * 3
    if size % 2 == 0:
        size += 1

    k = gaus.kernel(size, sigma)
    # r = range(size)
    # for i in r:
    #     for j in r:
    #         print(k[i][j])
    #     print('\n')

    pix = im.load()
    buf = buffer.load()
    upd = im.height / 10

    for y in range(0, im.height):
        if y % upd == 0:
            print("Readiness: ", y/upd * 10, "%")
        for x in range(0, im.width):
            while threader.Threader.threads > 50:
                1
            tr = threader.Threader(lambda: gaus.get_filtered(pix, x, y, size, k), x, y, buf)
            tr.start()
    while threader.Threader.threads > 0:
        1
    buffer.save("img/NoiseProcessed3.png")

    # win = gui.MainWindow(buffer)
    # win.show()

if __name__ == "__main__":
    main()
