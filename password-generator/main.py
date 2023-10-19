from tkinter import ttk 
from tkinter import *
import random , string

class Windows():
    root = Tk()
    mainframe = ttk.Frame(root, padding=20)
    root.tk.call('source', r'Forest-ttk-theme-master\forest-light.tcl')
    root.geometry('300x400')
    root.title('Create Your Password')
    ttk.Style().theme_use('forest-light')
    
    
    def slider_change(self, value):
        def generate_password(value):
            characters = string.ascii_lowercase
            if int(self.checkbox_number.get()) == 1:
                characters += string.digits
            if int(self.checkbox_uppercase.get()) == 1 :
                characters += string.ascii_uppercase
            if int(self.checkbox_symbol.get()) == 1:
                characters += string.punctuation
                
            print(self.checkbox_number.get())
            
            print(characters)
            password = ''.join(random.choice(characters) for _ in range(value))
            return password
        
        if round(float(value)) <= 7 :
            self.status.config(text='Weak', foreground='white', background='#FF1010')
        elif round(float(value)) > 7 and round(float(value)) <= 20:
            self.status.config(text='Good', foreground='white', background='#FF6510')
        else:
            self.status.config(text='Super', foreground='white', background='#28FF17')
            
        password = generate_password(round(float(value)))
        self.input_user_var.set(value=password)
        self.scalar_label.config(text=f"Password Length : {round(float(value))}")
        # ex = round(float(value))
        # print(self.checkbox_uppercase.get())
        
        
        
        
    def createWindows(self):
        label_title = ttk.Label(self.mainframe, text="Password Generator")
        self.input_user_var = StringVar(value='')
        input_user = ttk.Entry(self.mainframe, textvariable=self.input_user_var, width=70)
        # button = ttk.Button(self.mainframe , text="Search", command=self.getContact)
        self.status = ttk.Label(self.mainframe , text="Weak", foreground='white', background='red', padding=(5, 12))
        self.scalar_label = ttk.Label(self.mainframe, text="Password Length : 5")
        scalar = ttk.Scale(self.mainframe, from_=5 , to=50, command=self.slider_change, orient='horizontal')
        self.checkbox_uppercase = StringVar(value=0)
        self.checkbox_uppercase_entry = ttk.Checkbutton(self.mainframe, text="Uppercase", variable=self.checkbox_uppercase)
        self.checkbox_number = StringVar(value=0)
        self.checkbox_number_entry = ttk.Checkbutton(self.mainframe, text="123", variable=self.checkbox_number)
        self.checkbox_symbol = StringVar(value=0)
        self.checkbox_symbol_entry = ttk.Checkbutton(self.mainframe, text="!@#", variable=self.checkbox_symbol)
        label_title.pack()
        input_user.pack(pady=15)
        self.status.pack(pady=10)
        self.scalar_label.pack(pady=20)
        scalar.pack()
        self.checkbox_uppercase_entry.pack(pady=5)
        self.checkbox_number_entry.pack(pady=5)
        self.checkbox_symbol_entry.pack(pady=5)
        # button.pack()
    def loop(self):
        self.mainframe.pack()
        self.root.mainloop()

mainapp = Windows()
mainapp.createWindows()
mainapp.loop()
        
        