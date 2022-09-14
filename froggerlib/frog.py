from froggerlib.player_controllable import PlayerControllable

class Frog(PlayerControllable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, hg=0, vg=0):
        PlayerControllable.__init__(self, x, y, w, h, dx, dy, s, hg, vg)
        return

    def __str__(self):
        s = "Frog<"+PlayerControllable.__str__(self)+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    f = Frog()
    f.setHorizontalGap(15)
    f.setVerticalGap(15)
    f.setSpeed(2)

    print(f)
    f.up()
    print(f)
    while not f.atDesiredLocation():
        f.move()
        print(f)

    return

if __name__ == "__main__":
    test()
