class World:
    def __init__(self, width, height, swimmers_amount):
        self.width = width
        self.height = height
        self.swimmers = []
        for i in range(swimmers_amount):
            self.swimmers.append(Swimmer(50+(width-150)/4*i, 300))
    def update(self, delta):
        self.ship.update(delta)

class Swimmer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sinking = True
    def update(self, delta):
        pass
