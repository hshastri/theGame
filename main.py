import arcade
import pathlib
import time
import random

WIDTH = 15 * 32
HEIGHT = 15 * 32

class TiledWindow(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "Tiled Map")
        self.mapLocation = pathlib.Path.cwd()/'Assets'/'map.tmx'
        self.mapList = None
        self.wallList = None
        self.enemy: arcade.AnimatedTimeBasedSprite = None
        self.enemy_list: arcade.SpriteList = None

        self.start = 0.0

        self.simplePhysics: arcade.PhysicsEngineSimple = None

    def setup(self):
        map = arcade.tilemap.read_tmx(str(self.mapLocation))
        self.mapList = arcade.tilemap.process_layer(map, 'traverse', 1)
        self.wallList = arcade.tilemap.process_layer(map, 'walls', 1)

        self.start = time.time()

        path = pathlib.Path.cwd() /'Assets'/ 'Archive' / 'walk'
        self.enemy = \
            arcade.AnimatedTimeSprite(0.5, center_x= WIDTH, center_y=  5 * 32)
        self.enemy_list = arcade.SpriteList()
        all_files = path.glob('*.png')
        textures = []
        for file_path in all_files:
            #print(file_path)
            frame = arcade.load_texture(str(file_path))  # we want the whole image
            textures.append(frame)
        print(textures)
        self.enemy.textures = textures
        self.enemy_list.append(self.enemy)


    def on_draw(self):
        arcade.start_render()
        self.mapList.draw()
        self.wallList.draw()
        self.enemy_list.draw()

    def update(self, delta_time: float):

        self.enemy.center_x = self.enemy.center_x - 0.5

        if (time.time() - self.start >= 1.0):
            self.start = time.time()
            y_position = random.randint(5 * 32, HEIGHT)
            path = pathlib.Path.cwd() / 'Assets' / 'Archive' / 'walk'
            enemy : arcade.AnimatedTimeBasedSprite = \
                arcade.AnimatedTimeSprite(0.5, center_x=WIDTH, center_y= y_position)
            #enemy.center_x = enemy.center_x - 0.5
            all_files = path.glob('*.png')
            textures = []
            for file_path in all_files:
                #print(file_path)
                frame = arcade.load_texture(str(file_path))  # we want the whole image
                textures.append(frame)
            enemy.textures = textures
            #enemy.center_x = enemy.center_x - 0.5
            self.enemy_list.append(enemy)


        self.enemy_list.update()
        self.enemy_list.move(-0.5, 0)


        for enemy in self.enemy_list:
            enemy.update_animation()



def main():
    window: TiledWindow = TiledWindow()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
