from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from account_page import AccountPage
from home_page import HomePage
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from recents_page import RecentsPage
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from editor_page import EditorPage

import time
import random


class PageController(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


       
        self.account_page = AccountPage(page_controller=self)

        #TODO uncomment this line after testing editor page
        # self.switch_to(self.account_page)

        #TODO remove this line below after testing editor page
        self.initialize_editor_page()

        

        
        print(self.account_page.get_user())
    
    def initialize_home_page(self):
        current_user = self.account_page.get_user()
        self.home_page = HomePage(page_controller=self, user=current_user)
        self.switch_to(self.home_page)

    def initialize_recents_page(self):
        current_user = self.account_page.get_user()
        self.recents_page = RecentsPage(page_controller=self, user=current_user)
        self.switch_to(self.recents_page)

    def initialize_accounts_page(self):
        self.switch_to(self.account_page)

    def initialize_editor_page(self):
        #TODO uncomment the two lines below

        # current_user = self.account_page.get_user()
        # img_url = self.home_page.get_image_url()
        
        #TODO add user=current_user and img_url =img_url
        self.editor_page = EditorPage(page_controller=self)
        self.switch_to(self.editor_page)
            