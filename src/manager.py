from PIL import Image
import gaus, threader, gui
import datetime
__author__ = 'kitsu'


def init(img_dir, proc_dir, file, ext, sigma, filters) -> []:
    im = Image.open(img_dir + file + ext)
    buffer = [Image.new("RGB", (im.width, im.height)) for i in range(filters)]

    print("Sigma is ", sigma)
    size = int(sigma * 3)
    if size % 2 == 0:
        size -= 1

    k = gaus.kernel(size, sigma)
    kx = gaus.kernel_dx(size, sigma)
    ky = gaus.kernel_dy(size, sigma)
    # r = range(size)
    # for i in r:
    #     for j in r:
    #         print(k[i][j])
    #     print('\n')

    upd_buffer(im, buffer[0],
               size, k, "default gaussian",
               proc_dir + file + "Proc" + "Def" + str(sigma) + ext)
    if filters > 1:
        upd_buffer(im, buffer[1],
                   size, kx, "gaussian x derivation",
                   proc_dir + file + "Proc" + "Dx" + str(sigma) + ext)
        if filters > 2:
            upd_buffer(im, buffer[2],
                       size, ky, "gaussian y derivation",
                       proc_dir + file + "Proc" + "Dy" + str(sigma) + ext)
    return buffer


def upd_buffer(image, buffer, size, kernel, name, filename):

    upd = int(image.height / 10)
    pix = image.load()
    buf = buffer.load()

    for y in range(0, image.height):
        if y % upd == 0:
            print(datetime.datetime.now())
            print("Readiness of", name, " is ", y/upd * 10, "%\n")
        for x in range(0, image.width):
            buf[(x, y)] = gaus.get_filtered(pix, x, y, size, kernel)
        # while threader.LineThreader.threads > 20:
        #     1
        # tr = threader.LineThreader(lambda x: gaus.get_filtered(pix, x, y, size, kernel),
        #                            buf, image.width, y)
        # tr.start()

    print(datetime.datetime.now())
    print("Ready", name, '\n')
    buffer.save(filename)