from tkinter import StringVar
from gui.botoes import *


class EntradaDados(ctk.CTkEntry):
    def __init__(self, parent):
        super().__init__(parent)
        self.dado = StringVar()
        self.configure(height=20, fg_color=modoEscuro["corDeFundo"], text_color=modoEscuro["corPrincipalFonte"],
                       textvariable=self.dado)

    def entradaPesquisa(self, event):
        self.configure(width=533, placeholder_text='Pesquisa')
        self.enterEvent(event)

    def posicionarNoCentro(self):
        self.place(relx=0.12, rely=0.05)

    def posicionarComPlace(self, x, y):
        self.place(x=x, y=y)

    def entradaPlace(self, width, x, y):
        self.configure(width=width)
        self.posicionarComPlace(x, y)

    def entrada(self, width):
        self.configure(width=width)

    def getDados(self):
        return self.dado.get()

    def desabilitar(self):
        self.configure(state='disabled')

    def habilitar(self):
        self.configure(state='normal')

    def entradaComDados(self, placeholder):
        self.insert(0, placeholder)

    def limpar(self):
        self.delete(0, 'end')

    def enterEvent(self, event):
        self.bind('<Return>', event)

    def eventWrite(self, event):
        self.dado.trace('w', event)

    def mudarBorda(self):
        self.configure(border_color='red')
