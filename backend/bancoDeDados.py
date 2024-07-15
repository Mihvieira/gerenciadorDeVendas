import sqlite3
import sys

class BancoDeDados:
    #Define condições gerais do BD
    def __init__(self):
        self.criarTabelas()

    def conectar(self):
        self.con = sqlite3.connect('GerenciarVendas.db')
        self.cursor = self.con.cursor()

    def desconectar(self):
        self.cursor.close()
        self.con.close()

    def inserirDados(self, query):
        self.conectar()
        with self.con:
            try:
                self.cursor.execute(query)
                self.con.commit()
                return 'Dados inseridos com sucesso'
            except sqlite3.OperationalError as e:
                self.con.rollback()
                print(f"Erro de conexão: {e}")
            except sqlite3.ProgrammingError as e:
                self.con.rollback()
                print(f"Erro na consulta: {e}")
            except sqlite3.IntegrityError as e:
                self.con.rollback()
                print(f"Erro na consulta: {e}")
            except Exception as e:
                self.con.rollback()
                print(f"Erro inesperado: {e}")

    def consultar(self, query):
        self.conectar()
        with self.con:
            try:
                self.cursor.execute(query)
                return self.cursor.fetchall()
            except Exception as e:
                return f"Erro ao consultar dados {e}"
    
    def criarTabelas(self):
        self.conectar()
        self.criarTabelaCliente()
        self.criarTabelaProduto()
        self.criarTabelaVenda()
        self.criarTabelaItemVendido()
        self.criarTabelaPagamento()
        self.desconectar()
        return 'tabelas criadas com sucesso'
    
    def criarTabelaCliente(self):
        with self.con:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cliente(
            idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf TEXT,
            cnpj TEXT,
            nome TEXT not null,
            nascimento TEXT,
            telefone TEXT,
            email TEXT,
            endereco TEXT
            );
            ''')
            self.con.commit()
    
    def criarTabelaVenda(self):
        with self.con:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Venda(
            idVenda INTEGER PRIMARY KEY AUTOINCREMENT,
            idCliente INTEGER,
            dataHora TEXT,
            status TEXT,
            constraint fk_venda_cliente foreign key (idCliente) references Cliente(idCliente)
            );
            ''')
            self.con.commit()
    
    def criarTabelaProduto(self):
        with self.con:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produto(
            idProduto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            estoque INTEGER,
            desconto REAL,
            total REAL
            );
            ''')
            self.con.commit()
    
    def criarTabelaItemVendido(self):
        with self.con:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ItemVendido(
            idVenda INTEGER,
            idProduto INTEGER,
            quantidade INTEGER,
            precoUnit REAL,
            constraint fk_Item_Venda foreign key (idVenda) references Venda(idVenda) ON UPDATE CASCADE,
            constraint fk_Item_produto foreign key (idProduto) references Produto(idProduto)            
            );
            ''')
            self.con.commit()
    
    def criarTabelaPagamento(self):
        with self.con:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pagamento(
            idPagamento INTEGER PRIMARY KEY AUTOINCREMENT,
            idVenda INTEGER,
            data TEXT,
            tipo TEXT,
            valor REAL,
            constraint fk_pgto_venda foreign key (idVenda) references Venda(idVenda) ON UPDATE CASCADE
            );
            ''')
            self.con.commit()
    
    
    
    