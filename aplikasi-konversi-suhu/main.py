from tkinter import *
from tkinter import ttk , font , messagebox

class Window():
    root = Tk()
    mainframe = ttk.Frame(root, padding=20)
    root.title('Celcius Converter')
    root.geometry("300x300")
    def __init__(self):
        pass
    def calculate(self):
        self.result.pack_forget()
        user_choose = self.option_user_var.get()
        user_input = self.input_user_var.get()
        result_operation = {}
        if user_choose == "Kelvin":
            result_operation["Kelvin"] = round(user_input + 273)
        if user_choose == "Reamur":
            result_operation["Reamur"] = round(4/5*user_input)
        if user_choose == "Fahrenheit":
            result_operation["Fahrenheit"] = round(( 9/5 * user_input) + 32)
        print(result_operation)
        self.result.config(text=f"{user_input} Celcius is {result_operation[user_choose]} {user_choose}")
        self.result.pack(pady=10)
            
            
    def createWindow(self):
        self.input_user_var = IntVar(value='0')
        input_user = ttk.Entry(self.mainframe, textvariable=self.input_user_var)
        self.option_user_var = StringVar(value='Kelvin')
        option_user = ttk.Combobox(self.mainframe, values=['Fahrenheit', "Reamur", "Kelvin"], textvariable=self.option_user_var, state='readonly')
        button_start = ttk.Button(self.mainframe, text='Start', command=self.calculate)
        self.result = ttk.Label(self.mainframe,text='Result Here')
        input_user.pack()
        option_user.pack(pady=10)
        button_start.pack()
    def loop(self):
        self.mainframe.pack()
        self.root.mainloop()
    
if __name__ == "__main__":
    mainapp = Window()
    mainapp.createWindow()
    mainapp.loop()