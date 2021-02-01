import tkinter as tk 
from tkinter import ttk 

LARGEFONT =("Verdana", 35) 

# third window frame page2 
class HomePage(tk.Frame):  
    def __init__(self, parent, controller): 

        from SigninPage import SigninPage
        from RegisterPage import RegisterPage


        tk.Frame.__init__(self, parent) 
        # label = ttk.Label(self, text ="Home page", font = LARGEFONT) 
        # label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        # # button to show frame 2 with text 
        # # layout2 
        # button1 = ttk.Button(self, text ="Register Page", 
        #                     command = lambda : controller.show_frame(RegisterPage)) 
      
        # # putting the button in its place by  
        # # using grid 
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   
        # # button to show frame 3 with text 
        # # layout3 
        # button2 = ttk.Button(self, text ="Signin Page", 
        #                     command = lambda : controller.show_frame(SigninPage)) 
      
        # # putting the button in its place by 
        # # using grid 
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10) 