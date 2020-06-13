import tkinter as tk

class Todo():
    def __init__(self,master,todo_str):
        self.text = "todo"
        self.masterFrame = master
        self.frame = tk.Frame(master=master)
        self.label = tk.Label(master=self.frame,text=todo_str)
        self.delete_btn = tk.Button(master=self.frame,text="Done")
        self.delete_btn.bind("<Button-1>",self.delete_todo)
    
    def show_todo(self):
        self.label.grid(row=0)
        self.delete_btn.grid(row=0,column=1)
        self.frame.pack()

    def delete_todo(self,e):
        self.frame.destroy()
        
       