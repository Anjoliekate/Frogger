from froggerlib.touchable import Touchable

class Road(Touchable):

    def __init__(self, x=0, y=0, w=0, h=0):
        Touchable.__init__(self, x, y, w, h)

    def __str__(self):
        s = "Road<"+Touchable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    m = Road()
    print(m)
    return

if __name__ == "__main__":
    test()
