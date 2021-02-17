from functools import partial
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


class HomePage(Screen):
    def __init__(self, page_controller, user, **kw):
        super().__init__(**kw)
        self.name = 'home_page'
        self.user = user
        self.user_path = f'{os.getcwd()}/users/{self.user}'


        # Set bg color
        self.bg_image = Image(source='data/home_background.png', allow_stretch=True,
        keep_ratio = False)
        self.add_widget(self.bg_image)

        self.load_images(page_controller=page_controller)



    
    def load_images(self, page_controller):
        recent_images_box = BoxLayout(orientation='vertical', spacing= 10, size_hint=(.2, 1), pos_hint={'x': .05, 'y': 0}, padding=(0, 10))
        images_path = f'{self.user_path}/images'

        dir_list = os.listdir(images_path)
        
        recent_images_label = Label(text='Recent Photos', size_hint = (1, .2), font_size=30)
        recent_images_box.add_widget(recent_images_label)

        for i in range(len(dir_list)):
            img = Image(source=f'{images_path}/{dir_list[i]}', size_hint=(1, 1),
            keep_ratio = False, allow_stretch=True)

            recent_images_box.add_widget(img)
            if i == 2:
                break
        
        more_recents_button = Button(text='VIEW MORE', size_hint = (1, .2), on_release=partial(self.load_recents_page, page_controller))
        recent_images_box.add_widget(more_recents_button)
        self.add_widget(recent_images_box)

    def load_add_image_gui(self):
        pass

    def load_recents_page(self, page_controller, event):
        page_controller.initialize_recents_page()
            
            
