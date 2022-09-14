import sys
from froggerlib.locatable import Locatable

class Movable(Locatable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0):
        Locatable.__init__(self, x, y, w, h)
        self.mDesiredX = dx
        self.mDesiredY = dy
        self.mSpeed = s
        self.mRide = None
        return

    def move(self):
        if self.atDesiredLocation():
            return
        diffx = self.mDesiredX - self.mX
        diffy = self.mDesiredY - self.mY
        diff = abs(diffx) + abs(diffy)
        ratiox = float(diffx) / float(diff)
        ratioy = float(diffy) / float(diff)
        dx = int(ratiox * self.mSpeed)
        dy = int(ratioy * self.mSpeed)
        if abs(dx) > abs(diffx):
            dx = diffx
        if abs(dy) > abs(diffy):
            dy = diffy
        self.mX += dx
        self.mY += dy
        return

    def getDesiredX(self):
        return self.mDesiredX

    def getDesiredY(self):
        return self.mDesiredY

    def getSpeed(self):
        return self.mSpeed

    def setDesiredX(self, dx):
        self.mDesiredX = dx
        return

    def setDesiredY(self, dy):
        self.mDesiredY = dy
        return

    def setSpeed(self, s):
        self.mSpeed = s
        return

    def atDesiredLocation(self):
        return self.mX == self.mDesiredX and self.mY == self.mDesiredY

    def outOfBounds(self, screen_width, screen_height):
        if self.getX() + self.getWidth() < 0:
            return True
        if self.getX() > screen_width:
            return True
        if self.getY() + self.getHeight() < 0:
            return True
        if self.getY() > screen_height:
            return True
        return False

    def riding(self):
        return self.mRide != None

    def setRide(self, rideable):
        self.mRide = rideable
        return

    def getRide(self):
        return self.mRide

    def __str__(self):
        s = "Movable<"+Locatable.__str__(self)+","+str(self.mDesiredX)+","+str(self.mDesiredY)+","+str(self.mSpeed)+">"
        return s

    def __repr__(self):
        return str(self)

def test():
    m = Movable()
    m.setDesiredX(11)
    m.setDesiredY(-5)
    m.setSpeed(3)
    while not m.atDesiredLocation():
        print(m)
        m.move()

    print(m)
    return

if __name__ == "__main__":
    test()
