from gui.quadros import *
from gui.telaCadastro import *
from backend.vendas import *
from backend.pagamentos import *
from backend.itensVendidos import *
from backend.clientes import *
from backend.produtos import *


class TelaVendas(Quadro):
    def __init__(self, parent, modo):
        super().__init__(parent, modo)
        self.colunas = colunas['Vendas']
        self.configure(width=852, height=520, fg_color=self.modo["corQuadroPrincipal"], corner_radius=0)
        self.gerarBlocoPesquisaTrv()
        self.posicionarFrame(48, 0)
        self.venda = Venda()
        self.pagamento = Pagamento()
        self.itemVendido = ItemVendido()
    
    def gerarBlocoPesquisaTrv(self):
        self.entrada = EntradaDados(self)
        self.entrada.entradaPesquisa(self.buscar)
        self.entrada.posicionarNoCentro()
        self.botaoBuscar = Botao(self.master, "Buscar", self.buscar, self.modo["corBotoesPadrao"])
        self.botaoBuscar.posicionarBotao(700, 30)
        self.btnVerTudo = Botao(self.master, "Ver Todos", self.verTodos, self.modo["corBotoesPadrao"])
        self.btnVerTudo.posicionarBotao(790, 30)
        self.tree = Treeview(self, self.colunas, 100, 40, 70)
        self.tree.tamanhoColuna('id', 20)
        self.tree.tamanhoColuna('idCl', 50)
        self.tree.tamanhoColuna('idPag', 50)
        self.tree.tamanhoColuna('idProd', 50)
        self.tree.altura(7)
        self.tree.gerarSroolvbarY()
        self.tree.configurarBarra(710,70)
        self.tree.posicionarTree()

        self.btnEditar = Botao(self, 'Editar', self.editar, self.modo["corBotaoAtencao"])
        self.btnEditar.posicionarBotao(750, 70)
        self.btnCancelar = Botao(self, 'Cancelar', self.cancelar, self.modo["corBotaoAlerta"])
        self.btnCancelar.posicionarBotao(750, 114)
        self.btnIncluirNovo = Botao(self, 'Incluir Novo', self.incluirNovo, self.modo["corBotoesPadrao"])
        self.btnIncluirNovo.botaoDestaque()
        self.btnIncluirNovo.posicionarBotao(100, 250)
        self.btnConsultarProd = Botao(self, 'Ver Itens', self.editar, self.modo["corBotoesPadrao"])
        self.btnConsultarProd.posicionarBotao(750, 202)
    
    def buscar(self):
        try:
            self.tree.deletarDados()
        finally:
            dado = self.entrada.getDados()
            busca = self.venda.buscarEmTudo(dado) #retorna uma lista com uma lista de tuplas
            if not busca:
                messagebox.showinfo('Pesquisa', 'Termo não encontrado.')
            else:
                for i in range(len(busca[0])):
                    self.tree.inserirDados(busca[0][i])
                self.entrada.limpar()
        
    def verTodos(self):
        busca = self.venda.buscarTodos() # retorna lista de tuplas ou uma tupla vazia
        if not busca:
            messagebox.showinfo('Pesquisa', 'Nada encontrado.')
        else:
            for i in range(len(busca)):
                self.tree.inserirDados(busca[i])
            self.entrada.limpar()

    def editar(self):
        #pegar dados da treeview
        dados = self.tree.itemSelecionado()
        idCliente = dados[1]
        idVenda = dados[0]
        idPagamento = dados[5]
        dadosPagamento = dados[-3:]
        dadosCliente = self.verCliente(idCliente) #lista com tupla
        dadosIvendidos = self.verItensVendidos(idVenda)
        self.place_forget()
        cadastro = TelaCadastro(self.master, self.modo)
        cadastro.iniciarTelaComDados(dadosCliente, self.listaCadastro, dadosPagamento, idVenda, idPagamento)
    
    def cancelar(self):
        # TODO : permite cancelar a compra mais de uma vez, o que pode atualizar o estoque de forma errada
        alerta = messagebox.askokcancel('Alerta: Essa operação altera os dados', 'deseja prosseguir?')
        if alerta is True:
            dados = self.tree.itemSelecionado()
            idVenda = dados[0]
            try:
                novoSatus = self.venda.editarStatus('Cancelado', idVenda)
                dadosIvendidos = self.verItensVendidos(idVenda)
                for i in range(len(dadosIvendidos)):
                    estoque = self.produto.buscar(dadosIvendidos[i][1], 'idProduto')[0][4]
                    qtd = dadosIvendidos[i][2]
                    total = int(estoque) + int(qtd)
                    self.produto.editarEstoque(total, dadosIvendidos[i][1])
                self.itemVendido.excluir(idVenda)
                self.pagamento.excluir(idVenda)
                self.tree.deletarItem()
            except Exception as e:
                messagebox.showerror("ERRO ao cancelar venda", f"{e}")
        else:
            None
    
    def incluirNovo(self):
        self.destroy()
        cadastro = TelaCadastro(self.master, self.modo)
    
    def verItensVendidos(self, idVenda):
        consulta = self.itemVendido.buscar(idVenda, 'idVenda')
        self.criarListaCadastro(consulta)
        return consulta    
    
    def verProdutos(self, idsProduto):
        # TODO
        self.produto = Produto()
        self.verProdutos = []
        for i in range(len(idsProduto)):
            verProdutos.append(self.produto.buscar(idsProduto[i], "idProduto")[1])
        return verProdutos
    
    def criarListaCadastro(self, lista):
        self.produto = Produto()
        self.listaCadastro = []
        for i in range(len(lista)):
            nomeProduto = self.produto.buscar(lista[i][1], "idProduto")[0][1]
            novaLista = (lista[i][1], nomeProduto, lista[i][2], lista[i][3])
            self.listaCadastro.append(novaLista)
    
    def verCliente(self, idCliente):
        # TODO
        self.cliente = Cliente()
        self.cliente.setId(idCliente)
        return self.cliente.buscar(idCliente, 'idCliente')
        
        
        