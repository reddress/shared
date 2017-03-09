import tkinter as tk
from math import ceil
from decimal import Decimal

def roundup(x, factor):
    return (ceil(Decimal(x) * Decimal(factor)))/Decimal('10000')

def roundupmult(x, m, factor):
    return (ceil(Decimal(x) * Decimal(m) * Decimal(factor)))/Decimal('10000')

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.entryx.focus_set()

    def createWidgets(self):
        self.label1 = tk.Label(text="orig").grid(row=0, column=0)
        
        self.entryx = tk.Entry(width=9)
        self.entryx.grid(row=0, column=1)
        self.entryx.bind('<Key-Return>', self.update_values)
        self.entryx.bind('<Button-1>', self.clearall)
        self.entryx.bind('<F3>', self.clearall)

        # multiplier
        self.label7 = tk.Label(text="mult").grid(row=0, column=2)
        self.multiplier = tk.Entry(width=9)
        self.multiplier.grid(row=0, column=3)
        self.multiplier.bind('<Key-Return>', self.update_values)
        self.multiplier.bind('<Button-1>', self.clearall)
        self.multiplier.bind('<F3>', self.clearall)

        self.label2 = tk.Label(text="0%").grid(row=1, column=0)
        self.twenty = tk.Entry(width=9)
        self.twenty.grid(row=1, column=1)

        self.label3 = tk.Label(text="6%").grid(row=2, column=0)
        self.twentyone = tk.Entry(width=9)
        self.twentyone.grid(row=2, column=1)

        self.label6 = tk.Label(text="1.0").grid(row=6, column=0)
        self.three = tk.Entry(width=9)
        self.three.grid(row=6, column=1)

        # second column

        # self.label8 = tk.Label(text="3.0").grid(row=1, column=0)
        self.twentymult = tk.Entry(width=9)
        self.twentymult.grid(row=1, column=3)

        self.twentyonemult = tk.Entry(width=9)
        self.twentyonemult.grid(row=2, column=3)
        
        self.threemult = tk.Entry(width=9)
        self.threemult.grid(row=6, column=3)


    def clearall(self, event):
        self.twenty.delete(0, len(self.twenty.get()))
        self.twentyone.delete(0, len(self.twentyone.get()))
        self.three.delete(0, len(self.three.get()))

        self.twentymult.delete(0, len(self.twentymult.get()))
        self.twentyonemult.delete(0, len(self.twentyonemult.get()))
        self.threemult.delete(0, len(self.threemult.get()))

        self.multiplier.delete(0, len(self.multiplier.get()))

        self.entryx.delete(0, len(self.entryx.get()))
        self.entryx.focus_set()
        
    def update_values(self, event):
        x = self.entryx.get()
        x = x.replace(",", ".")
        if x == '':
            self.entryx.insert(0, '0')
            x = '0'

        m = self.multiplier.get()
        if m == '':
            self.multiplier.insert(0, '1')
            m = '1'

        self.twenty.delete(0, len(self.twenty.get()))
        self.twenty.insert(0, '{0:.3f}'.format(roundup(x, '30000')))

        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentyone.insert(0, '{0:.4f}'.format(roundup(x, '28200')))

        self.three.delete(0, len(self.three.get()))
        self.three.insert(0, '{0:.4f}'.format(roundup(x, '10000')))

        self.twentymult.delete(0, len(self.twentymult.get()))
        self.twentymult.insert(0, '{0:.3f}'.format(roundupmult(x, m, '30000')))

        self.twentyonemult.delete(0, len(self.twentyonemult.get()))
        self.twentyonemult.insert(0, '{0:.4f}'.format(roundupmult(x, m, '28200')))

        self.threemult.delete(0, len(self.threemult.get()))
        self.threemult.insert(0, '{0:.4f}'.format(roundupmult(x, m, '10000')))

root = tk.Tk()
root.wm_title("Calc ZERO")

# show all: 192x152+245+773")
# root.geometry("192x105+245+820")
# root.geometry("192x85+245+840")
root.geometry("192x64+245+861")

# root.wm_attributes("-topmost", 1)
app = Application(master=root)
app.mainloop()
