from tkinter import * 
from tkinter.filedialog import *

def open_file():
    file = askopenfile(title = "open file") #by default if you do not specify the mode or type of file it will be read and all type
    if file is not NONE:
        content = file.read()
        print(content)

def save_file():
    file = asksaveasfile(defaultextension = ".txt")
    if file is not NONE:
        pass

def add_items():
    list_box.insert(END, entry.get())
    entry.delete(0, END)

window = Tk()
window.title("Memoriser")
window.geometry("390x350")

file_frame = Frame(window)

file_save = Button(file_frame, text = "Save", font = ("times", 20), width = 15, command = save_file).grid(row = 1, column = 1)
file_open = Button(file_frame, text = "Open", font = ("times", 20), width = 15, command = open_file).grid(row = 1, column = 2)

file_frame.grid(row = 1, column = 1)

list_frame = Frame(window)

list_delete = Button(list_frame, text = "Delete", font = ("times", 20), width = 15).grid(row = 3, column = 2)
list_add = Button(list_frame, text = "Add", font = ("times", 20), width = 15, command = add_items).grid(row = 2, column = 2)
entry = Entry(list_frame, width = 20)

list_frame.grid(row = 2, column = 1)

list_box_frame = Frame(window)

list_box = Listbox(list_box_frame, width = 40, height = 12)

for i in range(1,21):
    list_box.insert(END, f"List {i} ")

list_box.grid(row = 1, column = 1)

list_box_frame.grid(row = 3, column = 1, pady = 20, padx = 10)

entry.grid(row = 2, column = 1, ipady = 6)

window.mainloop()