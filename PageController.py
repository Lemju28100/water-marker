from tkinter import messagebox
from dns.tsig import sign
from mysql.connector import connection
from RegisterPage import RegisterPage
from HomePage import HomePage
from SigninPage import SigninPage
import tkinter as tk 
import mysql.connector
from mysql.connector import errorcode
import bcrypt


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
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (SigninPage, HomePage, RegisterPage): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
            
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(SigninPage) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 

    def get_hashed_password(self, plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(self, plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password, hashed_password)
    
    # register user to database
    def register_user(self):
        register_page = self.frames[RegisterPage]
        creds = register_page.check_valid_fields()
        if creds == []:
            return
        else:
            # retrieve credentials from register page/ class
            email = creds.email
            password = creds.password

            # check if email exists in db
            cur = cnx.cursor()
            sql = 'SELECT email FROM users WHERE email = %s'
            db_email = cur.execute(sql, email)
            
            if len(db_email) > 0:
                go_to_login = messagebox.askokcancel(title="Email already exists", message="This email already exists. Login instead?")
                if go_to_login:
                        self.show_frame(SigninPage)
                        return
                else:
                    return
                

            #Adding user to db          
            cur.execute(f'INSERT INTO users (email, pwd) VALUES {email}, {self.get_hashed_password(password)}')
            cnx.commit()
            self.show_frame(HomePage)

    def sign_user_in(self):
        signin_page = self.frames[SigninPage]
        creds = signin_page.check_valid_fields()
        if creds == []:
            return
        else:
            #retrieve credentials from signin page/class
            email = creds.email
            password = creds.password

            #check if email exists
            cur = cnx.cursor()
            db_creds = cur.execute(f'SELECT email, pwd FROM users WHERE email = f{email}')
            if len(db_creds < 1):
                go_to_register = messagebox.askokcancel(title="Register?", message="This email does not exist. Do you want to register instead?")
                if go_to_register:
                    self.show_frame(RegisterPage)
                    return
                else:
                    return

            else:
                #check if the password matches one from db

                if len(db_password) < 1:
                    messagebox.showinfo(title="Incorrect Password")
                    # Prevent sql injection
                    # Finish Checking password

        

   