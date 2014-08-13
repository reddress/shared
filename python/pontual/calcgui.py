import tkinter as tk
from math import ceil
from decimal import Decimal

def roundup(x, factor):
    return (ceil(Decimal(x) * Decimal(factor)))/Decimal('10000')

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

        self.label2 = tk.Label(text="20%").grid(row=1, column=0)
        self.twenty = tk.Entry(width=9)
        self.twenty.grid(row=1, column=1)

        self.label3 = tk.Label(text="21%").grid(row=2, column=0)
        self.twentyone = tk.Entry(width=9)
        self.twentyone.grid(row=2, column=1)

        self.label4 = tk.Label(text="22%").grid(row=3, column=0)
        self.twentytwo = tk.Entry(width=9)
        self.twentytwo.grid(row=3, column=1)

        # self.all = tk.Text(width=19, height=2, font="ProggyTinyTTSZ", wrap=tk.WORD)
        #self.all = tk.Entry(width=8)
        #self.all.grid(row=4, column=0, columnspan=2)
        self.label5 = tk.Label(text="23%").grid(row=4, column=0)
        self.twentythree = tk.Entry(width=9)
        self.twentythree.grid(row=4, column=1)

    def clearall(self, event):
        self.twenty.delete(0, len(self.twenty.get()))
        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentytwo.delete(0, len(self.twentytwo.get()))
        self.twentythree.delete(0, len(self.twentythree.get()))


        # self.all.delete("1.0", tk.END)
        # self.all.delete(0, len(self.all.get()))
        self.entryx.delete(0, len(self.entryx.get()))
        
    def update_values(self, event):
        x = self.entryx.get()
        x = x.replace(",", ".")

        self.twenty.delete(0, len(self.twenty.get()))
        self.twenty.insert(0, '{0:.3f}'.format(roundup(x, '24000')))

        self.twentyone.delete(0, len(self.twentyone.get()))
        self.twentyone.insert(0, '{0:.4f}'.format(roundup(x, '23700')))

        self.twentytwo.delete(0, len(self.twentytwo.get()))
        self.twentytwo.insert(0, '{0:.4f}'.format(roundup(x, '23400')))

        self.twentythree.delete(0, len(self.twentytwo.get()))
        self.twentythree.insert(0, '{0:.4f}'.format(roundup(x, '23100')))

        fl = float(x)

        # self.all.delete("1.0", tk.END)
        # self.all.insert("1.0", '{:.2f}, {:.4f}, {:.4f}, {:.4f}'.format(fl * 2.4, fl * 2.37, fl * 2.34, fl * 3))
        # self.all.delete(0, len(self.all.get()))
        # self.all.insert(0, '{:.2f}'.format(fl * 3.0))


root = tk.Tk()
root.wm_title("Calc")
root.geometry("115x94+162+603")
root.wm_attributes("-topmost", 1)
app = Application(master=root)
app.mainloop()
