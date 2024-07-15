from tkinter import messagebox
from backend.clientes import Cliente
from gui.quadros import *
from gui.telaCadastro import TelaCadastro


class TelaClientes(Quadro):
    def __init__(self, parent, modo):
        super().__init__(parent, modo)
        self.cl = Cliente()
        self.colunas = colunas['Clientes']
        self.configure(width=852, height=520, fg_color=self.modo["corQuadroPrincipal"], corner_radius=0)
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
        self.tree = Treeview(self, self.colunas, 120, 20, 70)
        self.tree.tamanhoColuna('id', 20)
        self.tree.tamanhoColuna('DtNasc.', 90)
        self.tree.tamanhoColuna('Telefone', 90)
        self.tree.altura(7)
        self.tree.gerarSroolvbarY()
        self.tree.configurarBarra(830,70)
        self.tree.posicionarTree()

        self.btnEditar = Botao(self, 'Editar', self.editar, self.modo["corBotaoAtencao"])
        self.btnEditar.posicionarBotao(300, 250)
        self.btnExcluirProdutoT = Botao(self, 'Excluir', self.excluir, self.modo["corBotaoAlerta"])
        self.btnExcluirProdutoT.posicionarBotao(400, 250)
        self.btnIncluirNovo = Botao(self, 'Incluir Novo', self.incluirNovo, self.modo["corBotoesPadrao"])
        self.btnIncluirNovo.botaoDestaque()
        self.btnIncluirNovo.posicionarBotao(20, 250)

    def gerarBlocoEdicao(self):
        self.frameEdicao = Quadro(self, self.modo)
        self.frameEdicao.gerarFramePadrao(737, 167, self.modo['corDeFundo'])
        self.frameEdicao.calcGapVertical(5, 26, 3)
        self.rotuloNome = Rotulo(self.frameEdicao, 'Nome')
        self.rotuloNome.posicionarRotulo(5, self.frameEdicao.yDist[0])
        self.rotuloEnd = Rotulo(self.frameEdicao, 'Endereço')
        self.rotuloEnd.posicionarRotulo(336, self.frameEdicao.yDist[0])
        self.rotuloEmail = Rotulo(self.frameEdicao, 'E-mail')
        self.rotuloEmail.posicionarRotulo(470, self.frameEdicao.yDist[0])
        self.rotulodtNascimento = Rotulo(self.frameEdicao, 'Dt. Nascimento')
        self.rotulodtNascimento.posicionarRotulo(604, self.frameEdicao.yDist[0])
        
        self.inputNome = EntradaDados(self.frameEdicao)
        self.inputEnd = EntradaDados(self.frameEdicao)
        self.inputEmail = EntradaDados(self.frameEdicao)
        self.inputDataNascimento = EntradaDados(self.frameEdicao)
        
        self.rotuloTel = Rotulo(self.frameEdicao, 'Telefone')
        self.rotuloTel.posicionarRotulo(5, self.frameEdicao.yDist[2])
        self.rotulocpf = Rotulo(self.frameEdicao, 'CPF')
        self.rotulocpf.posicionarRotulo(120, self.frameEdicao.yDist[2])
        self.rotulocnpj = Rotulo(self.frameEdicao, 'CNPJ')
        self.rotulocnpj.posicionarRotulo(220, self.frameEdicao.yDist[2])
        
        self.inputTel = EntradaDados(self.frameEdicao)
        self.inputCpf = EntradaDados(self.frameEdicao)
        self.inputCnpj = EntradaDados(self.frameEdicao)
        
        self.btnSalvar = Botao(self.frameEdicao, 'Salvar', self.salvar, self.modo["corBotaoSave"])
        self.btnSalvar.botaoDestaque()
        self.btnSalvar.posicionarBotao(348, self.frameEdicao.yDist[3])

        self.frameEdicao.posicionarFrame(51, 300)
        
        self.inputs=[self.inputCpf, self.inputCnpj,  self.inputNome, self.inputDataNascimento, self.inputTel, self.inputEmail, self.inputEnd]
    
    def posicionarEntradaEdicao(self):
        self.inputNome.entradaPlace(317, 5, self.frameEdicao.yDist[1])
        self.inputEnd.entradaPlace(120, 336, self.frameEdicao.yDist[1])
        self.inputEmail.entradaPlace(120, 470, self.frameEdicao.yDist[1])
        self.inputDataNascimento.entradaPlace(120, 604, self.frameEdicao.yDist[1])
        self.inputTel.entradaPlace(90, 5, self.frameEdicao.yDist[3])
        self.inputCpf.entradaPlace(91, 120, self.frameEdicao.yDist[3])
        self.inputCnpj.entradaPlace(100, 220, self.frameEdicao.yDist[3])

    def buscar(self):
        try:
            self.tree.deletarDados()
        finally:
            dado = self.entrada.getDados()
            busca = self.cl.buscarEmTudo(dado)
            if not busca:
                messagebox.showinfo('Pesquisa', 'Termo não encontrado.')
            else:
                for i in range(len(busca[0])):
                    self.tree.inserirDados(busca[0][i])
                self.entrada.limpar()
    
    def verTodos(self):
        dado = self.entrada.getDados()
        busca = self.cl.buscarTodos()
        if not busca:
            messagebox.showinfo('Pesquisa', 'Nada encontrado.')
        else:
            for i in range(len(busca)):
                self.tree.inserirDados(busca[i])
            self.entrada.limpar()
        
    def salvar(self):
        criarCliente = self.criar()
        verifica = self.verificarSeExiste()
        if criarCliente == True and verifica == False:
            salvar = self.cl.cadastrar()
            if salvar == 'Dados inseridos com sucesso':
                self.frameEdicao.place_forget()
                messagebox.showinfo('Sucesso!', 'Dados cadastrados.')
            else:
                messagebox.showerror("ERRO", f"{salvar}")
    
    def validarDados(self, cpf, cnpj, telefone, email, data):
        while True:
            self.cpf = self.cl.cpfValido(cpf)
            self.cnpj = self.cl.cnpjValido(cnpj)
            telvalido = self.cl.telValido(telefone)
            emailValido = self.cl.emailValido(email) if email != '' else None
            dataValida = self.cl.dataValida(data) if data != '' else None
            
            if telvalido == False:
                messagebox.showerror("ERRO", "telefone inválido, por favor, verifique!")
                break
            elif self.cpf == False and self.cnpj == False:
                messagebox.showerror("Número Inválido", "Verifique o CPF e o CNPJ!")
                break
            elif emailValido == False:
                messagebox.showerror("ERRO", "E-mail inválido!")
                break
            elif dataValida == False:
                messagebox.showerror("ERRO", "Data inválida, digite no formato dd/mm/aaaa")
                break
            else:            
                return True
                break
    
    def verificarSeExiste(self):
        if self.cpf == True and self.cnpj == False:
            query = self.cl.buscar(self.cl.cpf, 'cpf')
            if query != []:
                messagebox.showerror("CPF já cadastrado", "Verifique o número ou busque no cadastro!")
                return True
            else:
                return False 
        elif self.cpf == False and self.cnpj == True:
            query = self.cl.buscar(self.cl.cnpj, 'cnpj')
            if query != None:
                messagebox.showerror("CNPJ já cadastrado", "Verifique o número ou busque no cadastro!")
                return True
            else:
                return False
                  
    def editar(self):
        try:
            dados = self.tree.itemSelecionado()
            self.cl.setId(dados[0])
            dados.pop(0)
            self.gerarBlocoEdicao()
            self.btnSalvar.place_forget()
            self.btnAtualizar = Botao(self.frameEdicao, 'Atualizar', self.atualizar, self.modo["corBotoesPadrao"])
            self.btnAtualizar.botaoDestaque()
            self.btnAtualizar.posicionarBotao(348, self.frameEdicao.yDist[3])
            self.gerarDadosEntrada(dados)
            self.tree.deletarItem()
            self.posicionarEntradaEdicao()
        except TypeError:
            messagebox.showerror('Erro', 'Nenhum item selecionado')
        except Exception as e:
            messagebox.showerror('Erro ao editar', f'{e}')
    
    def gerarDadosEntrada(self, dados):
        for i in range(len(self.inputs)):
            self.inputs[i].entradaComDados(dados[i])
            
    def atualizar(self):
        try:
            self.criar()
            atualizar = self.cl.editar()
            if atualizar == 'Dados inseridos com sucesso':
                self.limparEntrada(self.inputs)
                self.frameEdicao.place_forget()
                messagebox.showinfo('Sucesso!', 'Dados alterados.')
                self.tree.inserirDados(self.cl.verAtributos())
            else:
                messagebox.showerror("ERRO", f"{atualizar}")
        except TypeError:
            messagebox.showerror('Erro', 'Nenhum item selecionado')
        except Exception as e:
            messagebox.showerror('Erro ao atualizar', f'{e}')
        
    def excluir(self):
        try:
            dados = self.tree.itemSelecionado()
            self.cl.setId(dados[0])
            deletar = self.cl.excluir()
            if deletar == 'Dados inseridos com sucesso':
                self.tree.deletarItem()
                messagebox.showinfo('Sucesso!', 'Dados excluídos.')
            else:
                messagebox.showerror("ERRO", f"{deletar}")
        except TypeError:
            messagebox.showerror('Erro', 'Nenhum item selecionado')
        except Exception as e:
            messagebox.showerror('Erro ao excluir', f'{e}')
    
    def incluirNovo(self):
        self.gerarBlocoEdicao()
        self.posicionarEntradaEdicao()
    
    def criar(self):
        valido = self.validarDados(self.inputCpf.getDados(), self.inputCnpj.getDados(), self.inputTel.getDados(), self.inputEmail.getDados(), self.inputDataNascimento.getDados())

        if valido:
                self.cl.setNome(self.inputNome.getDados())
                self.cl.setEndereco(self.inputEnd.getDados())
                return True
        else:
            return False
