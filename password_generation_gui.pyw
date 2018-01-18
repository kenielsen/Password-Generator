from tkinter import *
from popup import Popup
from manipulator_screens import CombinationScreen, WordScreen
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
                  highlightthickness=1)
        self._content.pack(fill=BOTH, expand=YES)
        
        self.main_screen()
        
    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Main", command=self.main_screen)
        file_menu.add_command(label="Passwords", command=lambda: self.set_screen(Type.PASSWORD))
        file_menu.add_command(label="Words", command=lambda: self.set_screen(Type.WORD))
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
                                    lambda: self.set_screen(Type.PASSWORD), bg='gold')
        self._add_full_width_button("Word List Manipulation", 16,
                                    lambda: self.set_screen(Type.WORD), bg='darkorchid')
        self._add_full_width_button("About", 16, self.about, bg='royalblue')
        self._add_full_width_button("Exit", 16, self.client_exit, bg='firebrick')

    def set_screen(self, content_type):
        self._clear_content()
        self._set_title("Words" if content_type == Type.WORD else "Passwords")

        if content_type == Type.WORD:
            WordScreen(self._content)
        elif content_type == Type.PASSWORD:
            CombinationScreen(self._content)
        
        self._add_full_width_button("Back", 14, self.main_screen)

    def about(self):
        Popup(self, "About", ABOUT_TEXT)
        

    def _add_full_width_button(self, text, font_size, command=None, adjust_height = True, bg=None):
        button = Button(self._content,text = text,
                    font=(DEFAULT_FONT, font_size),
                    command=command, bg=bg)
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
        

root = Tk()

app = PasswordGenerationApp(root)
root.mainloop()
