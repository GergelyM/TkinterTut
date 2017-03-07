#imports
import os
from tkinter import *
from tkinter import ttk

#functions and methods
def callbackText():
    statusBar.config(text='Clicked')

def closeToplevel():
    login.destroy()

#GUI generators

root = Tk()
#Window header text / window name
root.wm_title("Tutorial 1")
#set min size of the window
root.minsize(width=800, height=600)
#window status bar
statusBar = Label(root, text="", bd=1, relief=GROOVE, anchor=CENTER)
#relief is simulated 3D effect FLAT,RAISED,SUNKEN,GROOVE,RIDGE
#anchors are used to define where text is positioned relative to a reference point
statusBar.pack(side=BOTTOM, fill=X)


button = Button(root, text='Click me')
button.config( command = callbackText )
button.pack()

login = Toplevel(root)
login.wm_title("Toplevel test")

#top1.geometry(x = 200, y = 300)

top1LabelUid = Label(login, text="User ID").grid(row=1, pady=10, sticky=E)
top1LabelUpw = Label(login, text="Password").grid(row=2, pady=10, sticky=E)

top1EntryUid = ttk.Entry(login).grid(row=1, column=1, columnspan=2, padx=5)
top1EntryUpw = ttk.Entry(login).grid(row=2, column=1, columnspan=2)

top1Button1 = ttk.Button(login, text="Cancel", command=closeToplevel).grid(row=3, column=1, pady=10)
top1Button2 = ttk.Button(login, text="Login").grid(row=3, column=2)



login.attributes('-topmost', True) #brings toplevel window to the top
login.focus_force()  #gives focus to toplevel window
login.grab_set() # disables main window until toplevel closed or given back by .grab_release()
#top1.grab_release() # to return to normal

#set position of toplevel to middle of root
#root.winfo_x(), root.winfo_y()
#x = root.winfo_x()
#y = root.winfo_y()
# wid = top1.winfo_width()
# hei = top1.winfo_height()
# top1.geometry("%dx%d+%d+%d" % (wid, hei, x + 30, y + 30))
#top1.geometry("150x200+%d+%d" % (x+30, y+30))


#hook main window to the main event handler loop
root.mainloop()
