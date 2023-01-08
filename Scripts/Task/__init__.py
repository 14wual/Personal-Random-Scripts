# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Tasks
# See proyect >> https://github.com/14wual/Personal-Random-Scripts/tree/main/Scripts/Task
# Follow me >> https://twitter.com/codewual

# --------------------Extern Imports--------------------
import customtkinter

# ----------Intern Imports--------------------
from pages import today
from pages import add

# --------------------APP--------------------
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk example")
        customtkinter.set_appearance_mode("light")

        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(padx=5, pady=5)
        
        today.tasks(self)
        add.add_task(self)

if __name__ == '__main__':
    app = App()
    app.mainloop()
