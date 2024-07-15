import tkinter as tk
import customtkinter as ctk
from gui.variaveis import *


class Rotulo(ctk.CTkLabel):
    # classe que controla os textos/rótulos/Label da aplicação
    def __init__(self, parent, text):
        super().__init__(parent)
        self.text = text
        self.tamanhoPadrao = 12
        self.tamanhoGrande = 24
        self.tamanhoPequeno = 10
        self.configure(text=self.text, font=ctk.CTkFont(fontPrincipal, self.tamanhoPadrao),
                       text_color=modoEscuro["corPrincipalFonte"], justify=tk.LEFT)

    def posicionarRotulo(self, x, y):
        self.place(x=x, y=y)

    def posicionarRotuloRel(self, x, y):
        self.place(relx=x, rely=y)

    def gerarNome(self, x, y):
        self.configure(font=ctk.CTkFont(fontPrincipal, self.tamanhoGrande))
        self.place(x=x, y=y)

    def gerarDataHora(self, data):
        self.configure(text=data, text_color=modoEscuro["corSecundariaFonte"], justify=tk.CENTER)
        self.place(relx=0.8, rely=0.94, anchor=tk.E)

    def gerarTextoDescricao(self, x, y):
        self.configure(text_color=modoEscuro["corSecundariaFonte"],
                       font=ctk.CTkFont(fontPrincipal, self.tamanhoPequeno))
        self.place(x=x, y=y)

    def getText(self):
        return self.text


