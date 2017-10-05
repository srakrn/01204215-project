import arcade
# This is bad. Please do not try.
from models import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SWIMMERS_AMOUNT = 4

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
    def draw(self):
        self.sync_with_model()
        super().draw()

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT, SWIMMERS_AMOUNT)
        self.swimmers_sprite = []
        for i in range(SWIMMERS_AMOUNT):
            self.swimmers_sprite.append(ModelSprite('imgs/swimmer-1.png', model=self.world.swimmers[i]))
    def on_draw(self):
        arcade.start_render()
        for swimmer_sprite in self.swimmers_sprite:
            swimmer_sprite.draw()

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
