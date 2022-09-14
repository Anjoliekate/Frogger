from froggerlib.movable import Movable

class Rideable(Movable):

    def __init__(self, x=0, y=0, w=0, h=0, dx=0, dy=0, s=0):
        Movable.__init__(self, x, y, w, h, dx, dy, s)
        self.mRiders = []
        return

    def supports(self, other):
        if self.overlapWithLocatable(other):

            if other not in self.mRiders:
                take_on = False
                ride = other.getRide()
                if ride == None:
                    take_on = True
                else:
                    ody = other.getDesiredY() - other.getY()
                    if ody < 0 and self.getY() < other.getY():
                        take_on = True
                    elif ody > 0 and self.getY() > other.getY():
                        take_on = True

                if take_on:
                    self.mRiders.append(other)
                    other.setRide(self)
                    return True
        else:
            if other in self.mRiders:
                self.mRiders.remove(other)
                if other.getRide() == self:
                    other.setRide(None)
        return False

    def getRiders(self):
        return self.mRiders

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

        for rider in self.mRiders:
            rider.setX(rider.getX()+dx)
            rider.setY(rider.getY()+dy)
            rider.setDesiredX(rider.getDesiredX()+dx)
            rider.setDesiredY(rider.getDesiredY()+dy)

        return

    def __str__(self):
        riders = ""
        for r in self.mRiders:
            if r != self.mRiders[0]:
                riders += ","
            riders += str(r)
        s = "Rideable<"+Movable.__str__(self)+","+riders+">"
        return s

    def __repr__(self):
        return str(self)


def test():
    d1 = Rideable(5,5,10,10, 20,20,4)
    d2 = Rideable(3,3,2,2)
    print(d1)
    print(d2)
    if d1.supports(d2):
        print("supports")
    else:
        print("not supports")
    print(d1)

    d1.move()
    print(d1)
    print(d2)
    d1.move()
    print(d1)
    print(d2)

    return

if __name__ == "__main__":
    test()
