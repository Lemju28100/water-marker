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
from PIL import Image as Im
import tkinter as tk
from tkinter import filedialog

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

        back_button = Button(text='BACK TO HOME', font_size=14, size_hint = (.15, .1), pos_hint = {'x':.825, 'y':.07},
        on_release=partial(self.back_to_home, page_controller))
        self.add_widget(back_button)

    
    def load_all_images(self):

        images_box = GridLayout(cols=4, size_hint = (.8, 1), spacing=10, padding=5)
        images_path = f'{self.user_path}/images'

        dir_list = os.listdir(images_path)

        for i in range(len(dir_list)):
            img = Image(source=f'{images_path}/{dir_list[i]}', size_hint=(1, 1),
            keep_ratio = False, allow_stretch=True, on_press_down=self.save_image_as)

            images_box.add_widget(img)
        self.add_widget(images_box)

        
    def back_to_home(self, page_controller, event):
        page_controller.initialize_home_page()

    def save_image_as(self, image):
        image_source = image.source
        image_photo = Im.open(image_source)

        root = tk.Tk()
        root.withdraw()
        
        root = tk.Tk()
        root.withdraw()
        files = [('PNG Image', '*.png'), ('JPEG Image', '*.jpeg')] 
        f = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        if f is None:
            return
        else:

            image_photo.save(fp=f.name)
                
