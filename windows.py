from tkinter import *

def display_greating():
    greeting_label.config(text="halo, selamat datang!")

wcindow = Tk()
window.title("program sambutan")

greeting_label = label(window, text="")
greeting_label.pack(pady=20)

greet_button = Button(window, text="tampilkan sambutan", command=)
greet_button.pack

window.mainloop()