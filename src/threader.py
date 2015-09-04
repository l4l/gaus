import threading

__author__ = 'kitsu'


class LineThreader (threading.Thread):
    threads = 0
    id = 0

    def __init__(self, fun, buf, width: int, y: int):
        threading.Thread.__init__(self)
        LineThreader.id += 1
        self.id = LineThreader.id
        self.fun = fun
        self.buf = buf
        self.width = width
        self.y = y

    def run(self):
        # print(self.id)
        LineThreader.threads += 1
        for x in range(0, self.width):
            self.buf[(x, self.y)] = self.fun(x)
        LineThreader.threads -= 1


class Threader (threading.Thread):
    threads = 0
    id = 0

    def __init__(self, fun):
        threading.Thread.__init__(self)
        LineThreader.id += 1
        self.id = LineThreader.id
        self.fun = fun
        self.ready = False
        self.result = []

    def run(self):
        LineThreader.threads += 1
        self.result = self.fun()
        LineThreader.threads -= 1

    def is_ready(self):
        return self.ready
