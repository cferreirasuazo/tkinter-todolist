 # for btn in main.winfo_children(): /* PRINTS ALL  CHILDREN OF THE FRAME*/
    #     print(btn['text'])        /*RETURNS THE NAME OF THE WIDGET*/

#print(e.widget.cget("text")) /*WHEN CLICK IN A EVENT, RETURNS THE TEXT OF THE WIDGET CLIEKCED*/

# def delete(e):
#     print(e.widget.cget("text"))
#     print(e.widget)
#     # for child in main.winfo_children():
#     #     print(child.cget("text"))

# for btn in btns:
#     new_btn = tk.Label(main,text=btn)
#     new_btn.bind("<Button-1>",delete)
#     new_btn.pack()


# Get the parent of a widget
# parent = event.widget.winfo_parent()


todoFile = "todoFile.txt"


openFile = open(todoFile,"r")


def readFile(todoFile):
    pass

import tkinter as tk
from MainFrame import MainFrame

main = tk.Tk()
main.title("TODO-LIST")
mainFrame = MainFrame(main)
mainFrame.appendTodos(openFile.readlines())
mainFrame.start()

main.mainloop()




