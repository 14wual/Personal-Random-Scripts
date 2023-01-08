import customtkinter
import sqlite3

def tasks(self):
    
    result = []
    
    self.tasks_frame = customtkinter.CTkFrame(self.main_frame)
    self.tasks_frame.grid(row=1,column=0,padx=10,pady=10, rowspan=2)
    
    conn = sqlite3.connect("ddbb/task.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ntasks")
    result = cursor.fetchall()

    if result == []:
        
        from PIL import Image
        self.done_image = customtkinter.CTkImage(light_image=Image.open("images\done.png"),
                                            size=(50,50))
        
        self.no_task_label_image = customtkinter.CTkLabel(self.tasks_frame,text="", image=self.done_image)
        self.no_task_label_image.pack(padx=15, pady=15)
        
        self.no_task_label = customtkinter.CTkLabel(self.tasks_frame,text="No Tasks")
        self.no_task_label.pack(padx=5, pady=5)
        
    else:
        
        for row in result:
            
            self.task_button = customtkinter.CTkButton(self.tasks_frame,text=row[1],
                command=lambda row=row:task_event(self,row))
            self.task_button.pack(padx=5, pady=5)
            
    conn.close()

def task_event(self,row):
    
    window1 = customtkinter.CTkToplevel(self)
            
    window1.title("Task")

    title_task = customtkinter.CTkLabel(window1, text=row[1],font=customtkinter.CTkFont(weight="bold"))
    title_task.pack(side="top", fill="both", expand=False, padx=10, pady=10)
    
    details_task = customtkinter.CTkTextbox(window1)
    details_task.pack(side="top", fill="both", expand=False, padx=10, pady=10)
    details_task.insert("0.0", row[3])
    details_task.configure(state="disabled")
    
    date_task = customtkinter.CTkLabel(window1, text=row[0])
    date_task.pack(side="top", fill="both", expand=False, padx=10, pady=10)
    
    delete_task = customtkinter.CTkButton(window1, text="Mark as done!",
        command=lambda row=row:event_delete_task(row))
    delete_task.pack(side="top", fill="both", expand=False, padx=10, pady=10)
    
def event_delete_task(row):
    
    conn = sqlite3.connect("ddbb/task.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ntasks WHERE num = ?",row[2])
    result = cursor.fetchall()