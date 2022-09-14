from froggerlib.locatable import Locatable

class Immovable(Locatable):

    def __init__(self, x=0, y=0, w=0, h=0):
        Locatable.__init__(self, x, y, w, h)
        return

    def __str__(self):
        s = "Immovable<"+Locatable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    m = Immovable()
    print(m)
    return

if __name__ == "__main__":
    test()
