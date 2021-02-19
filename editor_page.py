from logging import root, warn, warning
from kivy.core import text
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.uix.textinput import TextInput
import string
from pathlib import Path

from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image
from kivy.uix.popup import Popup


from functools import partial

import os


class EditorPage(Screen):
    def __init__(self, page_controller, **kw):
        super().__init__(**kw)

        #TODO set self.user back to user
        self.user = 'kathy'

        #TODO set self.img_url back to img_url
        self.img_url = f'{os.getcwd()}/users/{self.user}/images/test.png'

        self.watermark_path = f'{os.getcwd()}/users/{self.user}/watermarks'

        self.bg_image = Image(source='data/home_background.png', allow_stretch=True,
        keep_ratio = False)
        self.add_widget(self.bg_image)

        self.root_layout = BoxLayout(orientation='horizontal')
        self.root_layout.padding = 20
        self.root_layout.spacing = 50

        self.generate_recent_watermarks()
        self.generate_editing_box()
        self.generate_share_box()
        self.add_widget(self.root_layout)

    def generate_recent_watermarks(self):
        recent_watermark_box = BoxLayout(orientation='vertical', size_hint=(.15, 1))
        recent_watermark_label = Label(text='RECENT WATERMARKS', size_hint = (1, .4), font_size=15)
        recent_watermark_box.add_widget(recent_watermark_label)

        watermark_dir = os.listdir(self.watermark_path)
        
        for watermark in watermark_dir:
            water_image = Image(source=f'{self.watermark_path}/{watermark}', size_hint=(1, 1), allow_stretch=False, keep_ratio=True)
            recent_watermark_box.add_widget(water_image)
        
        self.root_layout.add_widget(recent_watermark_box)

    
    def generate_editing_box(self):
        editing_box = BoxLayout(orientation='vertical', size_hint=(.4, 1), spacing=5)
        editing_button_box = BoxLayout(orientation='horizontal', spacing=3, size_hint=(1, .1), pos_hint={'x': 0, 'y': 0})

        add_text_button = Button(text=' ADD \n\nTEXT', font_size=15, size_hint=(1, 1))
        add_watermark_button = Button(text='    ADD \n\nWATERMARK', font_size=15, size_hint=(1, 1))
        delete_watermark_button = Button(text='    DELETE \n\nWATERMARK', font_size=15, size_hint=(1, 1))

        editing_button_box.add_widget(add_text_button)
        editing_button_box.add_widget(add_watermark_button)
        editing_button_box.add_widget(delete_watermark_button)

        image_box = BoxLayout(orientation='vertical', size_hint=(1, .7))
        user_image = Image(source=self.img_url, allow_stretch=False, keep_ratio=True)
        image_box.add_widget(user_image)

        editing_box.add_widget(editing_button_box)
        editing_box.add_widget(image_box)

        self.root_layout.add_widget(editing_box)

    def generate_share_box(self):
        share_box = BoxLayout(orientation='vertical', size_hint=(.15, 1), spacing=5)

        view_recents_button = Button(text="VIEW RECENTS", font_size=15, size_hint=(1, .1))
        empty_space = BoxLayout(orientation='vertical', size_hint=(1, .3))
        save_button = Button(text='SAVE', font_size=15, size_hint=(1, .1))
        save_as_button = Button(text='SAVE AS', font_size=15, size_hint=(1, .1))
        empty_space2 = BoxLayout(orientation='vertical', size_hint=(1, .3))
        back_button = Button(text='BACK', font_size=15, size_hint=(1, .1))

        share_box.add_widget(view_recents_button)
        share_box.add_widget(empty_space)
        share_box.add_widget(save_button)
        share_box.add_widget(save_as_button)
        share_box.add_widget(empty_space2)
        share_box.add_widget(back_button)

        self.root_layout.add_widget(share_box)



    def view_recents(self, controller, event):
        controller.initialize_recents_page()


    def add_watermark(self):
        pass

