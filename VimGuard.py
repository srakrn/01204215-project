import arcade
import arcade.key
# This is bad. Please do not try.
from models import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SWIMMERS_AMOUNT = 4

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT, SWIMMERS_AMOUNT)
        self.background = arcade.load_texture("imgs/background.png")
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
            SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        for swimmer in self.world.swimmers:
            swimmer.draw()
        arcade.draw_text(str(Swimmer.score),
            self.width - 30, self.height - 30,
            arcade.color.BLACK, 20)
    def update(self, delta):
        self.world.update(delta)
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
