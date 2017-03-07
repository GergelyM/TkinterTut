from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text="Hey Yo!")
label.pack()


label.config(text="Rendkivul hosszu es idegen nyelvu szoveg.")
label.config(wraplength = 100)           # text wrap width in pixels
label.config(justify = CENTER)           # defult text justified to left
label.config(foreground = "blue", background="yellow")           # defult text justified to left
label.config( font = ("Courier", 18, "bold") )           # set text type and weight // style is a different method

#picture1 = PhotoImage(file="APM_03.jpg")
#label.config(image=picture1)    # just using the nem of the image object, so it acts as a local variable
# label.config(compund = "text")  #
# label.config(compund = "center")
# label.config(compund = "left")

#label.img = picture1  # this creates a copy of the picture object in Tk
#label.config(image = label.img) #so the copy won't be garbage collected when the class, or fuction dies

root.mainloop()