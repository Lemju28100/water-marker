from tkinter import Grid, PhotoImage, messagebox
import tkinter as tk 
from tkinter import filedialog
from PIL import Image
from choose_account_page import ChooseAccountPage
import os
import platform


user_email = ''
counter = ''
SIZE_TO_DISPLAY = (650, 600)
   
  
LARGEFONT =("Verdana", 35) 
   
class App(tk.Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs)
       
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  


   
        # initializing frames to an empty array 
        self.frames = {}  

        # set app to full screen 
        self.attributes("-fullscreen", True)
        self.update()

        self.window_height = self.winfo_height()
        self.window_width = self.winfo_width()
        print(self.window_height)
        window_info = (self.window_width, self.window_height)
        print(window_info)
        self.update()

        # Set Minimum size of the window
        self.min_width = self.window_height
        self.min_height = self.window_width
        self.minsize(self.min_width, self.min_height)
        
        




        self.choose_accounts_page = ChooseAccountPage(container, self, window_info=window_info)
        self.choose_accounts_page.grid(row=0, column=0, sticky="nsew")

        self.bind('<Escape>', self.exit_full_screen)

   
        # iterating through a tuple consisting 
        # of the different page layouts 
        # for F in (self.choose_accounts_page):       
        #     F.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(self.choose_accounts_page) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        # frame = self.frames[cont]
        if cont == 'Register Page':
            self.register_page.tkraise() 
        elif cont == 'Sign In Page':
            self.signin_page.tkraise()
        elif cont == 'Home Page':
            self.home_page.tkraise()
        else:
            cont.tkraise()



    # Toggle fullscreen
    def exit_full_screen(self, o):
        self.destroy()
    



