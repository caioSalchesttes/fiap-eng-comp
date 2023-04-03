
# Sistema de cadastro e vendas
Este código é um exemplo de um sistema de cadastro e vendas construído com a biblioteca Flask do Python. O sistema permite cadastrar clientes e produtos, ver os dados de um cliente ou produto específico, visualizar todos os clientes e produtos cadastrados, efetuar vendas e atualizar dados de um cliente ou produto específico.

Este código utiliza alguns conceitos fundamentais de Programação Orientada a Objetos (POO), que é um paradigma de programação que se baseia na definição de objetos que possuem atributos e métodos. Nesse código, temos diversas classes, tais como Cliente, PessoaFisica, PessoaJuridica e Produto, cada uma com seus próprios atributos e métodos.

Além disso, esse código utiliza o framework Flask, que é uma ferramenta para desenvolvimento de aplicações web em Python. O Flask permite criar rotas (como "/cadastrar_cliente") que podem ser acessadas via HTTP e retornar conteúdos (HTML, JSON, etc.) de acordo com as requisições dos usuários.

Por fim, o uso do Docker neste código é uma forma de facilitar o processo de deployment da aplicação. O Docker é uma plataforma que permite criar, distribuir e executar containers de aplicações de forma isolada, ou seja, sem afetar o ambiente do sistema operacional host. Com o Docker, é possível garantir que a aplicação será executada da mesma forma em diferentes sistemas operacionais e evitar problemas de compatibilidade de dependências. Isso torna o processo de deployment mais fácil e confiável, pois a aplicação pode ser executada em qualquer ambiente que tenha o Docker instalado, independentemente das configurações do sistema operacional host.

## Algumas práticas de engenharia de software aplicadas neste código incluem:
    
1.  Uso de classes e herança: O código usa classes e herança para representar os objetos do domínio, como clientes e produtos. Isso permite encapsular dados e comportamentos relacionados em um único objeto e simplifica a manutenção do código.
    
2.  Uso de rotas e métodos HTTP: As rotas do Flask mapeiam as requisições HTTP para funções específicas que realizam uma determinada tarefa, como cadastrar um cliente ou exibir os dados de um produto. O código usa os métodos HTTP apropriados (GET, POST) para cada uma dessas tarefas.
    
3.  Validação de entrada: O código realiza a validação de entrada em algumas rotas, verificando se os dados fornecidos pelo usuário estão no formato correto e fazendo a conversão de tipos de dados, como no caso do preço do produto.
    
4.  Uso de containers Docker: O código pode ser executado dentro de um container Docker, o que permite que o ambiente de desenvolvimento e produção sejam configurados de maneira padronizada e isolada. Isso facilita a portabilidade do código entre diferentes ambientes e minimiza problemas de dependências e configurações.

### Classes
O código possui quatro classes:

### Cliente
A classe Cliente é a classe base das classes PessoaFisica e PessoaJuridica. Ela possui três atributos: endereco, email e telefone.

### PessoaFisica
A classe PessoaFisica herda da classe Cliente. Além dos atributos da classe Cliente, ela possui os atributos nome, cpf e numero_celular.

### PessoaJuridica
A classe PessoaJuridica herda da classe Cliente. Além dos atributos da classe Cliente, ela possui os atributos cnpj, razao_social e site.

### Produto
A classe Produto possui quatro atributos: id, nome, preco e descricao.

### Rotas
O código possui as seguintes rotas:

### /
A rota principal do sistema. Ela exibe um menu com todas as opções disponíveis no sistema.

### /cadastrar_cliente
A rota para cadastrar um novo cliente. Ela possui um formulário com os campos endereco, email, telefone e tipo_cliente. Dependendo do tipo de cliente escolhido, o formulário é redirecionado para outra rota para completar o cadastro.

### /cadastrar_cliente_pf
A rota para completar o cadastro de uma pessoa física. Ela possui um formulário com os campos nome, cpf e numero_celular. Depois de preenchido, o cliente é adicionado à lista de clientes.

### /cadastrar_cliente_pj
A rota para completar o cadastro de uma pessoa jurídica. Ela possui um formulário com os campos cnpj, razao_social e site. Depois de preenchido, o cliente é adicionado à lista de clientes.

### /ver_dados_cliente
A rota para ver os dados de um cliente específico. Ela possui um formulário com o campo documento (CPF ou CNPJ). Quando o formulário é submetido, o código procura na lista de clientes pelo cliente com o CPF ou CNPJ informado e exibe seus dados.

### /ver_todos_clientes
A rota para visualizar todos os clientes cadastrados. Ela exibe uma lista com todos os clientes cadastrados.

### /cadastrar_produto
A rota para cadastrar um novo produto. Ela possui um formulário com os campos id, nome, preco e descricao. Depois de preenchido, o produto é adicionado à lista de produtos.

### /ver_dados_produto
A rota para ver os dados de um produto específico. Ela possui um formulário com o campo id do produto. Quando o formulário é submetido, o código procura na lista de produtos pelo produto com o ID informado e exibe seus dados.

### /ver_todos_produtos
A rota para visualizar todos os produtos cadastrados. Ela exibe uma lista com todos os produtos cadastrados.
