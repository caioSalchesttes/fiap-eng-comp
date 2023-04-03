from flask import Flask, request

app = Flask(__name__)

clientes = []
produtos = []
vendas = {}

class Cliente:
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

class PessoaFisica(Cliente):
    def __init__(self, endereco, email, telefone, nome, cpf, numero_celular):
        super().__init__(endereco, email, telefone)
        self.nome = nome
        self.cpf = cpf
        self.numero_celular = numero_celular

class PessoaJuridica(Cliente):
    def __init__(self, endereco, email, telefone, cnpj, razao_social, site):
        super().__init__(endereco, email, telefone)
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.site = site

class Produto:
    def __init__(self, id, nome, preco, descricao):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

@app.route('/', methods=['GET'])
def menu():
    return '''
        <h1>Bem-vindo(a) ao sistema de cadastro e vendas</h1>
        <p>Selecione uma das opções abaixo:</p>
        <ul>
            <li><a href="/cadastrar_cliente">Cadastrar cliente</a></li>
            <li><a href="/ver_dados_cliente">Ver dados de um cliente específico</a></li>
            <li><a href="/ver_todos_clientes">Visualizar todos os dados dos clientes cadastrados</a></li>
            <li><a href="/cadastrar_produto">Cadastrar produto</a></li>
            <li><a href="/ver_dados_produto">Ver dados de um produto específico</a></li>
            <li><a href="/ver_todos_produtos">Visualizar todos os dados dos produtos cadastrados</a></li>
            <li><a href="/efetuar_venda">Efetuar uma venda</a></li>
            <li><a href="/ver_vendas">Visualizar vendas</a></li>
            <li><a href="/atualizar_dados_cliente">Atualizar dados de um cliente específico</a></li>
            <li><a href="/atualizar_dados_produto">Atualizar dados de um produto específico</a></li>
            <li><a href="/sair">Sair</a></li>
        </ul>
    '''

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'GET':
        return '''
            <h2>Cadastrar cliente</h2>
            <form method="post">
                Endereço: <input type="text" name="endereco"><br>
                E-mail: <input type="email" name="email"><br>
                Telefone: <input type="text" name="telefone"><br>
                Tipo de cliente: 
                <select name="tipo_cliente">
                    <option value="PF">Pessoa Física</option>
                    <option value="PJ">Pessoa Jurídica</option>
                </select><br>
                <input type="submit" value="Cadastrar">
            </form>
        '''
    else:
        endereco = request.form['endereco']
        email = request.form['email']
        telefone = request.form['telefone']
        tipo_cliente = request.form['tipo_cliente']
        if tipo_cliente == 'PF':
            return '''
                <h2>Cadastrar cliente - Pessoa Física</h2>
                <form method="post" action="/cadastrar_cliente_pf">
                <input type="hidden" name="endereco" value="{}">
                <input type="hidden" name="email" value="{}">
                <input type="hidden" name="telefone" value="{}">
                Nome: <input type="text" name="nome"><br>
                CPF: <input type="text" name="cpf"><br>
                Número de celular: <input type="text" name="numero_celular"><br>
                <input type="submit" value="Cadastrar">
                </form>
        '''.format(endereco, email, telefone)
        elif tipo_cliente == 'PJ':
            return '''
            <h2>Cadastrar cliente - Pessoa Jurídica</h2>
            <form method="post" action="/cadastrar_cliente_pj">
            <input type="hidden" name="endereco" value="{}">
            <input type="hidden" name="email" value="{}">
            <input type="hidden" name="telefone" value="{}">
            CNPJ: <input type="text" name="cnpj"><br>
            Razão social: <input type="text" name="razao_social"><br>
            Site: <input type="text" name="site"><br>
            <input type="submit" value="Cadastrar">
            </form>
        '''.format(endereco, email, telefone)
@app.route('/cadastrar_cliente_pf', methods=['POST'])
def cadastrar_cliente_pf():
    endereco = request.form['endereco']
    email = request.form['email']
    telefone = request.form['telefone']
    nome = request.form['nome']
    cpf = request.form['cpf']
    numero_celular = request.form['numero_celular']
    cliente = PessoaFisica(endereco, email, telefone, nome, cpf, numero_celular)
    clientes.append(cliente)
    return '''
    <p>Cliente cadastrado com sucesso:</p>
    <ul>
    <li>Endereço: {}</li>
    <li>E-mail: {}</li>
    <li>Telefone: {}</li>
    <li>Nome: {}</li>
    <li>CPF: {}</li>
    <li>Número de celular: {}</li>
    </ul>
    '''.format(cliente.endereco, cliente.email, cliente.telefone, cliente.nome, cliente.cpf, cliente.numero_celular)

@app.route('/cadastrar_cliente_pj', methods=['POST'])
def cadastrar_cliente_pj():
    endereco = request.form['endereco']
    email = request.form['email']
    telefone = request.form['telefone']
    cnpj = request.form['cnpj']
    razao_social = request.form['razao_social']
    site = request.form['site']
    cliente = PessoaJuridica(endereco, email, telefone, cnpj, razao_social, site)
    clientes.append(cliente)
    return '''
    <p>Cliente cadastrado com sucesso:</p>
    <ul>
    <li>Endereço: {}</li>
    <li>E-mail: {}</li>
    <li>Telefone: {}</li>
    <li>CNPJ: {}</li>
    <li>Razão social: {}</li>
    <li>Site: {}</li>
    </ul>
    '''.format(cliente.endereco, cliente.email, cliente.telefone, cliente.cnpj, cliente.razao_social, cliente.site)
    
@app.route('/ver_dados_cliente', methods=['GET', 'POST'])
def ver_dados_cliente():
    if request.method == 'GET':
        return '''
        <h2>Ver dados de um cliente específico</h2>
        <form method="post">
        Informe o CPF (Pessoa Física) ou CNPJ (Pessoa Jurídica): <input type="text" name="documento"><br>
        <input type="submit" value="Buscar">
        </form>
        '''
    else:
        ocumento = request.form['documento']
        cliente_encontrado = None
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == documento:
            cliente_encontrado = cliente
            break
        elif isinstance(cliente, PessoaJuridica) and cliente.cnpj == documento:
            cliente_encontrado = cliente
            break
    if cliente_encontrado:
        if isinstance(cliente_encontrado, PessoaFisica):
            return '''
            <h2>Dados do cliente - Pessoa Física</h2>
            <ul>
                <li>Endereço: {}</li>
                <li>E-mail: {}</li>
                <li>Telefone: {}</li>
                <li>Nome: {}</li>
                <li>CPF: {}</li>
                <li>Número de celular: {}</li>
            </ul>
            '''.format(cliente_encontrado.endereco, cliente_encontrado.email, cliente_encontrado.telefone, cliente_encontrado.nome, cliente_encontrado.cpf, cliente_encontrado.numero_celular)
        else:
            return '''
            <h2>Dados do cliente - Pessoa Jurídica</h2>
            <ul>
                <li>Endereço: {}</li>
                <li>E-mail: {}</li>
                <li>Telefone: {}</li>
                <li>CNPJ: {}</li>
                <li>Razão social: {}</li>
                <li>Site: {}</li>
            </ul>
            '''.format(cliente_encontrado.endereco, cliente_encontrado.email, cliente_encontrado.telefone, cliente_encontrado.cnpj, cliente_encontrado.razao_social, cliente_encontrado.site)
    else:
        return '<p>Cliente não encontrado.</p>'
@app.route('/ver_todos_clientes', methods=['GET'])
def ver_todos_clientes():
    output = '<h2>Clientes cadastrados:</h2>'
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica):
            output += '''
            <h3>Pessoa Física</h3>
            <ul>
            <li>Endereço: {}</li>
            <li>E-mail: {}</li>
            <li>Telefone: {}</li>
            <li>Nome: {}</li>
            <li>CPF: {}</li>
            <li>Número de celular: {}</li>
            </ul>
            '''.format(cliente.endereco, cliente.email, cliente.telefone, cliente.nome, cliente.cpf, cliente.numero_celular)
        else:
            output += '''
            <h3>Pessoa Jurídica</h3>
            <ul>
            <li>Endereço: {}</li>
            <li>E-mail: {}</li>
            <li>Telefone: {}</li>
            <li>CNPJ: {}</li>
            <li>Razão social: {}</li>
            <li>Site: {}</li>
            </ul>
                    '''.format(cliente.endereco, cliente.email, cliente.telefone, cliente.cnpj, cliente.razao_social, cliente.site)
    return output

@app.route('/cadastrar_produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'GET':
        return '''
        <h2>Cadastrar produto</h2>
        <form method="post">
        ID: <input type="text" name="id"><br>
        Nome: <input type="text" name="nome"><br>
        Preço: <input type="text" name="preco"><br>
        Descrição: <textarea name="descricao"></textarea><br>
        <input type="submit" value="Cadastrar">
        </form>
        '''
    else:
        id = request.form['id']
        nome = request.form['nome']
        preco = float(request.form['preco'])
        descricao = request.form['descricao']
        produto = Produto(id, nome, preco, descricao)
        produtos.append(produto)
        return '''
        <p>Produto cadastrado com sucesso:</p>
        <ul>
        <li>ID: {}</li>
        <li>Nome: {}</li>
        <li>Preço: {}</li>
        <li>Descrição: {}</li>
        </ul>
        '''.format(produto.id, produto.nome, produto.preco, produto.descricao)

@app.route('/ver_dados_produto', methods=['GET', 'POST'])
def ver_dados_produto():
    if request.method == 'GET':
        return '''
        <h2>Ver dados de um produto específico</h2>
        <form method="post">
        ID do produto: <input type="text" name="id"><br>
        <input type="submit" value="Buscar">
        </form>
        '''
    else:
        id = request.form['id']
        produto_encontrado = None
        for produto in produtos:
            if produto.id == id:
                produto_encontrado = produto
                break
            if produto_encontrado:
                return '''
                <h2>Dados do produto</h2>
                <ul>
                    <li>ID: {}</li>
                    <li>Nome: {}</li>
                    <li>Preço: {}</li>
                    <li>Descrição: {}</li>
                </ul>
                '''.format(produto_encontrado.id, produto_encontrado.nome, produto_encontrado.preco, produto_encontrado.descricao)
            else:
                return '<p>Produto não encontrado.</p>'
@app.route('/ver_todos_produtos', methods=['GET'])
def ver_todos_produtos():
    output = '<h2>Produtos cadastrados:</h2>'
    for produto in produtos:
        output += '''
        <ul>
        <li>ID: {}</li>
        <li>Nome: {}</li>
        <li>Preço: {}</li>
        <li>Descrição: {}</li>
        </ul>
        '''.format(produto.id, produto.nome, produto.preco, produto.descricao)
    return output

if __name__ == '__main__':
    app.run(debug=True)