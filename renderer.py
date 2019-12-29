from tkinter import *
from tkinter.ttk import *

class Renderer(Frame):
    window_manager = Tk()
    window_manager.title("four function calculator")
    
    def __init__(self):
        super().__init__(self.window_manager)
        self.pack()
        self.create_widgets()

    def start(self):
        self.mainloop()

    def create_widgets(self):
        self.hi_there = Button(self, text = "Hello World", command = self.say_hi)
        self.hi_there.pack(side="top")

    def say_hi(self):
        print("hi there, everyone!")