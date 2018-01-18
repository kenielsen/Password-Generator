from tkinter import *
class Popup(Toplevel):
    def __init__(self, master=None, title=None, content=None):
        Toplevel.__init__(self, master)
        self.title(title)
        self.geometry("250x125")
        self.transient(master)
        l = Label(self, text=content, bg='white')
        l.pack(ipadx=50, ipady=10, fill=BOTH, expand=True)
        b = Button(self, text="OK", command=self.destroy)
        b.pack(pady=10, padx=10, ipadx=20, side=RIGHT)
