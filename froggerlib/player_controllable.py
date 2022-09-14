from froggerlib.movable import Movable

class PlayerControllable(Movable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0, hg=0, vg=0):
        Movable.__init__(self, x, y, w, h, dx, dy, s)
        self.mHorizontalGap = hg
        self.mVerticalGap = vg
        return

    def getHorizontalGap(self):
        return self.mHorizontalGap

    def getVerticalGap(self):
        return self.mVerticalGap

    def setHorizontalGap(self, hg):
        self.mHorizontalGap = hg
        return

    def setVerticalGap(self, vg):
        self.mVerticalGap = vg
        return

    def outOfBounds(self, screen_width, screen_height):
        if self.getX() < 0:
            return True
        if self.getX() + self.getWidth() > screen_width:
            return True
        if self.getY() < 0:
            return True
        if self.getY() + self.getHeight() > screen_height:
            return True
        return False

    def up(self):
        if self.atDesiredLocation():
            self.setDesiredY(self.mDesiredY - self.mVerticalGap)
        return

    def down(self):
        if self.atDesiredLocation():
            self.setDesiredY(self.mDesiredY + self.mVerticalGap)
        return

    def left(self):
        if self.atDesiredLocation():
            self.setDesiredX(self.mDesiredX - self.mHorizontalGap)
        return

    def right(self):
        if self.atDesiredLocation():
            self.setDesiredX(self.mDesiredX + self.mHorizontalGap)
        return

    def __str__(self):
        s = "PlayerControllable<"+Movable.__str__(self)+","+str(self.mHorizontalGap)+","+str(self.mVerticalGap)+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    pc = PlayerControllable()
    pc.setSpeed(3)
    print(pc)

    while not pc.atDesiredLocation():
        pc.move()
        print(pc)

    pc.setHorizontalGap(5)
    pc.setVerticalGap(10)

    pc.up()
    while not pc.atDesiredLocation():
        pc.move()
        print(pc)

    pc.left()
    while not pc.atDesiredLocation():
        pc.move()
        print(pc)

    pc.down()
    while not pc.atDesiredLocation():
        pc.move()
        print(pc)

    pc.right()
    while not pc.atDesiredLocation():
        pc.move()
        print(pc)

    return

if __name__ == "__main__":
    test()
