from tkinter import *
#from password_generation import count_words, count_combos, get_words, delete_word, add_word
import password_generation
from enum import Enum

class Type(Enum):
    WORD = 1
    PASSWORD = 2

ABOUT_TEXT = "A simple application to manage passwords.\n"+\
                "{0}2018 Kristen Nielsen".format(u"\u00A9") +\
                "\nkristen.e.nielsen@gmail.com"
DEFAULT_FONT = ""
class PasswordGenerationApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, width=500, height=300)
        self.master = master
        self._title_var = StringVar()
        self._input1_var = StringVar()
        self._current_page=""
        self.init_window()

    def init_window(self):
        self.master.title("Password Generation")
        self.pack(fill=BOTH, expand=YES)
        self.pack_propagate(0)
        
        self.create_menu()
        
        self.title = Label(self, textvariable=self._title_var,
                           font=(DEFAULT_FONT, 18))
        self.title.pack()
        self._content = Frame(self, highlightbackground="black", highlightcolor="black",\
                  highlightthickness=1, bg="antiquewhite")
        self._content.pack(fill=BOTH, expand=YES)
        
        self.main_screen()
        
    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        password_menu=Menu(menu, tearoff=0)
        password_menu.add_command(label="View Password")
        password_menu.add_command(label="New Password")

        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Main", command=self.main_screen)
        file_menu.add_cascade(label="Passwords", menu=password_menu)
        file_menu.add_command(label="Words", command=self.word_list_main_screen)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file_menu)
        
        help_menu = Menu(menu, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="Help", menu=help_menu)
        
    def main_screen(self):
        self._clear_content()
        self._set_title("Main")
        
        self._add_full_width_button("Password Manipulation", 16,
                                    self.password_main_screen)
        self._add_full_width_button("Word List Manipulation", 16,
                                    self.word_list_main_screen)
        self._add_full_width_button("Exit", 16, self.client_exit)

    def password_main_screen(self):
        self._clear_content()
        self._set_title("Password Manipulation")

        self._add_full_width_button("Count Passwords Used", 14,
                                    lambda: self.count(Type.PASSWORD))
        self._add_full_width_button("View Password", 14)
        self._add_full_width_button("New Password", 14)
        
        self._add_full_width_button("Return to Main", 14, self.main_screen)


    def word_list_main_screen(self):
        self._clear_content()
        self._set_title("Word List View")
        self._input1_var.set("")
        f = Frame(self._content)
        Label(f, text = "There are %d words in your list." % self.count(Type.WORD), anchor=W).pack(fill=X)
        f.pack(fill=BOTH)
        f = Frame(self._content)
        Label(f, text="Enter a word to add:").pack(side=LEFT)
        Entry(f, textvariable=self._input1_var).pack(side=LEFT)
        Button(f, text="Add", command=lambda:self.add_word(self._input1_var.get())).pack(side=LEFT)
        f.pack(fill=BOTH)
        f2=Frame(self._content)
        Label(f2, text="Double click a word to remove it", anchor=W).pack(side=TOP, fill=X)
        s = Scrollbar(f2)
        s.pack(side=RIGHT, fill=Y)
        l = Listbox(f2, bd=0, yscrollcommand=s.set)
        l.bind("<Double-1>", lambda x: self.delete_word(l.curselection()))
        l.pack(fill=BOTH)
        s.config(command=l.yview)
        for word in password_generation.get_words():
            l.insert(END, word)
        f2.pack(fill=BOTH, expand=1)
        self._add_full_width_button("Back", 13, self.main_screen, False)

    def about(self):
        Popup(self, "About", ABOUT_TEXT)

    def count(self, countType):
        num = 0
        title = ""
        form = "%d"
        if countType == Type.WORD:
            return password_generation.count_words()
        elif countType == Type.PASSWORD:
            num = password_generation.count_combos()
            title, form = "Number of Passwords", "You have used %d passwords"
        Popup(self, title, form % num)

    def add_word(self, word):
        password_generation.add_word(word)
        self.word_list_main_screen()

    def delete_word(self, word):
        password_generation.delete_word(word[0])
        self.word_list_main_screen()

    def _add_full_width_button(self, text, font_size, command=None, adjust_height = True):
        button = Button(self._content,text = text,
                    font=(DEFAULT_FONT, font_size),
                    command=command)
        if adjust_height:
            button.pack(fill=BOTH, expand=1)
        else:
            button.pack(fill=BOTH)
       
    def _set_title(self, text):
        self._title_var.set(text)

    def _clear_content(self):
        for child in self._content.winfo_children():
            child.destroy()

    def client_exit(self):
        self.master.destroy()

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

root = Tk()

app = PasswordGenerationApp(root)
root.mainloop()
