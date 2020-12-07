import time

class timer:
    def __init__(self, F):
        self.F = F
        self.start = 0
        self.time = 0

    def __call__(self, *args, **kargs):
        self.start = time.time()
        self.F(*args, **kargs)
        self.time = int((time.time() - self.start) * 10000) / 10000
        return print('time = ' + str(self.time) + ' s')

@timer
def AnyFunction(n):
    for i in range(n):
        print(i)
    print('Fin')

AnyFunction(100000)
