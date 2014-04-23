# GUI to hold name, and purchase info

import os
import shelve
import tkinter as tk
from datetime import datetime

from produto import Produto

os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/")
SHELF_FILE = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/pontual/reposicao/produtodb"
pdb = shelve.open(SHELF_FILE)

def set(widget, value):
    if isinstance(widget, tk.Text):
        widget.delete("1.0", tk.END)
        widget.insert("1.0", value)
    else:
        widget.delete(0, tk.END)
        widget.insert(0, value)

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        
    def createWidgets(self):
        self.clearBtn = tk.Button(text="Clear", command=self.clear)
        self.codigoValue = tk.StringVar()
        self.vendasValue = tk.StringVar()
        self.vendasNowValue = tk.StringVar()
        self.caixaValue = tk.StringVar()
        self.lastmodValue = tk.StringVar()

        self.codigo = tk.Entry(width=8, textvariable=self.codigoValue)
        
        self.loadBtn = tk.Button(text="Load", command=self.load)

        self.vendas = tk.Entry(width=8, textvariable=self.vendasValue)
        self.vendasNow = tk.Entry(width=8, textvariable=self.vendasNowValue)
        self.caixa = tk.Entry(width=8, textvariable=self.caixaValue)
        self.lastmod = tk.Entry(width=8, textvariable=self.lastmodValue)
        
        # self.saveBtn = tk.Button(text="Save", command=self.save)
        self.copyBtn = tk.Button(text="Copy", command=self.copy)
        
        self.info = tk.Text(width=42, height=6, font="ProggyTinyTTSZ")

        # self.dummyLabel = tk.Label(text="PTL")

        self.clearBtn.grid(row=0, column=0)
        self.codigo.grid(row=0, column=1)
        self.loadBtn.grid(row=0, column=2)
        self.lastmod.grid(row=0, column=3)
        # self.dummyLabel.grid(row=0, column=3)
        
        self.vendas.grid(row=1, column=0)
        self.vendasNow.grid(row=1, column=1)
        self.caixa.grid(row=1, column=2)
        # self.saveBtn.grid(row=0, column=5)
        self.copyBtn.grid(row=1, column=3)
        
        self.info.grid(row=2, column=0, columnspan=4)

        self.info.bind("<KeyRelease>", self.save)

    def clear(self):
        self.codigoValue.set("")
        self.vendasValue.set("")
        self.vendasNowValue.set("")
        self.caixaValue.set("")
        
    def load(self):
        codigo = self.codigoValue.get()
        try:
            produto = pdb[codigo]
            set(self.vendas, produto.vendas)
            set(self.caixa, produto.caixa)
            set(self.info, produto.info)
            try:
                set(self.lastmod, produto.lastmod.strftime("%d/%m/%y"))
            except AttributeError:
                set(self.lastmod, "")
        except KeyError:
            set(self.info, "\nÚltimo container - \n")
            set(self.lastmod, "")
        
    def save(self, event):
        codigo = self.codigoValue.get()
        if len(codigo) > 1:
            vendas = self.vendasValue.get()
            caixa = self.caixaValue.get()
            info = self.info.get("1.0", tk.END)[:-1]
            pdb[codigo] = Produto(codigo, caixa, info, vendas, datetime.now())

    def copy(self):
        info = self.info.get("1.0", tk.END)[:-1]
        self.clipboard_clear()
        codigoLine = (self.codigoValue.get() + ";;;;" +
                      ";".join([self.vendasValue.get(),
                                self.vendasNowValue.get(),
                                self.caixaValue.get()]))
        self.clipboard_append(codigoLine + "\n" + info)
        self.save(None)

root = tk.Tk()
root.wm_title("Reposicao")
root.geometry("272x114+1085+583")
root.wm_attributes("-topmost", 1)
app = Application(master=root)
app.mainloop()
print("Exiting...")
pdb.close()
