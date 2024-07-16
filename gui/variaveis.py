fontPrincipal = 'Inter'

icones = {
    "cadastro": "cadastro.png",
    "produtos": "produtos.png",
    "vendas": "vendas.png",
    "clientes": "clientes.png",
    "configuracao": "configuracao.png",
    "home": "home.png",
    "adicionarPessoa": "adicionar_pessoa.png",
    "usuario": "usuario.png",
    "dashboard": "dashboard.png"
}

# Dark Mode - Modo Escuro
modoEscuro = {
    "corPrincipalFonte": "#FFFFFF",
    "corSecundariaFonte": "#656D7A",
    "corMenuLateral": "#1E1E1E",
    "corQuadroPrincipal": "#080915",
    "corQuadroSecundario": "#101227",
    "corBotoesPadrao": "#1B75FA",
    "corBotaoAtencao": "#D3A93E",
    "corBotaoAlerta": "#FA281B",
    "corBotaoSave": "#34A853",
    "corDeFundo": "#444444"
}

caminhoImagens = r"imagens/icons/"

colunas = {
    'Clientes': ['id', 'Cpf', 'Cnpj', 'Nome', 'DtNasc.', 'Telefone', 'E-mail', 'endereço'],
    'Produtos': ['id', 'Nome', 'Descrição', 'Preço', 'Est.', 'Desc', 'Total'],
    'Cadastro': ['id', 'Nome', 'preço', 'Qtd'],
    'Vendas': ['id', 'idCl', 'dtVenda', 'Status', 'idPag', 'idProd', 'dataPg', 'FormaPgt', 'Total'],
}
