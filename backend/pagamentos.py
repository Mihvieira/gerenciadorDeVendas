from backend.bancoDeDados import BancoDeDados


class Pagamento:
    def __init__(self):
        self.tabela = 'Pagamento'
        self.id = None
        self.data = 'NULL'
        self.tipo = 'NULL'
        self.valor = 'NULL'
        self.idVenda = 'NULL'
        self.bd = BancoDeDados()
    
    def dados(self, data, tipo, valor, idVenda):
        self.data = data
        self.tipo = tipo
        self.valor = valor
        self.idVenda = idVenda
    
    def editDados(self, tipo, valor, idVenda):
        self.tipo = tipo
        self.valor = valor
        self.idVenda = idVenda
        
    def cadastrar(self):
        query = (f'INSERT INTO {self.tabela} (idVenda, data, tipo, valor) VALUES ('
                 f'"{self.idVenda}", "{self.data}", "{self.tipo}", "{self.valor}")')
        return self.bd.inserirDados(query)

    def editar(self):
        query = f'UPDATE {self.tabela} SET tipo="{self.tipo}", valor="{self.valor}" WHERE idPagamento={self.id}'
        return self.bd.inserirDados(query)

    def excluir(self, idVenda):
        query = f'DELETE FROM {self.tabela} WHERE idVenda="{idVenda}"'
        return self.bd.inserirDados(query)

    def buscar(self, valor, param):
        query = f'SELECT * FROM {self.tabela} WHERE {param}="{valor}"'
        resultado = self.bd.consultar(query)
        self.id = self.id = resultado[0] if resultado != '' else None
        return resultado
    
    def buscarEmTudo(self, valor):
        param = ['idPagamento', 'idVenda', 'data', 'tipo', 'valor']
        lista = []
        for i in param:
            query = f'SELECT * FROM {self.tabela} WHERE {i}="{valor}"'
            resultado = self.bd.consultar(query)
            if len(resultado) != 0:
                lista.append(resultado)
        return lista
    
    def setId(self, id):
        self.id = id
    
    def setData(self, data):
        self.data = data