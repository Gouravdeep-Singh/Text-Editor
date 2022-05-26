import tkinter
from tkinter import *
from tkinter import messagebox,filedialog
import os

#creating a function that contains all the widgets
def createwidget():
    global text
    text=tkinter.Text(x)
    text.pack(fill=tkinter.BOTH,expand=True)
    text.focus_set()

    menubar=tkinter.Menu(x)#creating a single menu that conatins all other menus
    x.config(menu=menubar)


    #CASCADE1: File
    file=tkinter.Menu(menubar,tearoff=0)
    file.add_command(label="New",command=New)
    file.add_command(label="Open",command=Open)
    file.add_command(label="Save",command=Save)

    file.add_separator()
    file.add_command(label="Exit",command=Exit)
    menubar.add_cascade(label="File",menu=file)

    #CASCADE 2: Edit
    edit=tkinter.Menu(menubar,tearoff=0)
    edit.add_command(label="Cut",command=cut)
    edit.add_command(label="Copy",command=copy)
    edit.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=edit)

    #CASCADE 3:Help
    help=tkinter.Menu(menubar,tearoff=0)
    help.add_command(label="About",command=Help)
    menubar.add_cascade(label="Help",menu=help)


def New():
    global text
    x.title("untitled")
    text.delete(1.0,END)

def Open():
    global text
    v=filedialog.askopenfile(defaultextension=".txt",filetype=[("All files",".")])
    v=v.name

    if v=="":
        v=None
    else:
      x.title(os.path.basename(v))
      text.delete(1.0,END)
      v=open(v,"r")#rb means read
      text.insert(1.0,v.read())
      v.close()



def Save():
    global text,v
    if v==None:
       v=filedialog.asksaveasfilename(initialfile="Untitled",filetype=[("All files",".")])
       if v==None:
           v=None
       else:
           v=open(v,"w")
           v.write(text.get(1.0,END))
           v.close()
           v=v.name
           x.title(os.path.basename(v))
    else:
        v=open(v,"w")
        v.write(text.get(1.0,END))
        v.close()


def Exit():
    x.destroy()

def cut():
    global text
    text.event_generate("<<Cut>>")

def copy():
    global text
    text.event_generate("<<Copy>>")

def paste():
    global text
    text.event_generate("<<Paste>>")

def Help():
    messagebox.showinfo("Notice","still working on it, advancements left")

x=tkinter.Tk()
x.title("Notepad")
x.geometry("600x500")
v=None#setting a variable to none
createwidget()
x.mainloop()
