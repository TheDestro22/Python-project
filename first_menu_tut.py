import tkinter as tk
from   tkinter import *

class Student:
    def __init__(self, first_menu) :
        self.first_menu = first_menu
        self.first_menu.geometry('2048x1536+1+1')
        self.first_menu.title('FCAI-CU Hub')
        self.first_menu.configure(background = 'silver')

first_menu = Tk()
student_menu = Student(first_menu)
first_menu.mainloop()
