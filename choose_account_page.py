from logging import NullHandler
from os import kill
import re
import tkinter as tk 
from tkinter import Button, PhotoImage, ttk
from tkinter.constants import ANCHOR, CENTER, NW, TOP 
from PIL import Image
from tkinter import messagebox
import os


LARGEFONT =("Verdana", 35) 
FONT_RATIOS = 0.03
PRIMARY_COLOR = '#1F9BD9'
BUTTON_RATIOS = 0.1
   
class ChooseAccountPage(tk.Frame): 
    def __init__(self, parent, controller, window_info):  
          
        
        tk.Frame.__init__(self, parent)
        self.window_width = window_info[0]
        self.window_height = window_info[1]
        # print(self.window_height)
        
        
        # Add background image
        filename= 'data/app_background.png'
        backgroud_img = Image.open(fp=filename)
        resized_image = backgroud_img.resize((self.window_width, self.window_height))
        resized_image.save(fp=filename)
        bg_image = tk.PhotoImage(file=filename)
        self.bg_image = bg_image
        background_label = tk.Label(parent, image=bg_image)
        background_label.place(relx=0.5, rely=0.5, anchor='center')

        #buttons 
        signin_frame = tk.Frame(self, bg='red')
        signin_frame.place(relheight=0.3, relwidth=0.5)
        user_path = f"{os.getcwd()}/users"

        
        for root, subdirectories, files in os.walk(user_path):
            for subdirectory in subdirectories:
                signin_button = ttk.Button(signin_frame, text=subdirectory.upper())
                signin_button.pack()
                print(os.path.join(root, subdirectory))

                # signin_button.pack()
            

        


        register_button = tk.Button(self, fg="white", bg="blue", text ="Register Instead?", 
        command = lambda : controller.show_frame('Register Page')) 
        


        