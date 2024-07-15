from tkinter import ttk
import tkinter as tk


class Treeview(ttk.Treeview):
    def __init__(self, parent, colunas, tamanho, x, y):
        super().__init__(parent)
        self.colunas = colunas
        self.tamanho = tamanho
        self.x = x
        self.y = y
        self.configure(show='headings', height=10, padding=5, selectmode='browse', columns=self.colunas)
        self.tamanhoColunas(self.colunas, self.tamanho)

    def posicionarTree(self):
        self.place(x=self.x, y=self.y)

    def posicionarNoCentro(self):
        self.place(relx=0.5, rely=0.05)

    def altura(self, h):
        self.configure(height=h)

    def headings(self):
        self.configure(show="tree")

    def gerarSroolvbarX(self, x, y):
        self.hsb = ttk.Scrollbar(self.master, orient=tk.HORIZONTAL, command=self.xview)
        self.configure(xscrollcommand=self.hsb.set)
        self.hsb.place(x=x, y=y)

    def gerarSroolvbarY(self):
        self.vsb = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscrollcommand=self.vsb.set)
        d = len(self.colunas) + 1
        d = (d * self.tamanho) + 10
        self.vsb.place(x=d, y=self.y, anchor='nw')

    def tamanhoColunas(self, colunas, tamanho):
        for i in colunas:
           self.heading(i, text=i), self.column(i, minwidth=0, width=tamanho)
    
    def tamanhoColuna(self, coluna,tamanho):
        self.column(coluna, minwidth=0, width=tamanho)
        
    def treeviewCadastro(self):
        self.configure(height=5)
        self.gerarSroolvbarY()
        self.posicionarTree()

    def itemSelecionado(self):
        for i in self.selection():
            item = self.item(i)
            gravar = item['values']
            return gravar
    def verId(self):
        self.identify()
    
    def configurarBarra(self, x,y):
        self.vsb.place(x=x,y=y)
    
    def inserirDados(self, lista):
        self.insert('', tk.END, values=lista)
    
    def deletarDados(self):
        for i in self.get_children():
            self.delete(i)
    
    def deletarItem(self):
        for i in self.selection():
            self.delete(i)
