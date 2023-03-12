from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivy.app import App
from kivy.core.window import Window
Window.size = (360, 800)
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.config import Config
import time
import os

Builder.load_file("./cum.kv")

class GalleryScreen(Screen):
    def on_enter(self, *args):
        photos = os.listdir("./Photos")
        for i in range(len(photos)):
            if i % 2 == 0:
                self.ids["scroll"].rows += 1
            self.ids["scroll"].add_widget(Image(source= "./Photos/" + photos[i]))
            self.ids["scroll"].height += 100 

    def back(self):

        self.manager.current = "Main screen"

class CameraScreen(Screen):
    def photo(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("./Photos/IMG_{}.png".format(timestr))

    def back(self):
        self.manager.current = "Main screen"


class MainScreen(Screen):
    def open_camera(self):
        self.manager.current = "Camera"

    def open_gallery(self):
        self.manager.current = "Gallery"

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main = MainScreen()
        camera = CameraScreen()
        gallery = GalleryScreen()
        screen_manager.add_widget(main)
        screen_manager.add_widget(camera)
        screen_manager.add_widget(gallery)

        return screen_manager


if __name__ == "__main__":
    app = MyApp()
    app.run()