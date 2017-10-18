import arcade, arcade.key
import random
import vim_commands as commands

class SpriteTextures:
    swimmer_normal = arcade.load_texture("imgs/swimmer-1.png", scale=1)
    swimmer_fallen = arcade.load_texture("imgs/swimmer-1-fallen.png", scale=1)
    swimmer_up = arcade.load_texture("imgs/swimmer-1-up.png", scale=1)

class World:
    def __init__(self, width, height, swimmers_amount):
        self.width = width
        self.height = height
        self.swimmers = []
        self.big_text = BigText()
        self.time = 0
        for i in range(swimmers_amount):
            self.swimmers.append(Swimmer(50+(width-150)/4*i, 275))
    def update(self, delta):
        self.time += delta
        self.randomized = random.uniform(0,1)*200
        if Swimmer.alive_swimmers > 0:
            if self.randomized < self.time:
                self.fallen_position = random.randint(0,3)
                while not self.swimmers[self.fallen_position].alive and not self.swimmers[self.fallen_position].sinking:
                    self.fallen_position = random.randint(0,3)
                self.swimmers[self.fallen_position].fallen()
                self.time = 0
        for swimmer in self.swimmers:
            swimmer.update(delta)
        
    def on_key_press(self, key, key_modifiers):
        for swimmer in self.swimmers:
            swimmer.on_key_press(key, key_modifiers)

class BigText:
    def __init__(self):
        self.text = ''
        self.duration = 0
        self.shown = False
        self.text_obj = arcade.create_text(self.text, arcade.color.BLACK, 20, width=600, align="center")
    def show(self, text, duration=500):
        print("Text showing.")
        self.text = text
        self.duration = duration
        self.shown = True
    def update(self, delta):
        print("Text updating.")
        if self.shown:
            self.duration -= delta
            if self.duration < 0:
                self.shown = False
        if not self.shown:
            self.text = ''
            self.duration = 0
        self.text_obj = arcade.create_text(self.text, arcade.color.BLACK, 20, width=600, align="center")
    def draw(self):
        arcade.render_text(self.text_obj, 300, 400)

class Swimmer:
    alive_swimmers = 0
    score = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True
        self.sinking = False
        self.unsinking = False
        self.rand = -1
        self.text = ''
        self.command = ''
        self.sprite = arcade.Sprite()
        self.sprite.texture = SpriteTextures.swimmer_normal
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y
        self.text_obj = arcade.create_text(self.text,
            arcade.color.BLACK, 14)
        Swimmer.alive_swimmers += 1
    def fallen(self):
        self.sprite.texture = SpriteTextures.swimmer_fallen
        self.sinking = True
        self.set_key()
        print(self.text)
    def sink(self):
        if self.sinking:
            self.y -= 2
        if self.sprite.top < -20:
            self.alive = False
            self.sinking = False
            self.unsinking = False
            self.text = ''
            Swimmer.alive_swimmers -= 1
    def unsink(self):
        if self.unsinking:
            self.sprite.texture = SpriteTextures.swimmer_up
            self.y += 5
            self.text = ''
            self.command = ''
        if self.y>275:
            self.sinking = False
            self.unsinking = False
            self.y = 275
            self.sprite.texture = SpriteTextures.swimmer_normal
            Swimmer.score += 1
    def set_key(self):
        self.rand = random.randint(0, len(commands.commands)-1)
        self.text = commands.commands[self.rand]["description"]
        self.command = ord(commands.commands[self.rand]["command"])
    def update(self, delta):
        if self.alive:
            self.sink()
            self.unsink()
            self.sprite.center_x = self.x
            self.sprite.center_y = self.y
            self.sprite.update()
            self.text_obj = arcade.create_text(self.text,
                arcade.color.BLACK, 14, width=50, align="center", anchor_x="center", anchor_y="bottom")
    def draw(self):
        self.sprite.draw()
        arcade.render_text(self.text_obj, self.x, self.y+50)
    def on_key_press(self, key, key_modifiers):
        if key == self.command:
            self.unsinking = True
