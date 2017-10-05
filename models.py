import arcade, arcade.key
import random

class SpriteTextures:
    swimmer_normal = arcade.load_texture("imgs/swimmer-1.png", scale=1)
    swimmer_fallen = arcade.load_texture("imgs/swimmer-1-fallen.png", scale=1)

class World:
    def __init__(self, width, height, swimmers_amount):
        self.width = width
        self.height = height
        self.swimmers = []
        self.time = 0
        for i in range(swimmers_amount):
            self.swimmers.append(Swimmer(50+(width-150)/4*i, 300))
        self.swimmers[0].command = arcade.key.A
        self.swimmers[1].command = arcade.key.S
        self.swimmers[2].command = arcade.key.D
        self.swimmers[3].command = arcade.key.F
    def update(self, delta):
        self.time += delta
        self.randomized = random.uniform(0,1)*2
        if Swimmer.alive_swimmers > 0:
            if self.randomized < self.time:
                self.fallen_position = random.randint(0,3)
                while(not self.swimmers[self.fallen_position].alive):
                    self.fallen_position = random.randint(0,3)
                self.swimmers[self.fallen_position].fallen()
                self.time = 0
        for swimmer in self.swimmers:
            swimmer.update(delta)
    def on_key_press(self, key, key_modifiers):
        print("Key pressed: {}".format(key))
        for swimmer in self.swimmers:
            swimmer.on_key_press(key, key_modifiers)

class Swimmer:
    alive_swimmers = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.sinking = False
        self.unsinking = False
        self.text = ''
        self.command = ''
        self.sprite = arcade.Sprite()
        self.sprite.texture = SpriteTextures.swimmer_normal
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        Swimmer.alive_swimmers += 1
    def fallen(self):
        self.sprite.texture = SpriteTextures.swimmer_fallen
        self.sinking = True
    def sink(self):
        if self.sinking:
            self.y -= 2
        if self.sprite.top < -20:
            self.alive = False
            self.sinking = False
            self.unsinking = False
            Swimmer.alive_swimmers -= 1
    def unsink(self):
        if self.unsinking:
            self.y += 3
        if self.y>300:
            print("Unsinking")
            self.unsinking = False
            self.y = 300
            self.sprite.texture = SpriteTextures.swimmer_normal
    def update(self, delta):
        if self.alive:
            self.sink()
            self.unsink()
            self.sprite.center_x = self.x
            self.sprite.center_y = self.y
            self.sprite.update()
    def draw(self):
        self.sprite.draw()
    def on_key_press(self, key, key_modifiers):
        print("on_key_press; key = {} command = {}".format(key, self.command))
        if key == self.command:
            self.unsinking = True
