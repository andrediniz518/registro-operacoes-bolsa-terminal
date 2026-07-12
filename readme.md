# Registro de Operações na Bolsa

Projeto desenvolvido em **Python** integrado ao **MySQL** para registrar operações de compra e venda de ações.

O objetivo do projeto é praticar a integração entre Python e banco de dados, aplicando as operações de **CRUD (Create, Read, Update e Delete)**.

## Funcionalidades

* Registrar operações de compra de ações
* Registrar operações de venda de ações
* Consultar histórico de operações
* Pesquisar operações por ticker
* Alterar operações cadastradas
* Excluir operações
* Menu interativo no terminal

## Tecnologias Utilizadas

* Python 3
* MySQL
* mysql-connector-python
* Git
* GitHub

## Estrutura do Projeto

```text
projeto/
│
├── main.py
├── conexao.py
├── operacoes.py
└── README.md
```

## Banco de Dados

O sistema utiliza uma tabela chamada **operacoes** com os seguintes campos:

| Campo         | Tipo                                      |
| ------------- |-------------------------------------------|
| id            | INT AUTO_INCREMENT <br/> PRIMARY KEY<br/> |
| ticker        | VARCHAR(10)                               |
| tipo          | VARCHAR(10)                               |
| quantidade    | INT                                       |
| preco         | DECIMAL(10,2)                             |
| data_operacao | DATE                                      |

## Como Executar

1. Clone este repositório.
2. Instale a biblioteca de conexão com o MySQL:

```bash
pip install mysql-connector-python
```

3. Crie um banco de dados no MySQL.
4. Crie a tabela **operacoes**.
5. Configure as credenciais de acesso no arquivo `conexao.py`.
6. Execute o programa:

```bash
python main.py
```

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

* Integração entre Python e MySQL
* Conexão com banco de dados
* Execução de comandos SQL através do Python
* Operações de CRUD (Create, Read, Update e Delete)
* Organização modular do código
* Manipulação de banco de dados relacional
* Persistência de dados

## Autor

André Diniz
