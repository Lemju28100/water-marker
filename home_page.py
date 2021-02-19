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
from kivy.uix.popup import Popup
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


class HomePage(Screen):
    def __init__(self, page_controller, user, **kw):
        super().__init__(**kw)
        self.name = 'home_page'
        self.user = user
        self.user_path = f'{os.getcwd()}/users/{self.user}'
        self.file_path = ''


        # Set bg color
        self.bg_image = Image(source='data/home_background.png', allow_stretch=True,
        keep_ratio = False)
        self.add_widget(self.bg_image)
        self.pi_has_uploaded = False

        self.load_images(page_controller=page_controller)
        self.load_add_image_gui()
        self.next_to_edit_screen = Button(text="Next", pos_hint={'x': .83, 'y': 0.05}, size_hint = (.15, .1), font_size=20, disabled=True, on_release = partial(self.load_editor_screen, page_controller))

        color_list = {'a': '#e28cd0', 'b':'#3ebf62', 'c': '#cd3190', 'd': '#363670', 'e': '#d6b750', 'f': '#4b8ce3', 'g': '#966a99', 'h': '#f80912', 'i': '#9a6278', 'j': '#a6bd05', 'k': '#579ccd', 'l': '#894cd5', 'm': '#bbea2e', 'n': '#87fcb1', 'o': '#14566d', 'p':'#39316d', 'q': '#fea6cb', 'r': '#51bea4', 's': '#335e25', 't': '#fc7a39', 'u': '#bff6ed', 'v': '#c9737a', 'w': '#e56b0e', 'x': '#5f0c25', 'y': '#abccea', 'z': '#becb47'}
        accounts_page_button = Button(background_color = color_list[self.user.lower()[0]], pos_hint={'x': .85, 'y': 0.85}, size_hint = (.1, .1), text=self.user[0].capitalize(), font_size = 20, border=(10, 10, 10, 10), on_release=partial(self.load_accounts_page, page_controller))
        self.add_widget(accounts_page_button)

        self.add_widget(self.next_to_edit_screen)



    
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
        
        add_image_box = BoxLayout(orientation='vertical', size_hint=(.5, .80), pos_hint={'x': .27, 'y': .05})
        self.add_image_button_bg = Image(source='data/add_background.png', allow_stretch=True, keep_ratio=False)

        add_image_button = Button(text='ADD YOUR IMAGE', font_size=20, pos_hint={'x': .3, 'y': 0.85}, size_hint = (.4, .1), on_release=self.add_image)
        self.add_widget(add_image_button)

        add_image_box.add_widget(self.add_image_button_bg)

        self.add_widget(add_image_box)

    def get_image_url(self):
        return self.file_path
    
    def load_accounts_page(self, controller, event):
        controller.initialize_accounts_page()

    
    def add_image(self, event):
        image_is_uploaded = False

        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename()
        
        supported_image_extensions = ['jpg', 'jpeg', 'png']

        for extension in supported_image_extensions:
            if str(self.file_path).endswith(extension):
                image_is_uploaded = True


        if self.file_path == '':
            return

        if image_is_uploaded:

            self.add_image_button_bg.source = self.file_path
            self.add_image_button_bg.allow_stretch = False
            self.next_to_edit_screen.disabled = False

        else:
        
            warning_popup = Popup(title='Photo not Entered', size_hint=(0.5, 0.5))
                

            warning_content= BoxLayout(orientation='vertical', size_hint=(.9, .9), spacing=10, pos_hint={'x':.4, 'y':0})
            warning_label = Label(text='Please choose a photo', font_size=16, size_hint=(.9, .2))
            ok_button = Button(text='OK', size_hint= (.9, .1), on_release=warning_popup.dismiss)

            warning_content.add_widget(warning_label)
            warning_content.add_widget(ok_button)
            warning_popup.add_widget(warning_content)
            warning_popup.open()
            
            

        


    def load_recents_page(self, page_controller, event):
        page_controller.initialize_recents_page()



    
    def load_editor_screen(self, controller, event):
        controller.initialize_editor_page()
            
            
