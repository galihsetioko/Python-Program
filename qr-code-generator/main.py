from tkinter import *
from tkinter import ttk
from tkinter import font , messagebox
import qrcode
import os, random


def code(teks):
    
    current_dir = os.getcwd()
    current_dir1 = os.path.join(current_dir, 'picture')
    try:
        os.mkdir(current_dir1)
    except FileExistsError:
        pass 
    random_name = random.randint(1,1000)
    file_loc = os.path.join(current_dir1, str(random_name))
    text_to_encode = teks
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text_to_encode)
    qr.make(fit=True)
    
    name = random
    # Membuat gambar QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Menyimpan gambar QR code
    label.pack_forget()
    input_user.pack_forget()
    button.pack_forget()
    img.save(f'{file_loc}.png')
    label.config(text=f"File Saved at\n{file_loc}.png")
    label.pack(pady=10)
    input_user.pack(pady=10)
    button.pack()
    

    
    
def getCode():
  input_user.pack_forget()
  button.pack_forget()
  label.pack()
  input_user.pack(pady=10)
  button.pack()
  button.config(command=getCode)
  print(button.pack_info)
  teks = input_user.get()
  code(teks)


root = Tk()
root.tk.call('source', r'QR Code Generator\Forest-ttk-theme-master\forest-dark.tcl')
root.title("QR Code Generator")
root.geometry('300x300')
ttk.Style().theme_use('forest-dark')
mainframe = ttk.Frame(root, padding=20)
# canvas qrcode
# canvas = Canvas(mainframe, width=180, height=180, background='white')
label = ttk.Label(mainframe, text='', justify='center', wraplength=250)
# myimg = PhotoImage(file='pretty.png')
# canvas.create_image(10, 10, image=myimg, anchor='nw')
count = IntVar()
count.set(0)
input_user = ttk.Entry(mainframe)
button = ttk.Button(mainframe, text='Get Code', command=getCode)

mainframe.pack()
input_user.pack(pady=10)
button.pack()

root.mainloop()
