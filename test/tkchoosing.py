import tkinter as tk

window = tk.Tk()
window.geometry('400x180')


def select():
    dict = {1: 'male', 2: 'female'}
    strings = dict.get(v.get())
    SexEntry.config(text=strings)


SexEntry = tk.Label(window)
SexEntry.grid(row=2, column=2, padx=5, pady=5)
site = [('male', 1),('female', 2)]

v = tk.IntVar()
for name, num in site:
    radio_button = tk.Radiobutton(window, text=name, variable=v, value=num, command=select, indicatoron=False)
    radio_button.grid(row=3, column=num + 1, padx=5, pady=5)

window.mainloop()
