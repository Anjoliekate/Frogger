from froggerlib.movable import Movable

class Dodgeable(Movable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0):
        Movable.__init__(self, x, y, w, h, dx, dy, s)
        return

    def hits(self, other):
        return self.overlapWithLocatable(other)

    def __str__(self):
        s = "Dodgeable<"+Movable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    d1 = Dodgeable(5,5,10,10)
    d2 = Dodgeable(3,3,2,2)
    print(d1)
    print(d2)
    if d1.hits(d2):
        print("hits")
    else:
        print("not hits")
    return

if __name__ == "__main__":
    test()
