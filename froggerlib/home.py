from froggerlib.touchable import Touchable

class Home(Touchable):

    def __init__(self, x=0, y=0, w=0, h=0):
        Touchable.__init__(self, x, y, w, h)

    def hits(self, other):
        return self.containsLocatable(other) and not other.riding()

    def __str__(self):
        s = "Home<"+Touchable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    m = Home()
    print(m)
    return

if __name__ == "__main__":
    test()
