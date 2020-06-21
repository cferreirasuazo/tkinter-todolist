import tkinter as tk
#Class to represent a TO-DO
class Todo():
    def __init__(self,master,todo_str):
        self.text = "todo"
        self.masterFrame = master
        self.frame = tk.Frame(master=master)
        self.label = tk.Label(master=self.frame,text=todo_str)
        self.delete_btn = tk.Button(master=self.frame,text="Done")
    
    #Renders the TO-DO
    def render(self):
        self.label.grid(row=0)
        self.delete_btn.grid(row=0,column=1)
        self.frame.pack()

       