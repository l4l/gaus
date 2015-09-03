import threading

__author__ = 'kitsu'


class Threader (threading.Thread):
    threads = 0
    id = 0

    def __init__(self, fun, x: int, y: int, buf):
        threading.Thread.__init__(self)
        Threader.id += 1
        self.id = Threader.id
        self.x = x
        self.y = y
        self.buf = buf
        self.fun = fun

    def run(self):
        # print(self.id)
        Threader.threads += 1
        self.buf[(self.x, self.y)] = self.fun()
        Threader.threads -= 1
