from tkinter import messagebox
from datetime import datetime
from backend.clientes import *
from backend.produtos import *
from backend.vendas import *
from backend.itensVendidos import *
from backend.pagamentos import *
from gui.quadros import *


class TelaCadastro(Quadro):
    def __init__(self, parent, modo):
        super().__init__(parent, modo)
        self.configure(width=852, height=520, fg_color=self.modo["corQuadroPrincipal"], corner_radius=0)
        self.posicionarFrame(48, 0)
        self.calcGapVertical(16, 28, 12)
        self.inicioCadastro()
        self.id = None
        self.dadosProduto = []
        self.cl = Cliente()
        self.produto = Produto()
        self.venda = Venda()
        self.pagamento = Pagamento()
        self.itemVendido = ItemVendido()
        self.clienteExistente = False
        self.vendaExistente = False
        self.itemVendidoExistente = False
        self.pagamentoExistente = False

    def inicioCadastro(self):
        # linha 0
        self.cpfOuCnpj = Rotulo(self, 'Digite o CPF ou CNPJ')
        self.cpfOuCnpj.posicionarRotulo(57, self.yDist[0])
        self.inputCpfOuCnpj = EntradaDados(self)
        self.inputCpfOuCnpj.entradaPlace(136, 191, self.yDist[0])
        self.inputCpfOuCnpj.enterEvent(self.getCpfCnpj)
        self.btnBuscar = Botao(self, 'Buscar', self.getCpfCnpj, self.modo["corBotoesPadrao"])
        self.btnBuscar.posicionarBotao(344, self.yDist[0])
        self.btnBuscar.enterEvent(self.getCpfCnpj)

    def gerarRotulos(self):
        #Define a tela para cadastro de fluxo de vendas
        self.idRotulo = Rotulo(self, self.id)
        self.idRotulo.posicionarRotulo(450, self.yDist[0])
        #linha 1
        self.rotuloNome = Rotulo(self, 'Nome')
        self.rotuloNome.posicionarRotulo(57, self.yDist[1])
        
        self.rotuloDataNascimento = Rotulo(self, 'Data de nascimento')
        self.rotuloDataNascimento.posicionarRotulo(388, self.yDist[1])
        
        self.rotuloTelefone = Rotulo(self, 'Telefone')
        self.rotuloTelefone.posicionarRotulo(522, self.yDist[1])
        
        
        self.rotuloEmail = Rotulo(self, 'E-mail')
        self.rotuloEmail.posicionarRotulo(659, self.yDist[1])

        #linha3
        self.rotuloEndereco = Rotulo(self, 'Endereço: Rua')
        self.rotuloEndereco.posicionarRotulo(57, self.yDist[3])
        self.rotuloNumero = Rotulo(self, 'Número')
        self.rotuloNumero.posicionarRotulo(388, self.yDist[3])
        self.rotuloBairro = Rotulo(self, 'Bairro')
        self.rotuloBairro.posicionarRotulo(494, self.yDist[3])

        #linha 5
        self.rotuloCidade = Rotulo(self, 'Cidade')
        self.rotuloCidade.posicionarRotulo(57, self.yDist[5])
        self.rotuloEstado = Rotulo(self, 'Estado')
        self.rotuloEstado.posicionarRotulo(189, self.yDist[5])
        self.rotuloCep = Rotulo(self, 'CEP')
        self.rotuloCep.posicionarRotulo(299, self.yDist[5])
        self.rotuloComplemento = Rotulo(self, 'Complemento')
        self.rotuloComplemento.posicionarRotulo(396, self.yDist[5])

        #linha 7
        self.selecioneProduto = Rotulo(self, 'Selecione o produto')
        self.selecioneProduto.posicionarRotulo(57, self.yDist[7])

        #linha 8
        self.btnAdicionarProduto = Botao(self, 'Adicionar', self.adicionarProduto, self.modo["corBotoesPadrao"])
        self.btnAdicionarProduto.posicionarBotao(57, self.yDist[8])
        self.btnExcluirProduto = Botao(self, 'Excluir', self.excluir, self.modo["corBotaoAtencao"])
        self.btnExcluirProduto.posicionarBotao(197, self.yDist[8])
        #linha 9
        self.itens = Rotulo(self, 'Itens selecionados')
        self.itens.posicionarRotulo(57, self.yDist[9])
        self.formaPagamento = Rotulo(self, 'Forma de pagamento')
        self.formaPagamento.posicionarRotulo(568, self.yDist[9])
        #linha 10
        self.verProdutos = Treeview(self, colunas['Cadastro'], 50, 57, self.yDist[10])
        self.verProdutos.treeviewCadastro()
        self.valor = Rotulo(self, 'Valor')
        self.valor.posicionarRotulo(299, self.yDist[10])
        self.cbxFormaPagamento = ctk.CTkComboBox(self, width=70, height=20, fg_color=self.modo['corDeFundo'],
                                                 font=(fontPrincipal, 12), dropdown_fg_color=self.modo['corDeFundo'],
                                                 text_color=self.modo['corPrincipalFonte'],
                                                 dropdown_text_color=self.modo['corPrincipalFonte'],
                                                 values=['PIX', 'Cartão de crédito', 'Cartão de débito', 'Dinheiro'])
        self.cbxFormaPagamento.place(x=568, y=self.yDist[10])
        #linha 11
        self.desconto = Rotulo(self, 'Desconto')
        self.desconto.posicionarRotulo(299, self.yDist[11])
        self.total = Rotulo(self, 'Total')
        self.total.posicionarRotulo(299, self.yDist[12])

        self.btnSalvar = Botao(self, 'Salvar', self.salvar, self.modo["corBotaoSave"])
        self.btnSalvar.botaoDestaque()
        self.btnSalvar.posicionarBotao(231, 450)
        self.btnGerarPedf = Botao(self, 'Gerar PDF', self.gerarPdf, self.modo['corBotoesPadrao'])
        self.btnGerarPedf.botaoDestaque()
        self.btnGerarPedf.posicionarBotao(497, 450)
        # linha 2
        self.inputNome = EntradaDados(self)
        self.inputTelefone = EntradaDados(self)
        self.inputDataNascimento = EntradaDados(self)
        self.inputEmail = EntradaDados(self)
        # linha 4
        self.inputRua = EntradaDados(self)
        self.inputNumero = EntradaDados(self)
        self.inputBairro = EntradaDados(self)
        self.inputBairro.entradaPlace(317, 494, self.yDist[4])
        # linha 6
        self.inputCidade = EntradaDados(self)
        self.inputEstado = EntradaDados(self)
        self.inputCep = EntradaDados(self)
        self.inputComplemento = EntradaDados(self)
        self.inputValor1 = EntradaDados(self)
        self.inputDesconto1 = EntradaDados(self)
        self.inputDesconto1.eventWrite(self.calcTotal)
        self.inputTotal1 = EntradaDados(self)
        self.inputsDadosCompra = [self.inputValor1, self.inputTotal1]
    
    def iniciarTelaComDados(self, dadosCliente, dadosProduto, dadosVenda, idVenda, idPagamento):
        try:
            self.clienteExistente = True
            self.vendaExistente = True
            self.pagamentoExistente = True
            self.itemVendidoExistente = True
            self.venda.setId(idVenda)
            self.pagamento.setId(idPagamento)
            self.itemVendido.setIdVenda(idVenda)
            
            #CPF CNPJ COM DADOS
            cpf = dadosCliente[0][1]
            cnpj = dadosCliente[0][2]
            self.inputCpfOuCnpj.place_forget()
            if cpf == "NULL":
                self.inputCpfOuCnpj.entradaComDados(cnpj)
                self.id = cnpj
            else:
                self.inputCpfOuCnpj.entradaComDados(cpf)
                self.id = cpf
            
            self.inputCpfOuCnpj.entradaPlace(136, 191, self.yDist[0])
            
            self.gerarRotulos()
            self.cbxFormaPagamento.place_forget()
            self.cbxFormaPagamento.set(dadosVenda[1])
            self.cbxFormaPagamento.place(x=568, y=self.yDist[10])
            self.inputTotal1.entradaComDados(dadosVenda[2])
            self.posicionarDadosDaCompra()
            
            self.btnSalvar.place_forget()
            self.btnAtualizarCompra = Botao(self, 'Atualizar', self.atualizarCompra(dadosProduto), self.modo["corBotaoSave"])
            self.btnAtualizarCompra.botaoDestaque()
            self.btnAtualizarCompra.posicionarBotao(231, 450)
            self.desabilitarInputs(dadosCliente[0])
            self.posicionarInputs()            
            # dados Produto
            for i in range(len(dadosProduto)):
                self.verProdutos.inserirDados(dadosProduto[i])
                tupla = (dadosProduto[i][0], dadosProduto[i][1], dadosProduto[i][-1], dadosProduto[i][2], dadosProduto[i][2])
                self.dadosProduto.append(tupla)              
            
        except Exception as e:
                messagebox.showerror("ERRO ao editar venda", f"{e}")
                
    def posicionarDadosDaCompra(self):
        self.inputValor1.entradaPlace(70, 370, self.yDist[10])
        self.inputDesconto1.entradaPlace(70, 370, self.yDist[11])
        self.inputTotal1.entradaPlace(70, 370, self.yDist[12])

    def posicionarInputs(self):
        self.inputNome.entradaPlace(317, 57, self.yDist[2])
        self.inputDataNascimento.entradaPlace(120, 388, self.yDist[2])
        self.inputTelefone.entradaPlace(120, 522, self.yDist[2])
        self.inputEmail.entradaPlace(150, 659, self.yDist[2])
        self.inputRua.entradaPlace(317, 57, self.yDist[4])
        self.inputNumero.entradaPlace(91, 388, self.yDist[4])
        self.inputCidade.entradaPlace(123, 57, self.yDist[6])
        self.inputEstado.entradaPlace(96, 189, self.yDist[6])
        self.inputCep.entradaPlace(80, 299, self.yDist[6])
        self.inputComplemento.entradaPlace(178, 396, self.yDist[6])

        self.inputsObridatorios = [self.inputNome, self.inputTelefone, self.inputEmail]
        self.inputEndereco = [self.inputRua, self.inputNumero, self.inputBairro, self.inputCidade, self.inputEstado,
                              self.inputCep, self.inputComplemento]
        self.inputs = [self.inputNome, self.inputDataNascimento, self.inputTelefone, self.inputEmail]  + self.inputEndereco

    def adicionarProduto(self):
        self.topLevelProduto = TelaPopUp(self, self.modo)

        # itens
        self.BuscarProdutos = EntradaDados(self.topLevelProduto)
        self.BuscarProdutos.entradaPesquisa(self.buscarProduto)
        self.BuscarProdutos.posicionarComPlace(91, 29)
        self.btnBuscarProduto = Botao(self.topLevelProduto, 'Buscar', self.buscarProduto, self.modo['corBotoesPadrao'])
        self.btnBuscarProduto.posicionarBotao(632, 29)
        self.tree = Treeview(self.topLevelProduto, colunas['Produtos'], 70, 100, 70)
        self.tree.altura(7)
        self.tree.gerarSroolvbarY()
        self.tree.configurarBarra(590, 70)
        self.tree.posicionarTree()

        self.qtd = Rotulo(self.topLevelProduto, "Quantidade: ")
        self.qtd.posicionarRotulo(300, 332)
        self.inputQtd = EntradaDados(self.topLevelProduto)
        self.inputQtd.entradaPlace(70, 400, 332)

        self.btnAdicionar = Botao(self.topLevelProduto, 'Adcionar', self.addProduto, self.modo["corBotaoSave"])
        self.btnAdicionar.botaoDestaque()
        self.btnAdicionar.posicionarBotaoRel(0.5, 0.9)

        self.topLevelProduto.mainloop()
    
    def atualizarCompra(self, dadosProduto):
        try:
            idsProduto = [(item[0]) for i, item in enumerate(self.dadosProduto)]
            precoUnit = [(item[2]) for i, item in enumerate(self.dadosProduto)]
            qtd = [(item[3]) for i, item in enumerate(self.dadosProduto)]
            novaQtd = [(item[4]) for i, item in enumerate(self.dadosProduto)]
            
            if len(idsProduto) == 0:
                messagebox.showerror('ERRO', 'Nenhum produto adicionado')
            else:
                for i in range(len(idsProduto)):
                    self.itemVendido.dados(self.itemVendido.idVenda, idsProduto[i], qtd[i], precoUnit[i])
                    self.itemVendido.editar()
                
                self.pagamento.editDados(self.cbxFormaPagamento.get(), self.inputValor1.getDados(), self.venda.id)
                self.pagamento.editar()
                
                atualizar = self.atualizarEstoque(idsProduto, novaQtd)
                if atualizar is True:               
                    messagebox.showinfo('Sucesso', 'Operação cadastrada')
                    self.place_forget()
                
        except Exception as e:
            messagebox.showerror('Erro ao cadastrar os dados', f'tente novamente {e}')

    def desabilitarInputs(self, lista):
        self.posicionarInputs()
        lista1 = list(lista[3:7])
        lista2 = list(lista[7].split())
        lista = lista1+lista2

        try:
            self.btnEditar = Botao(self, 'Editar', self.editar, self.modo["corBotaoAlerta"])
            self.btnEditar.posicionarBotao(596, self.yDist[6])
            self.bloquearInputs(lista, self.inputs)

        except:
            return None

    def getCpfCnpj(self, event=None):
        dado = self.inputCpfOuCnpj.getDados()
        valido = self.validarDados(dado, dado)
        if valido:
            self.verificarSeExiste()

    def validarDados(self, cpf, cnpj):
        self.cpf = self.cl.cpfValido(cpf)  
        self.cnpj = self.cl.cnpjValido(cnpj)

        if self.cpf is False and self.cnpj is False:
            messagebox.showerror("Número Inválido", "Verifique o número digitado")
            return False
        else:
            return True

    def verificarSeExiste(self):
        if self.cpf is True and self.cnpj is False:
            query = self.cl.buscar(self.cl.cpf, 'cpf')   
            if query != []:
                self.id = self.cl.cpf
                self.cl.setId(query[0][0])
                self.gerarRotulos()
                self.desabilitarInputs(query[0])
                self.posicionarInputs()
                self.clienteExistente = True
            else:
                self.id = self.cl.cpf
                self.gerarRotulos()
                self.posicionarInputs()
        elif self.cpf is False and self.cnpj is True:
            query = self.cl.buscar(self.cl.cnpj, 'cnpj')
            if query != []:
                self.id = self.cl.cnpj
                self.cl.setId(query[0][0])
                self.gerarRotulos()
                self.desabilitarInputs(query[0])
                self.posicionarInputs()
                self.clienteExistente = True
            else:
                self.id = self.cl.cnpj
                self.gerarRotulos()
                self.posicionarInputs()

    def salvar(self):    
        
        try:
            if self.clienteExistente is False:
                    self.criarCliente()
                    self.cl.cadastrar()
                    self.cl.buscarId(self.id, 'cpf')
                    self.cl.buscarId(self.id, 'cnpj')
            else:
                None
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            idsProduto = [(item[0]) for i, item in enumerate(self.dadosProduto)]
            precoUnit = [(item[2]) for i, item in enumerate(self.dadosProduto)]
            qtd = [(item[3]) for i, item in enumerate(self.dadosProduto)]
            novaQtd = [(item[4]) for i, item in enumerate(self.dadosProduto)]
            
            if len(idsProduto) == 0:
                messagebox.showerror('ERRO', 'Nenhum produto adicionado')
            else:
                if self.vendaExistente is False:
                    venda = self.criarVenda(data, self.cl.id)
                    if venda is True:
                            self.vendaExistente = True
                elif self.itemVendidoExistente is False:
                    itemVendido = self.criarItemPedido(self.venda.id, idsProduto, qtd, precoUnit)
                    if itemVendido is True:
                            self.itemVendidoExistente = True
                elif self.pagamentoExistente is False:
                    pagamento = self.criarPagamento(self.venda.data, self.inputValor1.getDados(), self.venda.id)
                    if pagamento is True:
                        self.pagamentoExistente = True
                
                atualizar = self.atualizarEstoque(idsProduto, novaQtd)
                if atualizar is True:               
                    messagebox.showinfo('Sucesso', 'Operação cadastrada')
                    self.place_forget()
                
        except:
            messagebox.showerror('Erro ao cadastrar os dados, tente novamente')
               

    def editar(self):
        # função para editar dados do cliente
        for i in range(len(self.inputs)):
            self.inputs[i].habilitar()

        self.btnEditar.place_forget()
        self.btnAtualizar = Botao(self, 'Atualizar', self.atualizar, self.modo["corBotoesPadrao"])
        self.btnAtualizar.posicionarBotao(596, self.yDist[6])

    def atualizar(self):
        # função para atualizar dados do cliente
        self.criarCliente()
        atualizar = self.cl.editar()
        if atualizar == 'Dados inseridos com sucesso':
            for i in range(len(self.inputs)):
                self.inputs[i].desabilitar()
            self.btnAtualizar.place_forget()
            self.btnEditar.posicionarBotao(596, self.yDist[6])
            messagebox.showinfo('Sucesso!', 'Dados alterados.')
        else:
            messagebox.showerror("ERRO", f"{atualizar}")

    def excluir(self):
        id = self.verProdutos.itemSelecionado()[0]
        self.removerProduto(id)
        self.verProdutos.deletarItem()
        self.calcTotal()
    
    def removerProduto(self, idToRemove):
        for i, item in enumerate(self.dadosProduto):
            if item[0] == idToRemove:
                self.dadosProduto.pop(i)

    def gerarPdf(self):
        pass

    def buscarProduto(self, *args):
        try:
            self.tree.deletarDados()
        finally:
            dado = self.BuscarProdutos.getDados()
            busca = self.produto.buscarEmTudo(dado)
            if not busca:
                messagebox.showinfo('Pesquisa', 'Termo não encontrado.', parent=self.topLevelProduto)
            else:
                for i in range(len(busca[0])):
                    self.tree.inserirDados(busca[0][i])
                self.BuscarProdutos.limpar()

    def addProduto(self):
        # adiciona os produtos para a tela cadastro        
        try:
            dados = self.tree.itemSelecionado()
            qtd = (self.inputQtd.getDados())
            if dados is None:
                messagebox.showerror("ERRO: Item não selecionado", f"Selecione um item para adicionar")          
            elif qtd == '' or qtd.isnumeric() == False:
                messagebox.showerror("ERRO: Quantidade Inválida", f"Insira números inteiros")
            elif self.verificarProdutoNaLista(dados[0]) is True:
                messagebox.showerror("ERRO: Produto está na lista", f"Exclua e insira novamente com a nova Quantidade", parent=self.topLevelProduto)
            else:
                qtd = int(qtd)
                novaQtd = self.compararQuatidade(dados[4], qtd)
                if novaQtd >= 0:
                    inserir = (dados[0], dados[1], dados[-1], qtd)
                    self.verProdutos.inserirDados(inserir)
                    for i in self.inputsDadosCompra:
                        i.place_forget()
                    tupla = (dados[0], dados[1], dados[-1], qtd, novaQtd)
                    self.dadosProduto.append(tupla)
                    self.calcTotal()
                    self.posicionarDadosDaCompra()
                    self.topLevelProduto.destroy()
                    
        except Exception as e:
            messagebox.showerror("ERRO ao adicionar o produto", f"{e}")
                
    def verificarProdutoNaLista(self, idProduto):
        idsProduto = [(item[0]) for i, item in enumerate(self.dadosProduto)]
        if idProduto in idsProduto:
            return True
        else:
            False
    
    def bloquearInputs(self, dados, listaInputs):
        for i in range(len(listaInputs)):
                listaInputs[i].entradaComDados(dados[i])
                listaInputs[i].desabilitar()

    def compararQuatidade(self, estoque, qtd):
        try:
            qtd = int(qtd)
            estoque = int(estoque)
        except Exception as e:
            messagebox.showerror("ERRO", f"Digite apenas números inteiros. {e}")
            
        if qtd > estoque:
            return messagebox.showerror("ERRO", f"Quantidade selecionada é superior ao estoque")
        else:
            novaqtd = estoque-qtd
            return novaqtd
        

    def calcTotal(self, *args):
        try:
            for i in self.inputsDadosCompra:
                i.limpar()
        finally:
            total = sum((float(self.verProdutos.set(i, 2)) * float(self.verProdutos.set(i, 3))) for i in
                        self.verProdutos.get_children())
            self.inputValor1.entradaComDados(total)

        try:
            desconto = self.inputDesconto1.getDados()
            if len(desconto) == 0:
                self.inputTotal1.entradaComDados(total)
            else:
                calcFinal = total - (total * (float(desconto) / 100))
                self.inputTotal1.entradaComDados(calcFinal)
        except:
            None

        self.posicionarDadosDaCompra()

    def entradaEmBranco(self, lista):
        for i in range(len(lista)):
            if lista[i].getDados() == '':
                lista[i].mudarBorda()
                return True
            else:
                return False

    def criarCliente(self):
        while True:
            try:
            # verificando itens de preenchimento obrigatório vazios
                vazio = self.entradaEmBranco(self.inputsObridatorios)
                if vazio is True:
                    messagebox.showerror("ERRO", "Há dados não preenchidos, por favor, verifique!")
                    break
                
                # validando entrada de dados restantes
                telvalido = self.cl.telValido(self.inputTelefone.getDados())
                emailValido = self.cl.emailValido(self.inputEmail.getDados())
                dataValida = self.cl.dataValida(self.inputDataNascimento.getDados())
                
                if telvalido == False:
                    messagebox.showerror("ERRO", "telefone inválido, por favor, verifique!")
                    break
                elif emailValido == False:
                    messagebox.showerror("ERRO", "E-mail inválido, por favor, verifique!")
                    break
                else:                                       
                    self.cl.setNome(self.inputNome.getDados())
                    endereco = self.getAllValues(self.inputEndereco)
                    enderecoCompleto = ', '.join(endereco)
                    self.cl.setEndereco(enderecoCompleto)
                    break
                    
            except Exception as e:
                messagebox.showerror("Erro ao cadastrar Cliente", f"{e}")
                break

    def criarVenda(self, data, idCliente):
        try:
            self.venda.dadosVenda(data, idCliente)
            cadastrar = self.venda.cadastrar()
            buscarId = self.venda.buscarId()
            if cadastrar != 'Dados inseridos com sucesso' or buscarId is None:
                return False
            else:
                return True
        except Exception as e:
            messagebox.showerror('Erro ao cadastrar Venda', f'{e}')

    def criarItemPedido(self, idVenda, listaProdutos, listaQtd, listaPreco):
        try:
            for i in range(len(listaProdutos)):
                self.itemVendido.dados(idVenda, listaProdutos[i], listaQtd[i], listaPreco[i])
                cadastrar = self.itemVendido.cadastrar()
                if cadastrar == 'Dados inseridos com sucesso':
                    return True
                else:
                    False
        except Exception as e:
            messagebox.showerror('Erro ao cadastrar Pedido', f'{e}')

    def criarPagamento(self, data, valor, idVenda):
        formaPg = self.cbxFormaPagamento.get()
        self.pagamento.dados(data, formaPg, valor, idVenda)
        try:
            cadastrar = self.pagamento.cadastrar()
            if cadastrar == 'Dados inseridos com sucesso':
                    return True
            else:
                False
        except Exception as e:
            messagebox.showerror('Erro ao cadastrar Pagamento', f'{e}')
            
    def atualizarEstoque(self, idsProdutos, listaQuantidade):
        try:
            for i in range(len(idsProdutos)):
                atualizar = self.produto.editarEstoque(listaQuantidade[i], idsProdutos[i])
                if atualizar == 'Dados inseridos com sucesso':
                    return True
                else:
                    False
        except Exception as e:
            messagebox.showerror('Erro ao atualizar estoque', f'{e}')
