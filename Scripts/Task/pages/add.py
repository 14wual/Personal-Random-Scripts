# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Tasks
# See proyect >> https://github.com/14wual/Personal-Random-Scripts/tree/main/Scripts/Task
# Follow me >> https://twitter.com/codewual

# This script is still under development

# --------------------Extern Imports--------------------
import sqlite3
import customtkinter
import tkinter as tk
from tkcalendar import DateEntry

# --------------------APP--------------------
def add_task(self):
    
    self.add_task_button = customtkinter.CTkButton(self.main_frame, text="Add Task",
        command=lambda:add_task_event(self))
    self.add_task_button.grid(row=3,column=0,padx=10,pady=10)
    
def add_task_event(self):
    
    self.add_task_frame = customtkinter.CTkFrame(self.main_frame)
    self.add_task_frame.grid(row=0,column=1,padx=10,pady=10, rowspan=3)
    
    self.title_task = customtkinter.CTkEntry(self.add_task_frame,placeholder_text="Title")
    self.title_task.grid(row=0,column=0,padx=10,pady=10)
    
    self.details_task = customtkinter.CTkTextbox(self.add_task_frame)
    self.details_task.grid(row=1,column=0,padx=10,pady=10)
    self.details_task.insert("0.0", "Details")
    
    self.date_var = tk.StringVar()
    self.date_entry = DateEntry(self.add_task_frame, width=12, background='white',
                       foreground='black', borderwidth=2, year=2023, month=1,
                       day=5, textvariable=self.date_var)
    self.date_entry.grid(row=2,column=0,padx=10,pady=10)
    
    self.add_task_event_button = customtkinter.CTkButton(self.add_task_frame,text="Create Task",
        command=lambda:create_task_event(self))
    self.add_task_event_button.grid(row=3,column=0,padx=10,pady=10)

def create_task_event(self):
    
    title = ""
    
    try:
        
        title = self.title_task.get()
        details = self.details_task.get()
        date = self.date_var.get()
        
    finally:
        
        if title == "":
            
            from PIL import Image

            warning_image = customtkinter.CTkImage(light_image=Image.open("images\warning.png"),
                                            size=(30, 30))
            
            window = customtkinter.CTkToplevel(self)
            window.title("[ERROR]")
            
            label = customtkinter.CTkLabel(window, text="",image=warning_image)
            label.pack(side="top", fill="both", expand=False, padx=10, pady=(10,0))

            label = customtkinter.CTkLabel(window, text="[ERROR] No Input Title",font=customtkinter.CTkFont(weight="bold"))
            label.pack(side="top", fill="both", expand=False, padx=10, pady=10)
        
        else:
            
            num = int("SELECT COUNT(*) FROM ntasks")+1
            
            conn = sqlite3.connect("ddbb/task.db")

            cursor = conn.cursor()
            cursor.execute("INSERT INTO ntasks (fecha, name, num, desc) VALUES (?, ?, ?, ?)",
                        (date, title, num, details))

            conn.commit()
            conn.close()
    
    self.add_task_frame.grid_forget()
