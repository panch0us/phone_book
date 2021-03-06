import tkinter
from tkinter import ttk

from tab_telephone import Telephone
from tab_calculations import Appg


class MainInterface:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('PanchProg')
        self.window.geometry("1200x690")
        self.window.resizable(width=False, height=False)
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5

        self.notebook = ttk.Notebook(self.window, width=1187, height=657)

        d_tab = Telephone(self.notebook)
        a_tab = Appg(self.notebook)

        self.notebook.add(d_tab, text="  Телефонный справочник  ")
        self.notebook.add(a_tab, text="  Вычисления  ")

        self.notebook.grid(row=1, column=1)


if __name__ == '__main__':
    program = MainInterface()
    program.window.mainloop()