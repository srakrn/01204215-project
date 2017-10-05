import arcade
# This is bad. Please do not try.
from models import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SWIMMERS_AMOUNT = 4

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT, SWIMEMERS_AMOUNT)
    def on_draw(self):
        arcade.start_render()

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
