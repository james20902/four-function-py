from tkinter import *
from tkinter.ttk import *

class Renderer(Frame):
    def __init__(self, name, width, height, resizable):
        self.window_manager = Tk()
        self.window_manager.title(name)
        self.window_manager.geometry(f"{width}x{height}")
        if not resizable:
            self.window_manager.resizable(0, 0)

        super().__init__(self.window_manager)
        self.pack()
        self.draw_elements()
        self.update_window("hello world")

    def start(self):
        self.mainloop()

    def draw_elements(self):
        self.windowvar = StringVar()
        self.window = Label(textvariable = self.windowvar)
        self.window.pack(side="top")

    def update_window(self, message):
        self.windowvar.set(message)