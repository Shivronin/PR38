from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (360, 800)
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.config import Config
import time
import os

Builder.load_string(
'''
<MainScreen>:
    name: "Main screen"

    FloatLayout:
        Button:
            text: "Открыть камеру"
            pos_hint: {'center_x': .3, 'center_y': .1/2}
            size_hint: .4, .1
            on_press: root.open_camera()

        Button:
            text: "Галерея"
            pos_hint: {'center_x': .7, 'center_y': .1/2}
            size_hint: .4, .1
            on_press: root.open_gallery()

<GalleryScreen>:
    name: "Gallery"

    
            
    ScrollView:
        GridLayout:
            cols: 2
            rows: 0
            row_default_height: 150
            col_default_height: 150

            padding: 0
            canvas.before:
                Color:
                    rgba: 1,8,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint: 1, None
            id: scroll

    Button:
        text: "Назад"
        pos_hint: {'center_x': .5, 'center_y': .1/2}
        size_hint: .4, .1
        on_press: root.back()

<CameraScreen>:
    name: "Camera"

    FloatLayout:
        Camera:
            id: camera
            resolution: (360, 800)
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            play: True
        
        Button:
            text: "Снимок"
            pos_hint: {'center_x': .5}
            size_hint: .5, .1
            on_press: root.photo()

        Button:
            text: "Назад"
            pos_hint: {'center_x': .2, 'center_y': .9}
            size_hint: .3, .1
            on_press: root.back()
'''
)

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

class MyApp(MDApp):
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