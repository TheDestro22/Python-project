import tkinter as tk

from tkinter import PhotoImage as ph

first_menu = tk.Tk()

first_menu.geometry("800x500")

first_menu.configure(background = 'lightblue')

first_menu.title("FCAI-CU")

buttonframe = tk.Frame(first_menu)



main_label = tk.Label(first_menu, text = "FCAI-CU Hub", font = ('Times New Roman', 28)).pack()

control_button = tk.Button(first_menu, text = "Control Staff" , font = ('Arial' , 18)).pack()

student_button = tk.Button(first_menu, text = "Student" , font = ('Arial' , 18)).pack()

first_menu.mainloop()