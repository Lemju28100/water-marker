import tkinter as tk 
from tkinter import Canvas, ttk
from PIL import Image


LARGEFONT =("Verdana", 15) 

# third window frame page2 
class HomePage(tk.Frame):  
    def __init__(self, parent, controller): 

        tk.Frame.__init__(self, parent) 
        