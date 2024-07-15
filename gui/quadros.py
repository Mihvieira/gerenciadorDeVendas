import locale
from abc import abstractmethod
from datetime import date
from gui.entradaDados import *
from gui.label import *
from gui.treeview import *

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")


class Quadro(ctk.CTkFrame):
    # classe que gera os quadros e ícones da tela inicial de acordo com os padrões da aplicação
    def __init__(self, parent, modo):
        super().__init__(parent)
        self.modo = modo
        self.configure(bg_color='transparent', fg_color=self.modo["corQuadroPrincipal"])
        self.dataHoje = date.today().strftime("%A, %d de %B de %Y")
        self.bgColorPadrao = 'transparent'
        self.yDist = []

    def gerarFramePadrao(self, width, height, cor):
        return self.configure(width=width, height=height, fg_color=cor, corner_radius=0)

    def posicionarFrame(self, x, y):
        self.place(x=x, y=y)

    def posicionarRel(self, x, y):
        self.place(relx=x, rely=y)

    def esquecerFrame(self):
        return self.place_forget()

    def calcGapVertical(self, y, dist, qtd):
        self.yDist.append(y)
        for i in range(qtd):
            d = y + dist
            y = d
            self.yDist.append(d)

    def getAllValues(self, lista):
        resultado = [entry.getDados() for entry in lista]
        return resultado

    def gerarPdf(self):
        # TODO imprimir tudo ou selecionado
        # TODO fazer primeiro imprimir tudo
        pass
    
    def limparEntrada(self, lista):
        for i in lista:
            return i.limpar()
    
    @abstractmethod
    def verTodos(self):
        pass
            
    @abstractmethod
    def buscar(self):
        pass
        
    @abstractmethod
    def salvar(self):
        pass
    
    @abstractmethod
    def atualizar(self):
        pass
    
    @abstractmethod
    def editar(self):
        pass


class TelaPopUp(ctk.CTkToplevel):
    # classe que gera os quadros e ícones da tela inicial de acordo com os padrões da aplicação
    def __init__(self, parent, modo):
        super().__init__(parent)
        self.modo = modo
        self.geometry('852x520')
        self.configure(fg_color=self.modo["corQuadroPrincipal"])

    def gerarVisualizacao(self, comando, colunas):
        self.tree = Treeview(self, colunas, 100, 91, 80)
        self.tree.posicionarNoCentro()
        self.btnGerarPdf = Botao(self, 'Gerar Pdf', comando, self.modo["corBotoesPadrao"])
        self.btnGerarPdf.posicionarBotaoRel(0.5, 0.8)

    def gerarVisualPesquisa(self):
        self.tree.headings()
    
    