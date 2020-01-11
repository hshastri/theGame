import arcade
import pathlib

WIDTH = 15 * 32
HEIGHT = 15 * 32

class TiledWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Tiled Map")
        self.mapLocation = pathlib.Path.cwd()/'Assets'/'map.tmx'
        self.mapList = None
        self.wallList = None
        self.simplePhysics: arcade.PhysicsEngineSimple = None

    def setup(self):
        map = arcade.tilemap.read_tmx(str(self.mapLocation))
        self.mapList = arcade.tilemap.process_layer(map, 'traverse', 1)
        self.wallList = arcade.tilemap.process_layer(map, 'walls', 1)

    def on_draw(self):
        arcade.start_render()
        self.mapList.draw()
        self.wallList.draw()

def main():
    window: TiledWindow = TiledWindow()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
