class World:
    def __init__(self, width, height, swimmers_amount):
        self.width = width
        self.height = height
        self.swimmers = []
        for i in range(swimmers_amount):
            self.swimmers.append(Swimmer(50+(width-150)/4*i, 300))
    def update(self, delta):
        for swimmer in self.swimmers:
            swimmer.update(delta)

class Swimmer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.sinking = False
        self.unsinking = False
    def sink(self):
        if self.sinking:
            self.y -= 10
        if self.y < 0:
            self.alive = False
            self.sinking = False
            self.unsinking = False
    def unsink(self):
        if self.unsinking:
            self.y += 10
            if self.y>300:
                self.unsinking = False
                self.y = 300
    def update(self, delta):
        self.sink()
        self.unsink()
