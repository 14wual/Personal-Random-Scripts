import customtkinter
import sqlite3

from pages import today
from pages import add

def main(self):
    
    self.main_frame = customtkinter.CTkFrame(self)
    self.main_frame.pack(padx=5, pady=5)
    
    today.tasks(self)
    add.add_task(self)