from logging import NullHandler
from os import kill
import re
import tkinter as tk 
from tkinter import PhotoImage, ttk
from tkinter.constants import NW 
from PIL import Image
from tkinter import messagebox


LARGEFONT =("Verdana", 35) 
   
class SigninPage(tk.Frame): 
    def __init__(self, parent, controller, signin_action):  

                
        from HomePage import HomePage
        from RegisterPage import RegisterPage
          
        
        tk.Frame.__init__(self, parent)
        self.signin_action = signin_action


        # Configure welcome canvas
        canvas = tk.Canvas(self, height=100, width=100)

        img = Image.open('signin.png')
        img = img.resize((90, 100))
        img.save('signin.png')

        signin_image = tk.PhotoImage(file='signin.png')
        self.signin_image = signin_image
        canvas.create_image(50, 50, image=signin_image)

        canvas.grid(column=2, row=1)
        

        # Buttons
        register_button = tk.Button(self, fg="white", bg="blue", text ="Register Instead?", 
        command = lambda : controller.show_frame('Register Page')) 
        register_button.grid(row = 0, column = 4, padx = 2, pady = 2) 
   
        sign_in_button = tk.Button(self, text ="Sign in", bg="green", command=self.signin_action,
         fg="white", width=35).grid(row = 5, column = 1, pady = 5, columnspan=2) 


        # Input fields
        username_field = ttk.Entry(self, width=35)
        password_field = ttk.Entry(self, width=35)
        self.email = username_field
        self.email.grid(columnspan=2, column=1, row=3)
        self.email.focus()
        self.password = password_field
        self.password.grid(columnspan=2, column=1, row=4)

        # Labels
        username_label = ttk.Label(self, text="Enter Email").grid(column=0, row=3, pady=5)
        password_label = ttk.Label(self, text="Enter Password").grid(column=0, row=4, pady=5)
        intro_label = ttk.Label(self, text="AUTO WATERMARK YOUR IMAGES").grid(column=2, row=0, padx=5, pady=5)
        sign_in_label = ttk.Label(self, text="SIGN IN").grid(column=2, row=2, columnspan=2)

    def check_valid_fields(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email = self.email.get()
        password = self.password.get()

        if email == '' or password == '':
            messagebox.showinfo(title='Empty Fields', message="Please enter all fields")
            return []

        if not re.search(regex, email):
            messagebox.showinfo(title="Invalid email", message="Please enter a valid email")
            return []
        
        return {'email': self.email, 'password':self.password}
        

 
