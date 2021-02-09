from App import App





app = App() 

app.mainloop() 

# import tkinter

# class simpleapp_tk(tkinter.Tk):
#     def __init__(self,parent):
#         tkinter.Tk.__init__(self,parent)
#         self.parent = parent
#         self.initialize()

#     def initialize(self):
#         self.grid()
#         self.bind('<Escape>', self.exit_full_screen)
#         self.bind('<F11>', self.go_full_screen)

#         label = tkinter.Label(self,anchor="center",bg="green")
#         label.grid(column=0,row=0,sticky='NSEW')

#         label2 = tkinter.Label(self,anchor="center",bg="black")
#         label2.grid(column=1,row=0,sticky='NSEW')

#         label3 = tkinter.Label(self,anchor="center",bg="red")
#         label3.grid(column=2,row=0,sticky='NSEW')

#         label4 = tkinter.Label(self,anchor="center",bg="purple")
#         label4.grid(column=0,row=1,sticky='NSEW')

#         label5 = tkinter.Label(self,anchor="center",bg="blue")
#         label5.grid(column=1,row=1,sticky='NSEW')

#         label6 = tkinter.Label(self,anchor="center",bg="yellow")
#         label6.grid(column=2,row=1,sticky='NSEW')


#         self.grid_columnconfigure(0,weight=1)
#         self.grid_columnconfigure(1,weight=1)
#         self.grid_columnconfigure(2,weight=1)
#         self.grid_rowconfigure(0,weight=1)
#         self.grid_rowconfigure(1,weight=1)

#     def exit_full_screen(self, o):
#         self.geometry(f"{self.min_width}x{self.min_height}")
#         self.attributes('-fullscreen', False)
#         self.update()

#     def go_full_screen(self, o):
#         self.attributes("-fullscreen", True)
#         self.update()

# if __name__ == "__main__":
#     app = simpleapp_tk(None)
#     app.attributes('-fullscreen', True)
#     app.title("Test App")
#     app.mainloop()





        

   