from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self,master):      #where <master> is the parent object
        self.label = ttk.Label(master, text="Hello, Gary!")
        self.label.grid(row=0, column=0,columnspan=2)

        ttk.Button(master, text="Fuck Sundays!", command=self.sundayHello).grid(row=1,column=0)
        ttk.Button(master, text="Fuck Currys!", command=self.currysHello).grid(row=1,column=1)

    #setters
    def sundayHello(self):
        self.label.config(text="Yes, fuck working on Sundays!")

    def currysHello(self):
        self.label.config(text="Such a shit hole!")

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# root = Tk()     # root is an instance of Tk() class, the main window object or top level window
# button = ttk.Button(root, text="click your mom")
# button.pack()
# button['text'] = 'press your nipple'
# button.config(text="'Lick the door handle'")
# print( button.config() )
#
#
# ttk.Label(root, text="Hello, Tkinter!").pack()
# root.mainloop()
