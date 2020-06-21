import tkinter as tk
from Todo import Todo

class MainFrame():
    def __init__(self, window):
        self.todos_frames = [] #Saves the TO-DOs
        self.MAX_TASK = 15 # Limit of TO-DOs
        self.title = tk.Label(master=window, text = "Todo-List")
        self.title.pack()
        self.frame = tk.Frame(master=window) 
        self.frame.pack()
        self.input = tk.Text(master=self.frame, width=40, height=2)
        self.input.pack()
        self.add_todo_btn = tk.Button(master=self.frame, text="Add Todo")
        self.add_todo_btn.bind('<Button-1>',self.addTodo)
        self.add_todo_btn.pack()
        self.todos_container = tk.Frame(master=self.frame)
        self.todos_container.pack()

    #Renders the main frame
    def render(self):
        self.frame.pack()

    #deletes a TO-DO
    def deleteTodo(self,e):
        child = str(e.widget).split(".")[3]
        #Get's the parent of the clicked button, and search it in the todo_frames 
        #and deletes it 
        for i in self.todos_frames:
            todo = str(i).split(".")[3]
            if todo == child:
                i.destroy()

    def addTodo(self,e):
        
        #Get's the string from the input
        str = self.input.get("0.0","end").replace('\n',"")
        if str:

            new_todo = Todo(self.todos_container,str)
            new_todo.delete_btn.bind("<Button-1>",self.deleteTodo)
            self.todos_frames.append(new_todo.frame)
            new_todo.render()

            self.input.delete("0.0","end")      


    #Gets the TO-DOs from a file and renders when in the main frame
    def appendTodos(self,todos):
        self.todos = [todo.replace("\n","") for todo in todos]
        for todo in todos:

            new_todo = Todo(self.todos_container,todo.replace("\n",""))
            new_todo.delete_btn.bind("<Button-1>",self.deleteTodo)
            self.todos_frames.append(new_todo.frame)
            new_todo.render()

       