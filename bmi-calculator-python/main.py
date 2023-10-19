from tkinter import *
from tkinter import ttk


class Windows():
    root = Tk()
    mainframe = ttk.Frame(root, padding=20)
    root.tk.call('source', r'Forest-ttk-theme-master\forest-light.tcl')
    root.geometry('300x400')
    root.title('Calculator BMI Tkinter')
    ttk.Style().theme_use('forest-light')
    def displayScore(self, value):
        self.result.pack_forget()
        score = ['Underweight', 'Normal', 'Overweight', 'Obesity']
        if value <= 18.5:
            status = f"You score is {value} and you {score[0]}"
        if value > 18.5 and value <= 24.9:
            status = f"You score is {value} and you {score[1]}"
        if value > 24.9 and value <= 29.9:
            status = f"You score is {value} and you {score[2]}"
        if value > 30:
            status = f"You score is {value} and you {score[3]}"
        self.result.config(text=status)
        self.result.pack(pady=30)
        
    def calculate(self):
        height_var = self.height_var.get() / 100
        weight_var = self.weight_var.get()
        res = weight_var / ( height_var*height_var)
        res = float("{:.1f}".format(res))
        self.displayScore(res)
        
    def createWindows(self):
        label_title = ttk.Label(self.mainframe, text="Calculator BMI")
        h_label = ttk.Label(self.mainframe, text="Height")
        self.height_var = IntVar(value='')
        w_label = ttk.Label(self.mainframe, text="Weight")
        self.weight_var = IntVar(value='')
        height = ttk.Entry(self.mainframe, textvariable=self.height_var, width=30)
        weight = ttk.Entry(self.mainframe, textvariable=self.weight_var, width=30)
        button = ttk.Button(self.mainframe , text="Start", command=self.calculate)
        self.result = ttk.Label(self.mainframe, text="")
        label_title.pack(pady=30)
        h_label.pack()
        height.pack(pady=15)
        w_label.pack()
        weight.pack(pady=15)
        button.pack()
    def loop(self):
        self.mainframe.pack()
        self.root.mainloop()

mainapp = Windows()
mainapp.createWindows()
mainapp.loop()
        
        