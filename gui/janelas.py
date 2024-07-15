from gui.quadros import *
from gui.telaCadastro import TelaCadastro
from gui.telaProdutos import TelaProdutos
from gui.telaVenda import TelaVendas
from gui.telasMenus import MenuLateral, MenuPrincipal
from gui.TelaCliente import *

class QuadroPrincipal(ctk.CTkFrame):
    # classe que controla o fluxo de janelas da aplicação
    def __init__(self, parent):
        super().__init__(parent)
        self.modo = modoEscuro
        self.configure(fg_color=self.modo["corQuadroPrincipal"], width=900, height=520)
        self.menuLateral()
        self.telaMenuPrincipal()

    def menuLateral(self):
        comandos = [self.abrirHome]
        self.frameLateral = MenuLateral(self, self.modo, comandos)

    def telaMenuPrincipal(self):
        comandos = [self.buscar('Tudo'), self.abrirCadastro, self.abrirProdutos, self.abrirVendas,
                    self.abrirClientes]
        self.framePrincipal = MenuPrincipal(self, self.modo, comandos)

    def abrirCadastro(self):
        self.framePrincipal.esquecerFrame()
        self.frameCadastro = TelaCadastro(self, self.modo)

    def abrirProdutos(self):
        self.framePrincipal.esquecerFrame()
        self.frameProdutos = TelaProdutos(self, self.modo)

    def abrirVendas(self):
        self.framePrincipal.esquecerFrame()
        self.frameVendas = TelaVendas(self, self.modo)

    def abrirClientes(self):
        self.framePrincipal.esquecerFrame()
        self.frameClientes = TelaClientes(self, self.modo)

    def abrirHome(self):
        self.telaMenuPrincipal()

    def esquecerFrames(self):
        widgets = self.winfo_children()
        widgets.pop(0)
        for i in widgets:
            if i.winfo_children():
                widgets.extend(i.winfo_children())
        for item in widgets:
            return item.place_forget()
    
    def buscar(self, tabela):
        pass
