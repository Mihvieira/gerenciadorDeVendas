import tkinter as tk
import customtkinter as ctk
import PIL.Image
from gui.variaveis import *


class Botao(ctk.CTkButton):
    def __init__(self, parent, text, command, color):
        super().__init__(parent)
        self.text = text
        self.command = command
        self.color = color
        self.configure(width=77, height=19, text=self.text, fg_color=self.color, command=self.command,
                       text_color=modoEscuro["corPrincipalFonte"], corner_radius=8, font=ctk.CTkFont(fontPrincipal, 12))

    def posicionarBotao(self, x, y):
        return self.place(x=x, y=y)

    def posicionarBotaoRel(self, relx, rely):
        self.place(relx=relx, rely=rely, anchor=tk.CENTER)

    def botaoDestaque(self):
        self.configure(width=178, height=26, font=ctk.CTkFont(fontPrincipal, 14), corner_radius=10)

    def botaoIcones(self, imagem, x, y):
        self.imagem = ctk.CTkImage(PIL.Image.open(caminhoImagens + imagem), size=(28, 28))
        self.configure(width=28, height=28, fg_color='transparent', image=self.imagem, border_width=0,
                       bg_color='transparent', hover=False, text='')
        self.place(x=x, y=y)
    
    def desabilitarBotao(self):
        self.configure(state='disabled')
    
    def habilitarBotao(self):
        self.configure(state='enable')
    
    def enterEvent(self, event):
        self.bind('<Return>', event)
