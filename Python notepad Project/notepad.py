from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
root.title("Untitled - Notepad")
root.geometry("640x750")
root.wm_iconbitmap("note.ico")
textarea=Text(root,font=("lucida",13))
file=None
textarea.pack(expand=True,fill=BOTH)


def newFile():
    global file
    root.title("Untitle - Notepad")
    file=None
    textarea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()


def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
          file=None
        else:
          f=open(file,"w")
          f.write(textarea.get(1.0,END))
          f.close()
          root.title(os.path.basename(file) + " - Notepad")
          print("file Saved")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()




def exitFile():
    root.destroy()

def cutFile():
    textarea.event_generate(("<<Cut>>"))

def copyFile():
    textarea.event_generate(("<<Copy>>"))


def pasteFile():
    textarea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad","Notepad by Sunny Suman")


menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="new",command=newFile)
filemenu.add_command(label="open",command=openFile)
filemenu.add_command(label="save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exitFile)
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="cut",command=cutFile)
editmenu.add_command(label="copy",command=copyFile)
editmenu.add_command(label="paste",command=pasteFile)
menubar.add_cascade(label="Edit",menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About Notepad",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

root.configure(menu=menubar)

scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.configure(command=textarea.yview)
textarea.configure(yscrollcommand=scroll.set)

root.mainloop()
