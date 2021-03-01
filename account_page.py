from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.uix.textinput import TextInput
import string
from pathlib import Path

from kivy.graphics.context_instructions import Color
from kivy.uix.image import Image
from kivy.uix.popup import Popup


from functools import partial

import os



class AccountPage(Screen):
    def __init__(self, page_controller, **kw):
        super().__init__(**kw)

        # Initialize Accounts
        self.accounts = []

        # Add a background image
        self.bg_image = Image(source='data/app_background.png', allow_stretch=True,
        keep_ratio = False)
        self.add_widget(self.bg_image)

        # Add an 'Add Account Label'
        self.add_account_label = Label(text='Choose Account', font_size=30, pos_hint={'x': 0, 'y': .07})
        self.add_widget(self.add_account_label)


        self.generate_account_buttons(page_controller)
        

        


    def generate_account_buttons(self, page_controller):

        # generate layout for account buttons
        accounts_box = BoxLayout(orientation = 'vertical', spacing= 10, size_hint=(.3, .4), pos_hint={'x': .34, 'y': .1})

        # get current directory
        self.current_directory = f'{os.getcwd()}/users'


        # define current username
        self.user = ''
        self.name = 'account_page'
        self.number_of_accounts= 0

        # iterate through user directories
        for subdir, dir, files in os.walk(self.current_directory):
            
            if len(dir) > 0:
                print('this is ' + str(dir))


                for directory_name in dir:
                    if directory_name == 'watermarks' or directory_name == 'images':
                        continue
                    else:
                        account_button = Button(text=directory_name.upper(), size_hint=(1, 1),
                        on_release = partial(self.authenticate, directory_name.lower(), page_controller),
                        background_normal='',
                        background_color='#00BFF3',
                        border=(1, 1, 1, 1),
                        font_size=20)
                        accounts_box.add_widget(account_button)
                        self.accounts.append(directory_name.lower())
                        self.number_of_accounts = len(dir)
            else:
                self.add_account_label.text = ''

        # Add add button to add account
        add_account_button = Button(text='ADD ACCOUNT',
         size_hint=(1, 1), on_release=partial(self.add_account, page_controller))

        if self.number_of_accounts < 3:
            accounts_box.add_widget(add_account_button)
        
        self.add_widget(accounts_box)

    
    def authenticate(self, username, page_controller, event):
        # set user equal to username on button cliked
        self.user = username
        print(self.user)
        
        
        

        # go to second screen
        page_controller.initialize_home_page()
        
    
    def get_user(self):
        return self.user

    
    def add_account(self, page_controller, event):

        self.add_account_pop = Popup(title='Add account', size_hint=(0.4, 0.4))

        pop_up_content = BoxLayout(orientation='vertical', size_hint=(.9, .9), spacing=10, pos_hint={'x':.4, 'y':0})

        add_button = Button(text='ADD', size_hint= (.9, .2), on_release=partial(self.validate_add_account_input, page_controller))

        cancel_button = Button(text='CANCEL', size_hint=(.9, .2), on_release=self.add_account_pop.dismiss)
        self.account_name_input = TextInput(size_hint=(.9, .2), font_size=25, hint_text='Only letters. At least 3')

        pop_up_content.add_widget(self.account_name_input)
        pop_up_content.add_widget(add_button)
        pop_up_content.add_widget(cancel_button)
        
        self.add_account_pop.add_widget(pop_up_content)

        
        self.add_account_pop.open()



    def validate_add_account_input(self, page_controller, e):

        warning_popup = Popup(title='', size_hint=(0.5, 0.5))

        name_entered = self.account_name_input.text
        

        warning_content= BoxLayout(orientation='vertical', size_hint=(.9, .9), spacing=10, pos_hint={'x':.4, 'y':0})
        warning_label = Label(text='', font_size=16, size_hint=(.9, .2))
        ok_button = Button(text='OK', size_hint= (.9, .1), on_release=warning_popup.dismiss)

        warning_content.add_widget(warning_label)
        warning_content.add_widget(ok_button)
        warning_popup.add_widget(warning_content)


        alphabet = list(string.ascii_lowercase)
        print(alphabet)
        if name_entered == '':
            warning_popup.title = 'Empty Entry'
            warning_label.text = 'Please enter a username'
            warning_popup.open()

            return

        if name_entered in self.accounts:
            warning_popup.title = 'Name already exists'
            warning_label.text = 'Please enter a different username'
            self.account_name_input.text = ""
            warning_popup.open()
            return
        
        if len(name_entered) < 3:
            warning_popup.title = 'Number of letters too low'
            warning_label.text = 'Please enter 3 letters or more'
            self.account_name_input.text = ""
            warning_popup.open()
            return



        for i in range(len(name_entered)):
            if not name_entered[i].lower() in alphabet:
                warning_popup.title = 'Invalid username'
                warning_label.text = 'Please enter only letters of the alphabet'
                self.account_name_input.text = ''
                warning_popup.open()
                return

        user_directory_to_make = f'{self.current_directory}/{name_entered.lower()}'
        Path(user_directory_to_make).mkdir(parents=True, exist_ok=True)

        user_images_path = f'{user_directory_to_make}/images'
        user_watermark_path = f'{user_directory_to_make}/watermarks'

        Path(user_images_path).mkdir(parents=True, exist_ok=True)
        Path(user_watermark_path).mkdir(parents=True, exist_ok=True)

        self.add_account_pop.dismiss()
        self.user = name_entered.lower()

        page_controller.initialize_home_page()


        
        

        


            


        

    




    

                
                
        