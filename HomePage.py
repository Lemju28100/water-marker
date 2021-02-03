import tkinter as tk 
from tkinter import Canvas, ttk
from PIL import Image


LARGEFONT =("Verdana", 15) 

# third window frame page2 
class HomePage(tk.Frame):  
    def __init__(self, parent, controller, logout_action, display_images_action, delete_account_action, next_action, add_image_action): 

        from SigninPage import SigninPage
        from RegisterPage import RegisterPage


        tk.Frame.__init__(self, parent) 

        self.logout_action = logout_action
        self.display_images_action = display_images_action
        self.delete_account_action = delete_account_action
        self.next_action = next_action
        self.add_img_action = add_image_action

        # labels
        self.welcome_label = ttk.Label(self, text="Welcome User. WaterMark Your Image", font=LARGEFONT) #Configure this in page controller to say actual name of person
        self.welcome_label.grid(row=0, column=2, columnspan=2)

        # buttons
        images_button = ttk.Button(self, text='Images', width=15, command=self.display_images_action)
        images_button.grid(column=0, row=1)

        delete_button = ttk.Button(self, text='Delete Account', width=15, command=self.delete_account_action)
        delete_button.grid(column=0, row=5)

        signout_button = ttk.Button(self, text='Log out', width=15, command=self.logout_action)
        signout_button.grid(column=5, row=1)



        next_button = ttk.Button(self, text='NEXT', width=15, command=self.next_action)
        next_button.grid(column=5, row=5)

        img = Image.open('data/add_img.png')
        img = img.resize((350, 300))
        img.save('data/add_img.png')

        add_img = tk.PhotoImage(file='data/add_img.png')
        self.add_img = add_img
        add_img_button = ttk.Button(self, image=self.add_img, command=self.add_img_action)
        self.add_img_button = add_img_button
        add_img_button.grid(row=1, column=2, rowspan=3, columnspan=3, padx=10, pady=10)




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