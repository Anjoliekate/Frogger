from froggerlib.untouchable import Untouchable

class Grass(Untouchable):

    def __init__(self, x=0, y=0, w=0, h=0):
        Untouchable.__init__(self, x, y, w, h)

    def hits(self, other):
        return self.overlapWithLocatable(other) and not other.riding()

    def __str__(self):
        s = "Grass<"+Untouchable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    m = Grass()
    print(m)
    return

if __name__ == "__main__":
    test()
