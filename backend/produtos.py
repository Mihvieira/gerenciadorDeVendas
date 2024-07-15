from backend.bancoDeDados import *
from gui.variaveis import colunas


class Produto:
    def __init__(self):
        self.bd = BancoDeDados()
        self.id = None
        self.tabela = 'Produto'
        
    def criar(self, nome, desc, preco, estoque, desconto):
        self.nome = nome
        self.descricao = desc
        self.preco = float(preco.replace(',', '.'))
        self.estoque = estoque.replace(',', '.')
        self.desconto = float(desconto) if desconto != '' else 0
        self.total = self.preco-(self.preco*(self.desconto/100))

    def cadastrar(self):
        query = (f'INSERT INTO {self.tabela} (nome, descricao, preco, estoque, desconto, total) VALUES ("{self.nome}", "{self.descricao}", "{self.preco}", "{self.estoque}", "{self.desconto}", "{self.total}")')
        return self.bd.inserirDados(query)

    def editar(self):
        query = f'UPDATE {self.tabela} SET nome="{self.nome}", descricao="{self.descricao}", preco="{self.preco}", estoque="{self.estoque}", desconto="{self.desconto}", total="{self.total}" WHERE idProduto={self.id}'
        return self.bd.inserirDados(query)
    
    def editarEstoque(self, est, idproduto):
        query = f'UPDATE {self.tabela} SET estoque="{est}" WHERE idProduto={idproduto}'
        return self.bd.inserirDados(query)
    
    def buscarEstoque(self, id):
        pass

    def excluir(self):
        query = f'DELETE FROM {self.tabela} WHERE idProduto="{self.id}"'
        return self.bd.inserirDados(query)

    def buscar(self, valor, param):
        query = f'SELECT * FROM {self.tabela} WHERE {param}="{valor}"'
        resultado = self.bd.consultar(query)
        return resultado
    
    def buscarId(self, valor, param):
        query = f'SELECT id FROM {self.tabela} WHERE {param}="{valor}"'
        resultado = self.bd.consultar(query)
        self.setId(resultado[0])
        return self.id
    
    def buscarEmTudo(self, valor):
        param = ['nome', 'descricao', 'preco', 'estoque', 'desconto', 'total']
        lista = []
        for i in param:
            query = f'SELECT * FROM {self.tabela} WHERE {i}="{valor}"'
            resultado = self.bd.consultar(query)
            if len(resultado) != 0:
                lista.append(resultado)
        return lista

    def buscarTodos(self):
        query = f'SELECT * FROM {self.tabela}'
        resultado = self.bd.consultar(query)
        return resultado
    
    def setId(self, id):
        self.id = id
    
    def verAtributos(self):
        return [self.id, self.nome, self.descricao, self.preco, self.estoque, self.desconto, self.total]
