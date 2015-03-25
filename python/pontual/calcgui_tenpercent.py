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

        self.label2 = tk.Label(text="10%").grid(row=1, column=0)
        self.twenty = tk.Entry(width=9)
        self.twenty.grid(row=1, column=1)

        self.label3 = tk.Label(text="11%").grid(row=2, column=0)
        self.twentyone = tk.Entry(width=9)
        self.twentyone.grid(row=2, column=1)

        self.label4 = tk.Label(text="12%").grid(row=3, column=0)
        self.twentytwo = tk.Entry(width=9)
        self.twentytwo.grid(row=3, column=1)

        self.label5 = tk.Label(text="13%").grid(row=4, column=0)
        self.twentythree = tk.Entry(width=9)
        self.twentythree.grid(row=4, column=1)

        self.label6 = tk.Label(text="3.0").grid(row=5, column=0)
        self.three = tk.Entry(width=9)
        self.three.grid(row=5, column=1)

        # second column

        # self.label8 = tk.Label(text="3.0").grid(row=1, column=0)
        self.twentymult = tk.Entry(width=9)
        self.twentymult.grid(row=1, column=3)

        self.twentyonemult = tk.Entry(width=9)
        self.twentyonemult.grid(row=2, column=3)
        
        self.twentytwomult = tk.Entry(width=9)
        self.twentytwomult.grid(row=3, column=3)

        self.twentythreemult = tk.Entry(width=9)
        self.twentythreemult.grid(row=4, column=3)

        self.threemult = tk.Entry(width=9)
        self.threemult.grid(row=5, column=3)


    def clearall(self, event):
        self.twenty.delete(0, len(self.twenty.get()))
        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentytwo.delete(0, len(self.twentytwo.get()))
        self.twentythree.delete(0, len(self.twentythree.get()))
        self.three.delete(0, len(self.three.get()))

        self.twentymult.delete(0, len(self.twentymult.get()))
        self.twentyonemult.delete(0, len(self.twentyonemult.get()))
        self.twentytwomult.delete(0, len(self.twentytwomult.get()))
        self.twentythreemult.delete(0, len(self.twentythreemult.get()))
        self.threemult.delete(0, len(self.threemult.get()))

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
        self.twenty.insert(0, '{0:.3f}'.format(roundup(x, '27000')))

        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentyone.insert(0, '{0:.4f}'.format(roundup(x, '26700')))

        self.twentytwo.delete(0, len(self.twentytwo.get()))
        self.twentytwo.insert(0, '{0:.4f}'.format(roundup(x, '26400')))

        self.twentythree.delete(0, len(self.twentythree.get()))
        self.twentythree.insert(0, '{0:.4f}'.format(roundup(x, '26100')))

        self.three.delete(0, len(self.three.get()))
        self.three.insert(0, '{0:.4f}'.format(roundup(x, '30000')))

        self.twentymult.delete(0, len(self.twentymult.get()))
        self.twentymult.insert(0, '{0:.3f}'.format(roundupmult(x, m, '27000')))

        self.twentyonemult.delete(0, len(self.twentyonemult.get()))
        self.twentyonemult.insert(0, '{0:.4f}'.format(roundupmult(x, m, '26700')))

        self.twentytwomult.delete(0, len(self.twentytwomult.get()))
        self.twentytwomult.insert(0, '{0:.4f}'.format(roundupmult(x, m, '26400')))

        self.twentythreemult.delete(0, len(self.twentythreemult.get()))
        self.twentythreemult.insert(0, '{0:.4f}'.format(roundupmult(x, m, '26100')))

        self.threemult.delete(0, len(self.threemult.get()))
        self.threemult.insert(0, '{0:.4f}'.format(roundupmult(x, m, '30000')))

        # fl = float(x)
        # self.all.delete("1.0", tk.END)
        # self.all.insert("1.0", '{:.2f}, {:.4f}, {:.4f}, {:.4f}'.format(fl * 2.4, fl * 2.37, fl * 2.34, fl * 3))
        # self.all.delete(0, len(self.all.get()))
        # self.all.insert(0, '{:.2f}'.format(fl * 3.0))


root = tk.Tk()
root.wm_title("Calc TEN PERCENT")
root.geometry("192x112+162+585")
# root.wm_attributes("-topmost", 1)
app = Application(master=root)
app.mainloop()
