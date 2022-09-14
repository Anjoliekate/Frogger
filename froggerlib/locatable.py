class Locatable:

    def __init__(self, x=0, y=0, w=0, h=0):
        self.mX = x
        self.mY = y
        self.mWidth = w
        self.mHeight = h
        return

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getWidth(self):
        return self.mWidth

    def getHeight(self):
        return self.mHeight

    def setX(self, x):
        self.mX = x
        return

    def setY(self, y):
        self.mY = y
        return

    def setWidth(self, width):
        self.mWidth = width
        return

    def setHeight(self, height):
        self.mHeight = height
        return

    def containsPoint(self, x, y):
        if( (x >= self.getX()) and
            (x <= self.getX() + self.getWidth()) and
            (y >= self.getY()) and
            (y <= self.getY() + self.getHeight()) ):
            return True
        return False

    def containsLocatable(self, other):
        ox1 = other.getX()
        ox2 = ox1 + other.getWidth()
        oy1 = other.getY()
        oy2 = oy1 + other.getHeight()
        opoints = [ (ox1,oy1), (ox1,oy2), (ox2,oy2), (ox2,oy1) ]
        for op in opoints:
            x, y = op
            if not self.containsPoint(x, y):
                return False
        return True

    def overlapWithLocatable(self, other):
        sx1 = self.getX()
        sx2 = sx1 + self.getWidth()
        sy1 = self.getY()
        sy2 = sy1 + self.getHeight()
        spoints = [ (sx1,sy1), (sx1,sy2), (sx2,sy2), (sx2,sy1) ]

        ox1 = other.getX()
        ox2 = ox1 + other.getWidth()
        oy1 = other.getY()
        oy2 = oy1 + other.getHeight()
        opoints = [ (ox1,oy1), (ox1,oy2), (ox2,oy2), (ox2,oy1) ]

        for sp in spoints:
            x, y = sp
            if other.containsPoint(x, y):
                return True

        for op in opoints:
            x, y = op
            if self.containsPoint(x, y):
                return True

        return False

    def hits(self, other):
        return False

    def supports(self, other):
        return False

    def riding(self):
        return False

    def setRide(self, other):
        return

    def __str__(self):
        s = "Locatable<"+str(self.mX)+","+str(self.mY)+","+str(self.mWidth)+","+str(self.mHeight)+">"
        return s

    def __repr__(self):
        return str(self)




def test():
    l = Locatable()
    print(l)
    l.setX(1)
    l.setY(2)
    l.setWidth(3)
    l.setHeight(4)
    print(l)

    l2 = Locatable(4, 6, 1, 1)
    print(l2)
    if l2.overlapWithLocatable(l):
        print("overlap")
    else:
        print("no overlap")

    return

if __name__ == "__main__":
    test()
