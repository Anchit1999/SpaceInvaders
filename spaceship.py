class Spaceship():

    def __init__(self, xPos, yPos, vel, sym):
        self.xPos = xPos
        self.yPos = yPos
        self.vel = vel
        self.sym = sym

    def moveright(self, yPos):
        if yPos < 15:  # 8
            yPos += self.vel
            return yPos
        else:
            return yPos

    def moveleft(self, yPos):
        if yPos > 1:
            yPos -= self.vel
            return yPos
        else:
            return yPos
