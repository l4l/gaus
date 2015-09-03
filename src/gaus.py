from math import pi, exp, pow

__author__ = 'kitsu'


def get_filtered(pixels: [[]], x: int, y: int, size: int, k: [[]]) -> ():
    t = (0, 0, 0)
    s = 0
    half = int(size / 2)

    for i in range(x - half, x + half):
        for j in range(y - half, y + half):
            try:
                pix = pixels[(i, j)]
            except IndexError:
                continue

            mod = k[j - y + half][i - x + half]
            t = (t[0] + pix[0] * mod,
                 t[1] + pix[1] * mod,
                 t[2] + pix[2] * mod)
            s += mod
    if s != 0:
        return int(t[0] / s), int(t[1] / s), int(t[2] / s)
    else:
        return 0, 0, 0


def kernel(size: int, sigma: float) -> [[]]:
    a = [[0 for x in range(size)] for x in range(size)]
    cnst = 1 / (2 * pi * pow(sigma, 2))
    s = 0

    half = int(size / 2)
    r = range(size)

    for i in r:
        for j in r:
            x = i - half
            y = j - half

            d = (x * x + y * y) / \
                (2 * sigma * sigma)

            a[i][j] = cnst * exp(-d)
            s += a[i][j]

    for i in r:
        for j in r:
            a[i][j] /= s

    return a


def kernel_dx(size: int, sigma: float) -> [[]]:
    a = [[0 for x in range(size)] for x in range(size)]
    cnst = 1 / (2 * pi * pow(sigma, 2))
    s = 0

    half = int(size / 2)
    r = range(size)

    for i in r:
        for j in r:
            x = i - half
            y = j - half

            d = (2 * x + y * y) / \
                (2 * sigma * sigma)

            a[i][j] = cnst * exp(-d)
            s += a[i][j]

    for i in r:
        for j in r:
            a[i][j] /= s

    return a


def kernel_dy(size: int, sigma: float) -> [[]]:
    a = [[0 for x in range(size)] for x in range(size)]
    const = 1 / (2 * pi * pow(sigma, 2))
    s = 0

    half = int(size / 2)
    r = range(size)

    for i in r:
        for j in r:
            x = i - half
            y = j - half

            d = (x * x + 2 * y) / \
                (2 * sigma * sigma)

            a[i][j] = const * exp(-d)
            s += a[i][j]

    for i in r:
        for j in r:
            a[i][j] /= s

    return a
