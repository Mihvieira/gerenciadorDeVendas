from backend.bancoDeDados import BancoDeDados
from backend.pagamentos import *


class Venda:
    def __init__(self):
        self.bd = BancoDeDados()
        self.tabela = 'Venda'
        self.id = 'NULL'
        self.data = 'NULL'
        self.idCliente = 'NULL'
        self.status = 'Finalizado'
    
    def dadosVenda(self, data, idCliente):
        self.data = data
        self.idCliente = idCliente
    
    def mudarStatus(self, status):
        self.status = status
        
    def cadastrar(self):
        query = (f'INSERT INTO {self.tabela} (idCliente, dataHora, status) VALUES ('f'"{self.idCliente}", "{self.data}", "{self.status}")')
        return self.bd.inserirDados(query)

    def editar(self):
        query = f'UPDATE {self.tabela} SET idCliente="{self.idCliente}", dataHora="{self.data}", status="{self.status}" WHERE idVenda={self.id}'
        return self.bd.inserirDados(query)
    
    def editarStatus(self, status, idVenda):
        query = f'UPDATE {self.tabela} SET status="{status}" WHERE idVenda={idVenda}'
        return self.bd.inserirDados(query)
    
    def excluir(self, valor, param):
        query = f'DELETE FROM {self.tabela} WHERE {param}="{valor}"'
        return self.bd.inserirDados(query)

    def buscar(self, valor, param):
        query = f'SELECT * FROM {self.tabela} v, Pagamento p WHERE {param}.v="{valor}" and idVenda.v=idVenda.p'
        resultado = self.bd.consultar(query)
        Id = resultado[0] if resultado != '' else None
        self.setId(Id)
        return resultado
    
    def buscarEmTudo(self, valor):
        param = ['idVenda','idCliente', 'dataHora', 'status']
        lista = []
        for i in param:
            query = f'SELECT * FROM {self.tabela} AS v, Pagamento AS p WHERE v.{i}="{valor}" and v.idVenda=p.idVenda'
            resultado = self.bd.consultar(query)
            if len(resultado) != 0:
                lista.append(resultado)
        return lista        
    
    def buscarTodos(self):
        query = f'SELECT * FROM {self.tabela} AS v, Pagamento AS p WHERE v.idVenda=p.idVenda'
        resultado = self.bd.consultar(query)
        return resultado

    def buscarId(self):
        query = f'SELECT * FROM {self.tabela} WHERE dataHora="{self.data}" and idCliente={self.idCliente}'
        resultado = self.bd.consultar(query)
        Id = resultado[0][0] if resultado != '' else None
        self.setId(Id)
        return self.id

    def setId(self, id):
        self.id = id