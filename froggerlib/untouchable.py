from froggerlib.immovable import Immovable

class Untouchable(Immovable):

    def __init__(self, x=0, y=0, w=0, h=0):
        Immovable.__init__(self, x, y, w, h)
        return

    def __str__(self):
        s = "Untouchable<"+Immovable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    m = Untouchable()
    print(m)
    return

if __name__ == "__main__":
    test()
