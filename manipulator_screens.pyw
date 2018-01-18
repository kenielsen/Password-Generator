from tkinter import *
from popup import Popup
from password_generation import CombinationManipulator, WordManipulator
# word_manipulation_screen
class WordScreen(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self._word_var = StringVar()
        self._count_var = StringVar()
        self._manipulator = WordManipulator()
        self._lb = None
        self._init_screen()
        

    def _init_screen(self):
        f1 = Frame(self)
        Label(f1, textvariable=self._count_var, anchor=W).pack(fill=X)
        self._update_count()
        f1.pack(fill=BOTH)

        f2 = Frame(self)
        Label(f2, text="Enter a Word to Add:").pack(side=LEFT)
        e = Entry(f2, textvariable=self._word_var)
        e.pack(side=LEFT)
        e.focus_set()
        Button(f2, text="Add", command=self.add_word, bg='lightgreen').pack(side=LEFT)
        f2.pack(fill=BOTH)

        f3 = Frame(self)
        scrollbar = Scrollbar(f3)
        scrollbar.pack(side=RIGHT, fill=Y)
        self._lb = Listbox(f3, bd=0, yscrollcommand=scrollbar.set)
        self._lb.bind("<Double-1>", lambda x: self.delete_word(self._lb.curselection()[0]))
        self._lb.pack(fill=BOTH)
        scrollbar.config(command=self._lb.yview)
        for word in self._manipulator.read():
            self._lb.insert(END, word)
        f3.pack(fill=BOTH, expand=YES)
        
        self.pack(fill=BOTH, expand=YES)

    def count(self):
        return self._manipulator.count()

    def add_word(self):
        word = self._word_var.get()
        if self._manipulator.add(word):
            self._lb.insert(END, word)
            self._update_count()
            self._word_var.set("")
        else:
            Popup(self.master.master, "Error", "You cannot add %s to the list" % word)

    def delete_word(self, idx):
        word = self._lb.get(idx)
        if self._manipulator.delete(idx):
            self._lb.delete(idx)
            self._update_count()
        else:
            Popup(self.master.master, "Error", "You cannot remove %s from the list" % word)

    def _update_count(self):
        self._count_var.set("There are %d words in your list." % self.count())
        
        
class CombinationScreen(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self._separator_var = StringVar()
        self._length_var = StringVar()
        self._count_var = StringVar()
        self._manipulator = CombinationManipulator()
        self._init_screen()

    def _init_screen(self):
        self._separator_var.set("&")
        self._length_var.set("")
        
        f1 = Frame(self)
        Label(f1, textvariable=self._count_var, anchor=W).pack(fill=X)
        self._update_count()
        f1.pack(fill=BOTH)

        f2 = Frame(self)
        sf1 = Frame(f2)
        ssf1 = Frame(sf1)
        Label(ssf1, text="Enter separator:", anchor=W).pack(side=LEFT)
        Entry(ssf1, textvariable=self._separator_var, width=3).pack(side=LEFT)
        ssf1.pack(fill=BOTH, expand=YES)        
        ssf2 = Frame(sf1)
        Label(ssf2, text="Enter Number of Words:").pack(side=LEFT)
        Spinbox(ssf2, textvariable=self._length_var, width=3, from_=3, to=self._count_words()).pack(side=LEFT)
        ssf2.pack(fill=BOTH, expand=YES)
        sf1.pack(side=LEFT, fill=BOTH, expand=YES)
        sf2 = Frame(f2, bg="green")
        Button(sf2, text="GENERATE!", bg='lightgreen', font=("", 16), command=self.new).pack(fill=BOTH, expand=YES)
        sf2.pack(side=LEFT, fill=BOTH, expand=YES)
        f2.pack(fill=BOTH, expand=YES)


        f4 = Frame(self)
        #Button(f4, text="GENERATE!", font=("", 16), command=self.new).pack(fill=BOTH, expand=YES)
        Button(f4, text="View A- Password", font=("", 16), command=lambda: self.view(-1)).pack(fill=BOTH, expand=YES)
        Button(f4, text="View Password", font=("", 16), command=lambda: self.view(-2)).pack(fill=BOTH, expand=YES)
        f4.pack(fill=BOTH, expand=YES)
        
        self.pack(fill=BOTH, expand=YES)

    def count(self):
        return self._manipulator.count()

    def view(self, index):
        Popup(self.master.master, "View Combination", self._manipulator.view(index))

    def new(self):
        separator = self._separator_var.get()
        length = eval(self._length_var.get())
        combo = self._manipulator.generate(separator, length)
        self.view(-1)
        self._update_count()
        self._separator_var.set("&")
        self._length_var.set("")

    def _count_words(self):
        w = WordManipulator()
        return w.count()

    def _update_count(self):
        self._count_var.set("You have used %d passwords." % self.count())
