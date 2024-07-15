from backend.bancoDeDados import *
import re
from dateutil import parser

class Pessoa:
    def __init__(self):
        self.cpf = 'NULL'
        self.cnpj = 'NULL'
        self.nome = 'NULL'
        self.dataNascimento = 'NULL'
        self.telefone = 'NULL'
        self.email = 'NULL'
        self.endereco = 'NULL'
        self.bd = BancoDeDados()

    def dadosBasicos(self, nome, telefone, email):
        self.nome = nome.title()
        self.telefone = telefone
        self.email = email.lower()
    
    def setNome(self, nome):
        self.nome = nome.title()
    
    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    def setEndereco(self, endereco):
        self.endereco = endereco

    def filtrarCaracteres(self, string):
        filtro = '.,-/*$^?~[]'
        return [char for char in string if char not in filtro and char.isnumeric()]

    def cpfValido(self, cpf):
        cpf = cpf.strip()
        cpf = self.filtrarCaracteres(cpf)
        cpf_filtrado = ''.join(cpf)
        pattern = "\d{3}\.\d{3}\.\d{3}-\d{2}"
        self.cpf_formatado = '{}.{}.{}-{}'.format(cpf_filtrado[:3], cpf_filtrado[3:6], cpf_filtrado[6:9], cpf_filtrado[-2:])

        if re.match(pattern, self.cpf_formatado):
            self.cpf = self.cpf_formatado
            return True
        else:
            return False

    def cnpjValido(self, cnpj):
        cnpj = cnpj.strip()
        cnpj = self.filtrarCaracteres(cnpj)
        cnpj_filtrado = ''.join(cnpj)
        pattern = "\d{2}\.\d{3}\.\d{3}\/000\d{1}\-\d{2}"
        self.cnpj_formatado = '({}){}.{}/{}-{}'.format(cnpj_filtrado[:2], cnpj_filtrado[2:5], cnpj_filtrado[5:8], cnpj_filtrado[8:12], cnpj_filtrado[-2:])
        if re.match(pattern, self.cnpj_formatado):
            self.cpf = self.cnpj_formatado
            return True
        else:
            return False

    def telValido(self, tel):
        tel_formatado = '({}){}-{}'.format(tel[:2], tel[2:7], tel[7:11])
        pattern = r"^(\(\d{2}\)9\d{4}-\d{4})$"
        resultado = re.match(pattern, tel_formatado)
        if resultado:
            return True
        else:
            return False
    

    def emailValido(self, email):
        pattern = r"(^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$)"

        if re.match(pattern, email):
            self.email = email
            return True
        else:
            return False
    
    def dataValida(self, data):
        try:
            date_obj = parser.parse(data)
            self.dataNascimento = data
            return True
        except ValueError:
            return False

class Cliente(Pessoa):
    def __init__(self):
        super().__init__()
        self.tabela = 'Cliente'
        self.id = None

    def cadastrar(self):
        query = (f'INSERT INTO {self.tabela} (cpf, cnpj, nome, nascimento, telefone, email, endereco) VALUES ('
                       f'"{self.cpf}", "{self.cnpj}", "{self.nome}", "{self.dataNascimento}", "{self.telefone}", "{self.email}",'
                       f'"{self.endereco}")')
        return self.bd.inserirDados(query)

    def editar(self):
        query = f'UPDATE {self.tabela} SET cpf="{self.cpf}", cnpj="{self.cnpj}", nome="{self.nome}", nascimento="{self.dataNascimento}", telefone="{self.telefone}", email="{self.email}", endereco="{self.endereco}" WHERE idCliente={self.id}'
        return self.bd.inserirDados(query)

    def excluir(self):
        query = f'DELETE FROM {self.tabela} WHERE idCliente="{self.id}"'
        return self.bd.inserirDados(query)

    def buscar(self, valor, param):
        query = f'SELECT * FROM {self.tabela} WHERE {param}="{valor}"'
        resultado = self.bd.consultar(query)
        return resultado

    def buscarId(self, valor, param):
        query = f'SELECT id FROM {self.tabela} WHERE {param}="{valor}"'
        resultado = self.bd.consultar(query)
        if resultado != []:
            self.setId(resultado[0])
        return self.id
    
    def buscarEmTudo(self, valor):
        param = ['cpf', 'cnpj', 'nome', 'nascimento', 'telefone', 'email', 'endereco']
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
        return [self.id, self.cpf, self.cnpj, self.nome, self.dataNascimento, self.telefone, self.email, self.endereco]

