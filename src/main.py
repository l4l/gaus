from math import pi, exp, pow

__author__ = 'kitsu'


def main():
    size = 5
    r = range(size)
    sigma = 1

    k = kernel(size, sigma)
    for i in r:
        for j in r:
            print(k[i][j])
        print('\n')


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


if __name__ == "__main__":
    main()
