import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import json
from settings import *


# Functions
class Extra(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__(master = parent)
        self.geometry("300x200")
        self.resizable(False,False)
        self.attributes('-topmost', 'true')

        #layout
        self.columnconfigure((0,1,2),weight=1)
        self.rowconfigure((0,1,2,3),weight=1,uniform="a")

# Main app
class App(ctk.CTk):

    def __init__(self):

        # window setup
        super().__init__()
        ctk.set_default_color_theme("dark-blue")
        self.title("Mobilit-e")
        self.geometry("300x120")
        self.resizable(False,False)

        #layout
        self.columnconfigure(0,weight=1)
        self.rowconfigure((0,1,2,3),weight=1,uniform="b")

        #widgets
        self.username_input = UsernameInput(self)
        self.password_input = PasswordInput(self)
        LoginButton(self, self.username_input, self.password_input)
        ReadButton(self)
        RegButton(self) # Still testing
        ChangeTheme(self)

        self.mainloop()

class LoginButton(ctk.CTkButton):
    def __init__(self,parent, username_input, password_input):
        super().__init__(master = parent, text = "Login")
        font = ctk.CTkFont(family = "Consolas", size = 20, weight = "bold")
        self.grid(column=0,row=2,rowspan=1,sticky="nsew",padx=2,pady=2)
        self.username_input = username_input
        self.password_input = password_input

        self.configure(command=self.login_clicked)

    def login_clicked(self):
        username = self.username_input.get()
        password = self.password_input.get()

        filename = "credentials.json"

        try:
            with open(filename, "r") as file:
                json_data = file.read()
                if json_data:
                    data = json.loads(json_data)
                else:
                    data = {}
        except FileNotFoundError:
            data = {} 

        data[username] = password

        with open(filename, "w") as file:
            json.dump(data, file,indent=4)

class ReadButton(ctk.CTkButton):
    def __init__(self,parent):
        super().__init__(master = parent, text = "Read Data \nFrom Users")
        font = ctk.CTkFont(family= "Consolas", size = 25, weight = "bold")
        self.grid(column=1,row=0,rowspan=2,sticky="nsew",padx=5,pady=5)

        self.configure(command=self.read_data)


    def read_data(self): 
        filename = "credentials.json"

        with open(filename, "r") as file:
            json_data = file.read()

        data = json.loads(json_data)

        for username, password in data.items():
            print("Username:", username)
            print("Password:", password)
            print("---------------------")

# Opens new window
class RegButton(ctk.CTkButton):
    def __init__(self,parent):
        super().__init__(master = parent, text = "Register")
        font = ctk.CTkFont(family = "Consolas", size = 25, weight = "bold")
        self.grid(column=1,row=2,rowspan=1,sticky="nsew",padx=2,pady=2)
        
        self.configure(command=self.open_reg)

    # Cria nova janela para fazer registo
    def open_reg(self):
        extra_window = Extra(self.master)
        name = ctk.CTkEntry(master=extra_window, placeholder_text="Name")
        username = ctk.CTkEntry(master=extra_window, placeholder_text="Username")
        email = ctk.CTkEntry(master=extra_window, placeholder_text="Email")
        password = ctk.CTkEntry(master=extra_window, placeholder_text="Password")
        name.grid(column=1,row=0,sticky="ew")
        username.grid(column=1,row=1,sticky = "ew")
        email.grid(column=1,row=2,sticky = "ew")
        password.grid(column=1,row=3,sticky = "ew")
        
        reg_button = ctk.CTkButton(master=extra_window,text="Register")
        reg_button.grid(column=1,row=4,sticky = "ew")

class UsernameInput(ctk.CTkEntry):
    def __init__(self,parent):
        super().__init__(master = parent,placeholder_text="Username")
        self.grid(column=0,row=0,rowspan=1,sticky="nsew")

class PasswordInput(ctk.CTkEntry):
    def __init__(self,parent):
        super().__init__(master = parent,placeholder_text="Password",show="*")
        self.grid(column=0,row=1,rowspan=1,sticky="nsew")      

class regClient(ctk.CTk):
    def __init__(self,parent):
        super().__init__(master = parent)
        def register_client():
            # Open new window to register new user
            register_window = ctk.CTkToplevel(self)
            register_window.title("Login")
            register_window.geometry("250x200")
            register_window.maxsize(width=250,height=200)

            #Creates grid
            register_window.grid_columnconfigure(0, weight=1)
            register_window.grid_rowconfigure(1, weight=1)
            
            user_input = ctk.CTkEntry(register_window,placeholder_text="Username")
            user_input.grid(column=0,row=0,padx=5,pady=5,sticky="ew")
            pw_input = ctk.CTkEntry(register_window,placeholder_text="Password",show="*")
            pw_input.grid(column=0,row=1,padx=5,pady=5,sticky="ew")
            email_input = ctk.CTkEntry(register_window,placeholder_text="Email")
            email_input.grid(column=0,row=2,padx=5,pady=5,sticky="ew")
            submit_login = ctk.CTkButton(register_window,text="Login")
            submit_login.grid(column=0,row=3,padx=10,pady=10,sticky="nsew")

class ChangeTheme(ctk.CTkSwitch):
    def __init__(self,parent):
        super().__init__(master = parent,
                     text="Theme",
                     onvalue = "on",
                     offvalue = "off")
        self.grid(column=0,row=3,sticky = "ws")
        self.configure(command=self.switch_theme)
        self.toggle()
    
        
    def switch_theme(self):
        if self.get() == "on":
            ctk.set_appearance_mode('dark')
        else:
            ctk.set_appearance_mode('light')


    

# Window
if __name__ == "__main__":
    App()
