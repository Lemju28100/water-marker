import tkinter as tk 
from tkinter import Canvas, ttk
from PIL import Image
from dns.flags import to_text


LARGEFONT =("Verdana", 15) 

# third window frame page2 
class AddLogoPage(tk.Frame):  
    def __init__(self, parent, controller, back_to_select_image, add_logo, add_text, remove_watermark, process_image): 

        tk.Frame.__init__(self, parent)

        self.back_to_select_image = back_to_select_image
        self.add_logo = add_logo
        self.add_text = add_text
        self.remove_watermark = remove_watermark
        self.process_image = process_image

        # Buttons
        add_logo_button = ttk.Button(self, text='ADD LOGO', width=15, command=self.add_logo)
        add_logo_button.grid(row=0, column=1)

        back_button =ttk.Button(self, text='Back', width=15, command=self.back_to_select_image)
        back_button.grid(row=4, column=0)

        add_text_button = ttk.Button(self, text='ADD TEXT', width=15, command=self.add_text)
        add_text_button.grid(row=0, column=2)

        remove_water_mark_button = ttk.Button(self, text='REMOVE WATERMARK', command=self.remove_watermark)
        remove_water_mark_button.grid(row=0, column=3)

        process_button = ttk.Button(self, text='ADD WATERMARK', command = self.process_image)
        process_button.grid(row=4, column=4)

        # Canvas
        self.canvas = Canvas(self, width=550, height=600)
        self.canvas.grid(row=1, rowspan=3, column=0, columnspan=4)
        

        