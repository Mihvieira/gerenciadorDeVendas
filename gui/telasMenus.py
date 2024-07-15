from tkinter import messagebox

from gui.quadros import *
from gui.treeview import *
from backend.vendas import *
from backend.pagamentos import *
from backend.itensVendidos import *
from backend.clientes import *
from backend.produtos import *

class MenuLateral(Quadro):
    # classe que gera os quadros e ícones da tela inicial de acordo com os padrões da aplicação
    def __init__(self, parent, modo, comandos):
        super().__init__(parent, modo)
        self.comandos = comandos
        self.configure(width=48, height=520, fg_color=self.modo["corMenuLateral"], corner_radius=0)
        self.gerarMenuLateral()

    def gerarMenuLateral(self):
        # define o menu lateral fixo com seus ícones e ações para cada botão
        self.posicionarFrame(0, 0)
        # define os itens do menu lateral
        # Home/Início
        self.botaoHome = Botao(self, '', self.comandos[0], '')
        self.botaoHome.botaoIcones(icones["home"], 4, 13)


class MenuPrincipal(Quadro):
    # classe que gera os quadros e ícones da tela inicial de acordo com os padrões da aplicação
    def __init__(self, parent, modo, comandos):
        super().__init__(parent, modo)
        self.comandos = comandos
        self.entries = []
        self.configure(width=852, height=520, fg_color=self.modo["corQuadroPrincipal"], corner_radius=0)
        self.gerarMenuPrincipal()

    def gerarMenuPrincipal(self):
        #Tela do Menu Principal - apresenta as ações da aplicação e viabiliza a transição entre cada item
        self.posicionarFrame(48, 0)
        #Itens da Tela
        #Barra de Pesquisa
        self.entrada = EntradaDados(self)
        self.entrada.entradaPesquisa(self.buscar)
        self.entrada.posicionarNoCentro()
        self.entries.append(self.entrada)
        self.botaoBuscar = Botao(self, "Buscar", self.comandos[0], self.modo["corBotoesPadrao"])
        self.botaoBuscar.posicionarBotao(700, 30)
        #Quadros explicativos com botões para abrir nova tela
        frameMenuCadastro = None
        frameMenuProdutos = None
        frameMenuVendas = None
        frameMenuClientes = None
        #Quadro Cadastro
        self.gerarFrameMenu(frameMenuCadastro, self.modo["corQuadroSecundario"], self.modo["corBotaoAtencao"],
                            'Gere uma nova venda aqui.\nCadastre o cliente e a venda.', icones["cadastro"], "Cadastro",
                            self.comandos[1], 9, 187)
        #Quadro Produtos
        self.gerarFrameMenu(frameMenuProdutos, self.modo["corQuadroSecundario"], self.modo["corBotoesPadrao"],
                            'Gerencie os produtos aqui.\nInclua, edite, exclua e consulte.', icones["produtos"],
                            "Produtos", self.comandos[2], 219, 187)
        #Quadro Vendas
        self.gerarFrameMenu(frameMenuVendas, self.modo["corQuadroSecundario"], self.modo["corBotoesPadrao"],
                            'Gerencie as vendas aqui.\nEdite e exclua e consulte.', icones["vendas"], "Vendas",
                            self.comandos[3], 429, 187)
        #Quadro Clientes
        self.gerarFrameMenu(frameMenuClientes, self.modo["corQuadroSecundario"], self.modo["corBotoesPadrao"],
                            'Gerencie os clientes aqui.\nInclua, edite, exclua e consulte.', icones["clientes"],
                            "Clientes", self.comandos[4], 639, 187)
        #Data e Hora
        self.data = Rotulo(self, '', )
        self.data.gerarDataHora(self.dataHoje.capitalize())

    def gerarFrameMenu(self, nome, cor1, cor2, textoLabel, imagem, textoBotao, comandoBotao, x, y):
        #gera o conteúdo do Quadro Menu Principal com medidas pré-definidas
        nome = ctk.CTkFrame(self, width=205, height=182, fg_color=cor1, corner_radius=15, bg_color=self.bgColorPadrao)

        self.labelTexto = Rotulo(nome, textoLabel)
        self.labelTexto.gerarTextoDescricao(17, 92)
        self.imagemFrame = ctk.CTkImage(PIL.Image.open(caminhoImagens + imagem))

        self.frameElipse = ctk.CTkFrame(nome, width=44, height=44, fg_color=cor2, corner_radius=50,
                                        bg_color=self.bgColorPadrao)

        self.labelIcon = ctk.CTkLabel(self.frameElipse, image=self.imagemFrame, text='')

        self.botao = Botao(nome, textoBotao, comandoBotao, cor2)
        self.botao.botaoDestaque()
        self.botao.posicionarBotaoRel(0.5, 0.9)

        self.labelIcon.place(x=11, y=10)
        self.frameElipse.place(x=17, y=32)

        nome.place(x=x, y=y)
    
    def buscar(self, event=None):
        dado = self.entrada.getDados()
        self.cl = Cliente()
        self.prod = Produto()
        self.venda = Venda()
        self.pagamento = Pagamento()
        buscaCliente = self.cl.buscarEmTudo(dado)
        buscaProduto = self.prod.buscarEmTudo(dado)
        buscaVenda = self.venda.buscarEmTudo(dado)
        buscaPg = self.pagamento.buscarEmTudo(dado)
        if not buscaCliente and not buscaPg and not buscaProduto and not buscaVenda:
            messagebox.showinfo('Pesquisa', 'Termo não encontrado.')
        else:
            self.topLevel = TelaPopUp(self, self.modo)
            dados = [buscaCliente, buscaProduto, buscaVenda, buscaPg]
            self.criarTabela(dados)
            self.topLevel.mainloop()
    
    def criarTabela(self, dados):
        total_rows = len(dados)
        total_columns = [1, 2, 3, 4, 5, 6, 7, 8]
        
        self.tree = Treeview(self.topLevel, total_columns, 100, 20, 20)
        self.tree.altura(total_rows)
        for i in range(len(dados)):
            if len(dados[i]) != 0:
                for j in dados[i]:
                    for a in range(len(j)):
                        self.tree.inserirDados(j[a])
        
        self.tree.posicionarTree()