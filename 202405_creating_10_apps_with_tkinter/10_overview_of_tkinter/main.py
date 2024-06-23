import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles = float(entry_int.get())
    km = miles * 1.60934
    output_string.set(km)


window = ttk.Window(themename="journal")
window.title("Demo")
window.geometry('800x400')

title_label = ttk.Label(master=window, text="Miles to kilometers", font='Calibri 24 bold')
title_label.pack()

input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side=tk.LEFT, padx=10)
button.pack(side=tk.LEFT)
input_frame.pack(pady=10)

output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font='Calibri 24', textvariable=output_string)
output_label.pack(pady=5)

window.mainloop()
