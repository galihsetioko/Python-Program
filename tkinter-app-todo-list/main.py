from tkinter import *
from tkinter import ttk , font
import tkinter
from tkinter import messagebox

root = Tk()
root.title('To Do List App')

def add():
    box.insert(END, enter.get())

def delete():
    try:
        box.delete(box.curselection()[0])
    except IndexError:
        messagebox.showwarning('Warning', 'Pilih Data Dalam Tabel !!')

def allDell():
    box.delete(0, END)
        
font_use = font.Font(family='arial', size=15, weight='bold')
frame = ttk.Frame(root, padding=20)
label = ttk.Label(frame, text='To Do List', font=font_use)
enter = ttk.Entry(frame, width=50)
button_add = ttk.Button(frame, command=add, text='Tambah')
box = tkinter.Listbox(frame, width=50)
button_delete = ttk.Button(frame, command=delete , text='Hapus')
button_all_delete = ttk.Button(frame, command=allDell , text='Hapus Semua')

frame.pack()
label.pack(pady=20)
enter.pack()
button_add.pack(pady=10)
box.pack(pady=20)
button_delete.pack(pady=20)
button_all_delete.pack()

root.mainloop()