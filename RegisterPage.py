import tkinter as tk 
from tkinter import  ttk
from tkinter import messagebox
from PlaceHolder import EntryWithPlaceholder
from PIL import Image
import re

LARGEFONT =("Verdana", 35) 

# second window frame page1  
class RegisterPage(tk.Frame): 
      
    def __init__(self, parent, controller, register_action):

        from HomePage import HomePage
        from SigninPage import SigninPage 
          
        tk.Frame.__init__(self, parent) 
        self.register_action = register_action

         # Configure welcome canvas
        canvas = tk.Canvas(self, height=100, width=100)

        img = Image.open('data/signup.png')
        img = img.resize((90, 100))
        img.save('data/register.png')

        signin_image = tk.PhotoImage(file='data/register.png')
        self.signin_image = signin_image
        canvas.create_image(50, 50, image=signin_image)

        canvas.grid(column=2, row=1)
        

        # Buttons
        signin_button = tk.Button(self, fg="white", bg="green", text ="Sign in Instead?", 
        command = lambda : controller.show_frame("Sign In Page")) 
        signin_button.grid(row = 0, column = 4, padx = 2, pady = 2) 
   
        register_button = tk.Button(self, text ="REGISTER", bg="blue", command=self.register_action,
         fg="white", width=35).grid(row = 6, column = 1, pady = 5, columnspan=2) 


        # Input fields
        username_field = EntryWithPlaceholder(self, placeholder='Must be email')
        username_field.config(width=35)
        username_field.grid(columnspan=2, column=1, row=3)
        self.email = username_field
        self.email.focus()

        password_field = EntryWithPlaceholder(master=self, placeholder="Must be atleast 8 characters")
        password_field.config(width=35)
        password_field.grid(columnspan=2, column=1, row=4)
        self.password = password_field

        confirm_password_field = EntryWithPlaceholder(self, placeholder='Must be same as password')
        confirm_password_field.config(width=35)
        confirm_password_field.grid(columnspan=2, column=1, row=5)
        self.confirm_password = confirm_password_field
        

        # Labels
        username_label = ttk.Label(self, text="Enter Email").grid(column=0, row=3, pady=5)
        password_label = ttk.Label(self, text="Enter Password").grid(column=0, row=4, pady=5)
        intro_label = ttk.Label(self, text="AUTO WATERMARK YOUR IMAGES").grid(column=2, row=0, padx=5, pady=5)
        register_label = ttk.Label(self, text="REGISTER").grid(column=2, row=2, columnspan=2)
        confirm_password_label = ttk.Label(self, text="Confirm Password").grid(column=0, row=5, pady=5)

    def check_valid_fields(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        email = self.email.get()
        password = self.password.get()
        confirm_password = self.confirm_password.get()


        if email == '' or password == '' or confirm_password == '':
            messagebox.showinfo(title='Empty Fields', message="Please enter all fields")
            return []

        if not re.search(regex, email):
            messagebox.showinfo(title="Invalid email", message="Please enter a valid email")
            return []

        if len(password) < 8:
            messagebox.showinfo(title="Weak Password!", message="Please enter at least 8 characters for your password")
        
        if password != confirm_password:
            messagebox.showinfo(title="Passwords not equal", message="Please enter the same passwords")
            return []
        
        
        return {'email': email, 'password':password}
        