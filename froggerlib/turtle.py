from froggerlib.rideable import Rideable
import random

class Turtle(Rideable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0):
        Rideable.__init__(self, x, y, w, h, dx, dy, s)
        return

    def __str__(self):
        s = "Turtle<"+Rideable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    r = Turtle(5,5,10,10, -15, 10, 4)
    print(r)
    while not r.atDesiredLocation():
        r.move()
        print(r)
    return

if __name__ == "__main__":
    test()
