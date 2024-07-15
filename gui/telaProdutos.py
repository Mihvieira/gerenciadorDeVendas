from tkinter import messagebox
from gui.quadros import *
from gui.variaveis import colunas
from backend.produtos import *


class TelaProdutos(Quadro):
    def __init__(self, parent, modo):
        super().__init__(parent, modo)
        self.colunas = colunas['Produtos']
        self.configure(width=852, height=520, fg_color=self.modo["corQuadroPrincipal"], corner_radius=0)
        self.produto = Produto()
        self.gerarBlocoPesquisaTrv()
        self.posicionarFrame(48, 0)

    def gerarBlocoPesquisaTrv(self):
        self.entrada = EntradaDados(self)
        self.entrada.entradaPesquisa(self.buscar)
        self.entrada.posicionarNoCentro()
        self.botaoBuscar = Botao(self.master, "Buscar", self.buscar, self.modo["corBotoesPadrao"])
        self.botaoBuscar.posicionarBotao(700, 30)
        self.btnVerTudo = Botao(self.master, "Ver Todos", self.verTodos, self.modo["corBotoesPadrao"])
        self.btnVerTudo.posicionarBotao(790, 30)
        self.tree = Treeview(self, self.colunas, 70, 100, 70)
        self.tree.altura(7)
        self.tree.gerarSroolvbarY()
        self.tree.configurarBarra(590,70)
        self.tree.posicionarTree()

        self.btnEditar = Botao(self, 'Editar', self.editar, self.modo["corBotaoAtencao"])
        self.btnEditar.posicionarBotao(700, 70)
        self.btnExcluirProdutoT = Botao(self, 'Excluir', self.excluir, self.modo["corBotaoAlerta"])
        self.btnExcluirProdutoT.posicionarBotao(700, 114)
        self.btnIncluirNovo = Botao(self, 'Incluir Novo', self.incluirNovo, self.modo["corBotoesPadrao"])
        self.btnIncluirNovo.botaoDestaque()
        self.btnIncluirNovo.posicionarBotao(100, 250)

    def gerarBlocoEdicao(self):
        self.frameEdicao = Quadro(self, self.modo)
        self.frameEdicao.gerarFramePadrao(737, 167, self.modo['corDeFundo'])
        self.frameEdicao.calcGapVertical(5, 26, 3)
        self.rotuloNome = Rotulo(self.frameEdicao, 'Nome')
        self.rotuloNome.posicionarRotulo(5, self.frameEdicao.yDist[0])
        self.rotuloQtd = Rotulo(self.frameEdicao, 'Quantidade')
        self.rotuloQtd.posicionarRotulo(336, self.frameEdicao.yDist[0])
        self.rotuloDesc = Rotulo(self.frameEdicao, 'Descrição')
        self.rotuloDesc.posicionarRotulo(470, self.frameEdicao.yDist[0])
        self.inputNome = EntradaDados(self.frameEdicao)
        self.inputQtd = EntradaDados(self.frameEdicao)
        self.inputDesc = EntradaDados(self.frameEdicao)
        self.rotuloPreco = Rotulo(self.frameEdicao, 'Preço Unitário R$')
        self.rotuloPreco.posicionarRotulo(5, self.frameEdicao.yDist[2])
        self.rotuloDesconto = Rotulo(self.frameEdicao, 'Desconto %')
        self.rotuloDesconto.posicionarRotulo(120, self.frameEdicao.yDist[2])
        self.inputPreco = EntradaDados(self.frameEdicao)
        self.inputDesconto = EntradaDados(self.frameEdicao)
        self.btnSalvar = Botao(self.frameEdicao, 'Salvar', self.salvar, self.modo["corBotaoSave"])
        self.btnSalvar.botaoDestaque()
        self.btnSalvar.posicionarBotao(348, self.frameEdicao.yDist[3])
        self.frameEdicao.posicionarFrame(51, 300)
        
        self.inputs = [self.inputNome, self.inputDesc, self.inputPreco, self.inputQtd, self.inputDesconto]
    
    def posicionarEntradaEdicao(self):
        self.inputNome.entradaPlace(317, 5, self.frameEdicao.yDist[1])
        self.inputQtd.entradaPlace(120, 336, self.frameEdicao.yDist[1])
        self.inputDesc.entradaPlace(120, 470, self.frameEdicao.yDist[1])
        self.inputPreco.entradaPlace(100, 5, self.frameEdicao.yDist[3])
        self.inputDesconto.entradaPlace(91, 120, self.frameEdicao.yDist[3])
        

    def buscar(self):
        try:
            self.tree.deletarDados()
        finally:
            dado = self.entrada.getDados()
            busca = self.produto.buscarEmTudo(dado)
            if not busca:
                messagebox.showinfo('Pesquisa', 'Termo não encontrado.')
            else:
                for i in range(len(busca[0])):
                    self.tree.inserirDados(busca[0][i])
                self.entrada.limpar()
    
    def verTodos(self):
        busca = self.produto.buscarTodos()
        if not busca:
            messagebox.showinfo('Pesquisa', 'Nada encontrado.')
        else:
            for i in range(len(busca)):
                self.tree.inserirDados(busca[i])
            self.entrada.limpar()
            
    def salvar(self):
        self.criar()
        salvar = self.produto.cadastrar()
        if salvar == 'Dados inseridos com sucesso':
            messagebox.showinfo('Sucesso!', 'Dados cadastrados.')
            self.limparEntrada(self.inputs)
            self.frameEdicao.place_forget()
        else:
            messagebox.showerror("ERRO", f"{salvar}")
                
    def editar(self):
        dados = self.tree.itemSelecionado()
        self.produto.setId(dados[0])
        self.gerarBlocoEdicao()
        self.btnSalvar.place_forget()
        self.btnAtualizar = Botao(self.frameEdicao, 'Atualizar', self.atualizar, self.modo["corBotoesPadrao"])
        self.btnAtualizar.botaoDestaque()
        self.btnAtualizar.posicionarBotao(348, self.frameEdicao.yDist[3])
        index = 1
        for i in self.inputs:
            i.entradaComDados(dados[index])
            index +=1
        self.tree.deletarItem()
        self.posicionarEntradaEdicao()

    def excluir(self):
        dados = self.tree.itemSelecionado()
        self.produto.setId(dados[0])
        deletar = self.produto.excluir()
        if deletar == 'Dados inseridos com sucesso':
            self.tree.deletarItem()
            messagebox.showinfo('Sucesso!', 'Dados excluídos.')
        else:
            messagebox.showerror("ERRO", f"{salvar}")
    
    def atualizar(self):
        self.criar()
        atualizar = self.produto.editar()
        if atualizar == 'Dados inseridos com sucesso':
            messagebox.showinfo('Sucesso!', 'Dados alterados.')
            self.limparEntrada(self.inputs)
            self.frameEdicao.place_forget()
            self.tree.inserirDados(self.produto.verAtributos())
        else:
            messagebox.showerror("ERRO", f"{salvar}")
    
    def incluirNovo(self):
        self.gerarBlocoEdicao()
        self.posicionarEntradaEdicao()
    
    def criar(self):
        dados = self.getAllValues(self.inputs)
        self.produto.criar(dados[0], dados[1], dados[2], dados[3], dados[4])

