from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import os
from pathlib import Path

class RecentsPage(Screen):
    def __init__(self, page_controller, user, **kw):
        super().__init__(**kw)
        self.user = user
        self.user_path = f'{os.getcwd()}/users/{self.user}'

        
        # Set bg color
        self.bg_image = Image(source='data/home_background.png', allow_stretch=True,
        keep_ratio = False)
        self.add_widget(self.bg_image)

        # Load images
        self.load_all_images()

        back_button = Button(text='BACK TO HOME', font_size=14, size_hint = (.15, .1), pos_hint = {'x':.825, 'y':.07})
        self.add_widget(back_button)

    
    def load_all_images(self):

        images_box = GridLayout(cols=4, size_hint = (.8, 1), spacing=10, padding=5)
        images_path = f'{self.user_path}/images'

        dir_list = os.listdir(images_path)

        for i in range(len(dir_list)):
            img = Image(source=f'{images_path}/{dir_list[i]}', size_hint=(1, 1),
            keep_ratio = False, allow_stretch=True)

            images_box.add_widget(img)
        self.add_widget(images_box)

        
                
