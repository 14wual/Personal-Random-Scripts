import customtkinter


from pages import main

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk example")
        customtkinter.set_appearance_mode("light")

        main.main(self)

if __name__ == '__main__':
    app = App()
    app.mainloop()