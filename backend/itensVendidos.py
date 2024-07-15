from backend.bancoDeDados import BancoDeDados
from backend.produtos import *


class ItemVendido:
    def __init__(self):
        self.tabela = 'ItemVendido'
        self.idVenda = 'NULL'
        self.IdProduto = 'NULL'
        self.qtd = 'NULL'
        self.precoUnitario = 'NULL'
        self.bd = BancoDeDados()
    
    def dados(self, idVenda, idsProdutos, qtd, precoUnitario):
        self.idVenda = idVenda
        self.IdProduto = idsProdutos
        self.qtd = qtd
        self.precoUnitario = precoUnitario

    def cadastrar(self):
        query = (f'INSERT INTO {self.tabela} (idVenda, idProduto, quantidade, precoUnit) VALUES ('
                 f'"{self.idVenda}", "{self.IdProduto}", "{self.qtd}", "{self.precoUnitario}")')
        resultado = self.bd.inserirDados(query)
        if resultado == 'Dados inseridos com sucesso':
            'queryProduto = '
        return resultado

    def editar(self):
        query = f'UPDATE {self.tabela} SET idProduto="{self.IdProduto}", quantidade="{self.qtd}", precoUnit="{self.precoUnitario}" WHERE idVenda="{self.idVenda}"'
        return self.bd.inserirDados(query)

    def excluir(self, idVenda):
        query = f'DELETE FROM {self.tabela} WHERE idVenda="{idVenda}"'
        return self.bd.inserirDados(query)

    def buscar(self, valor, param):
        query = f'SELECT * FROM {self.tabela} WHERE {param}="{valor}"'
        resultado = self.bd.consultar(query)
        return resultado

    def calcularValorTotal(self):
        return self.precoUnitario * self.qtd
    
    def setIdVenda(self, idVenda):
        self.idVenda = idVenda
