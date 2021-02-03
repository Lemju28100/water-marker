from tkinter import PhotoImage, messagebox
from dns.tsig import sign
from mysql.connector import connection
from RegisterPage import RegisterPage
from HomePage import HomePage
from SigninPage import SigninPage
import tkinter as tk 
import mysql.connector
from mysql.connector import errorcode
import bcrypt
from tkinter import filedialog
from PIL import Image
import os, glob

user_email = ''

try:
  cnx = mysql.connector.connect(user='elema', database='water_marker', host='127.0.0.1', password='Sk1dragonro@r', use_pure=True)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
# else:
#   cnx.close()

# Driver Code 
   
  
LARGEFONT =("Verdana", 35) 
   
class PageController(tk.Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs)
        global cnx
        self.connection = cnx
          
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
        self.config(padx=10, pady=5)
        self.title("WaterMarker.ai")
   
        # initializing frames to an empty array 
        self.frames = {}   
        self.signin_page = SigninPage(container, self, signin_action=self.sign_user_in)

        self.register_page = RegisterPage(container, self, register_action = self.register_user)

        self.home_page = HomePage(container, self, 
        next_action=self.next_to_select_watermark_position,
        add_image_action=self.add_image_to_watermark,
        logout_action=self.logout,
        display_images_action=self.display_images,
        delete_account_action=self.delete_account
        )
        

   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (self.signin_page, self.register_page, self.home_page):       
            F.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(self.home_page) 
   
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
        
    def get_hashed_password(self, plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(self, plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password, hashed_password)
    
    # register user to database
    def register_user(self):
        
        creds = self.register_page.check_valid_fields()
        if creds == []:
            return
        else:
            # retrieve credentials from register page/ class
            email = creds['email']
            password = creds['password']

            # check if email exists in db
            cur = cnx.cursor()
            sql = 'SELECT email FROM users WHERE email = %s'
            cur.execute(sql, (email,))
            db_email = cur.fetchall()
            if len(db_email) > 0:
                go_to_login = messagebox.askokcancel(title="Email already exists", message="This email already exists. Login instead?")
                if go_to_login:
                        self.show_frame(self.signin_page)
                        return
                else:
                    return
                

            #Adding user to db 
            sql = 'INSERT INTO users (email, pwd) VALUES (%s, %s)'         
            cur.execute(sql, (email, self.get_hashed_password(password),))
            cnx.commit()
            self.show_frame(self.home_page)

    def sign_user_in(self):
        
        creds = self.signin_page.check_valid_fields()
        if creds == []:
            return
        else:
            #retrieve credentials from signin page/class
            email = creds['email']
            password = creds['password']
            print(email)
            print(password)

            #check if email exists
            cur = cnx.cursor()
            sql = 'SELECT email FROM users WHERE email = %s'
            cur.execute(sql, (email,))
            db_email = cur.fetchall()
            if len(db_email) < 1:
                go_to_register = messagebox.askokcancel(title="Register?", message="This email does not exist. Do you want to register instead?")
                if go_to_register:
                    self.show_frame(self.register_page)
                    return
                else:
                    return

            else:
                #check if the password matches one from db
                sql = 'SELECT pwd FROM users WHERE email = %s'
                cur.execute(sql, (email,))
                db_password = cur.fetchall()[0][0]
                if not self.check_password(password, self.get_hashed_password(password)):
                    messagebox.showinfo(title="Incorrect Password", message="Your Password is incorrect. Please try again")
                    return
                else:
                    USER_EMAIL = email
                    self.show_frame(self.home_page)

                    # Finish Checking password

    def logout(self):
        is_logout = messagebox.askokcancel(title='Logout?', message='Are you sure you want to logout?')
        if is_logout:
            self.show_frame(self.signin_page)
            cnx.close()
        else:
            return

    def display_images(self):
        pass
    
    def next_to_select_watermark_position(self):
        pass

    def delete_account(self):
        global user_email
        is_delete = messagebox.askokcancel(title='Delete Account???', message='Are you sure you want to delete this accout')
        if is_delete:
            is_ok = messagebox.askokcancel(title='Permanent Delete!!!', message='Do you really want to delete your account?? Account deletion cannot be reversed! All your images will be lost')
            if is_ok:
                cur = cnx.cursor()
                sql = ('DELETE FROM users WHERE email=%s')
                cur.execute(sql, (user_email,))
                self.show_frame(self.signin_page)
                cnx.close()
            else:
                return
        else:
            return


    def add_image_to_watermark(self):
        # Empty the temp path


        # Ask user for Image file
        file_path = filedialog.askopenfilename()
        print(file_path)

        # Open the file with image module
        try:
            uploaded_image = Image.open(file_path)
        except UnicodeDecodeError:
            messagebox.showinfo(title='Not an Image!', message='Please upload an image')
            return

        # resize the image just for display to user
        img = uploaded_image
        img = img.resize((350, 300))
        tmp_img_path = 'temp/display_image.png'
        img.save(tmp_img_path)

        # Replace the button with image 
        
        loaded_uploaded_image = PhotoImage(tmp_img_path)
        self.loaded_uploaded_image = loaded_uploaded_image
        self.home_page.add_img_button.config(image=self.loaded_uploaded_image)

        # TODO Display the selected image by emptying the temp filepath.
        # TODO Make sure you delete everything in temp directory only when image processing is complete.





        

   