from tkinter import *
from password_generation import count_words, count_combos
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
        self.content = Frame(self, highlightbackground="black", highlightcolor="black",\
                  highlightthickness=1, bg="antiquewhite")
        self.content.pack(fill=BOTH, expand=YES)
        
        self.main_screen()
        
    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        password_menu=Menu(menu, tearoff=0)
        password_menu.add_command(label="View Password")
        password_menu.add_command(label="New Password")

        word_list_menu = Menu(menu, tearoff=0)
        word_list_menu.add_command(label="List Words", command=self.word_list_list_screen)
        word_list_menu.add_command(label="Modify List")

        file_menu = Menu(menu, tearoff=0)
        file_menu.add_cascade(label="Passwords", menu=password_menu)
        file_menu.add_cascade(label="Word List", menu=word_list_menu)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file_menu)
        
        help_menu = Menu(menu, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menu.add_cascade(label="Help", menu=help_menu)
        
    def main_screen(self):
        self._clear_content()
        self._set_title("Main")
        self._current_page="main"
        
        self._add_full_width_button("Password Manipulation", 16,
                                    self.password_main_screen)
        self._add_full_width_button("Word List Manipulation", 16,
                                    self.word_list_main_screen)
        self._add_full_width_button("Exit", 16, self.client_exit)

    def password_main_screen(self):
        self._clear_content()
        self._set_title("Password Manipulation")
        self._current_page="password_main"

        self._add_full_width_button("Count Passwords Used", 14,
                                    lambda: self.count(Type.PASSWORD))
        self._add_full_width_button("View Password", 14)
        self._add_full_width_button("New Password", 14)
        
        self._add_full_width_button("Return to Main", 14, self.main_screen)

    def word_list_main_screen(self):
        self._clear_content()
        self._set_title("Word List Manipulation")
        self._current_page="word_list_main"

        self._add_full_width_button("Count Words", 14,
                                    lambda:self.count(Type.WORD))
        self._add_full_width_button("List Words", 14,
                                    self.word_list_list_screen)
        self._add_full_width_button("Modify Words", 14)
        
        self._add_full_width_button("Return to Main", 14, self.main_screen)

    def word_list_list_screen(self):
        self._clear_content()
        self._set_title("Word List View")
        self._current_page="word_list_list"
        f = Frame(self.content)
        Label(f, text="Enter a word to add:").pack(side=LEFT)
        Entry(f, textvariable=self._input1_var).pack(side=LEFT)
        Button(f, text="Add", command=lambda:self.add_word(self._input1_var.get())).pack(side=LEFT)
        f.pack(fill=BOTH, expand=1)
        self._add_full_width_button("Back", 13, self.word_list_main_screen)

    def about(self):
        Popup(self, "About", ABOUT_TEXT)

    def count(self, countType):
        num = 0
        title = ""
        form = "%d"
        if countType == Type.WORD:
            num = count_words()
            title, form = "Number of Words", "There are %d words in the list"
        elif countType == Type.PASSWORD:
            num = count_combos()
            title, form = "Number of Passwords", "You have used %d passwords"
        Popup(self, title, form % num)

    def add_word(self, word):
        pass

    def _add_full_width_button(self, text, font_size, command=None):
        button = Button(self.content,text = text,
                    font=(DEFAULT_FONT, font_size),
                    command=command)
        button.pack(fill=BOTH, expand=1)
       
    def _set_title(self, text):
        self._title_var.set(text)

    def _clear_content(self):
        for child in self.content.winfo_children():
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
