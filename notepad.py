from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.font
root = Tk()
def new():
    global file
    root.title("Untitled-Notepad")
    file = None
    text.delete(1.0, END)
def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = ".txt", filetypes =[("Allfiles", "*.*"), ("Text documnets", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("file has been saved")
    else:
        #save the files
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()
def opn():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All files", "*.*"), ("Text documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def delete():
    text.delete(1.0, END)
def about():
    tmsg.showinfo("notepad", "This notepad GUI is created by Ritik")
root.geometry("655x343")
root.title("Text Editor")
root.configure(bg = "grey")
root.wm_iconbitmap("notepad.ico")
#menu start
menu1 = Menu(root)
#file menu
submenu1 = Menu(menu1, tearoff = 0)
submenu1.add_command(label = "New", command = new)
submenu1.add_command(label = "Open", command = opn)
submenu1.add_command(label = "Save", command = save)
submenu1.add_separator()
submenu1.add_command(label = "Exit", command = quit)
root.config(menu = menu1)
menu1.add_cascade(label = "File", menu = submenu1)
#edit menu
submenu2 = Menu(menu1, tearoff = 0)
submenu2.add_command(label = "Cut", command = cut)
submenu2.add_command(label = "Copy", command = copy)
submenu2.add_command(label = "Paste", command = paste)
submenu2.add_separator()
submenu2.add_command(label = "Delete", command = delete)
menu1.add_cascade(label = "Edit", menu = submenu2)
#help menu
submenu4 = Menu(menu1, tearoff = 0)
submenu4.add_command(label = "About", command = about)
menu1.add_cascade(label = "Help", menu = submenu4)
frame = Frame(root)
scrollbar1 = Scrollbar(frame)
scrollbar1.pack(side = RIGHT, fill = Y)
fnt = StringVar(frame)
fnt.set("helvetica")
file = None
text = Text(frame, width = 655, height = 343, font = f"{fnt.get()} 15", bg = "grey24", fg = "aliceblue", yscrollcommand = scrollbar1.set)
text.pack(fill = BOTH)
scrollbar1.config(command = text.yview)
lbl1 = Label(root, text = f"    python GUI       UTF- 8", padx = 20, bg = "grey20", fg = "white", bd = 2, anchor = "e").pack(side = BOTTOM, fill = X)
frame.pack(fill = "both")
root.mainloop()
