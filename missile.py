class Missile():
    def pos(self, x, y):
        self.x = x
        self.y = y

    def moveup(self, oldx):
        if oldx > 0:
            oldx -= self.vel
            return oldx
        else:
            return oldx

    def checkcollision(self, mx, my, ax, ay):
        if mx == ax and ay == my:
            return 1
        else:
            return 0


class Mis1(Missile):

    def __init__(self):
        self.vel = 1
        self.sym = u'\u2022'
        self.typ = 1


class Mis2(Missile):
    def __init__(self):
        self.vel = 2
        self.sym = u'\u2021'
        self.typ = 2
