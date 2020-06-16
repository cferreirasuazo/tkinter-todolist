import tkinter as tk
from Todo import Todo

class MainFrame():
    def __init__(self, window):
        self.counter = 0
        self.todos = []
        self.todos_frames = []
        self.MAX_TASK = 15
        self.title = tk.Label(master=window, text = "Todo-List")
        self.title.pack()
        self.frame = tk.Frame(master=window,width=300, height=500,background='red') 
        self.frame.pack()
        self.input = tk.Text(master=self.frame, width=40, height=2)
        self.input.pack()
        self.add_todo_btn = tk.Button(master=self.frame, text="Add Todo")
        self.add_todo_btn.bind('<Button-1>',self.addTodo)
        self.add_todo_btn.pack()
        self.todos_container = tk.Frame(master=self.frame)
        self.todos_container.pack()

    def start(self):
        self.frame.pack()

    def catchEvent(self,e):
        child = str(e.widget).split(".")[3]

        for i in self.todos_frames:
            todo = str(i).split(".")[3]
            if todo == child:
                i.destroy()
        

    def print_todo(self,e):
        print(e)

    def addTodo(self,e):
        
        str = self.input.get("0.0","end").replace('\n',"")
        self.todos.append(str)
        if str:
            new_todo = Todo(self.todos_container,str)
            self.todos_frames.append(new_todo.frame)
            new_todo.delete_btn.bind("<Button-1>",self.catchEvent)
            new_todo.show_todo()
            self.input.delete("0.0","end")      
        
        for i in enumerate(self.todos_frames):
            print(i)

    def appendTodos(self,todos):
        self.todos = [todo.replace("\n","") for todo in todos]

        for todo in todos:
            new_todo = Todo(self.todos_container,todo.replace("\n",""))
            new_todo.delete_btn.bind("<Button-1>",self.catchEvent)
            self.todos_frames.append(new_todo.frame)
            new_todo.show_todo()

       