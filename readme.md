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

## DEMONSTRAÇÃO

## TELA INICIAL
<img width="387" height="160" alt="INICIAL-IMG-1" src="https://github.com/user-attachments/assets/dc250764-7f05-4b74-8a74-67aeb8aa7ebd" />

## CADASTRO DE AÇÕES
<img width="305" height="223" alt="CADASTRO-IMG-2" src="https://github.com/user-attachments/assets/a49506c4-055c-4c83-892e-5b84736cc327" />

## LISTAR AÇÕES EXISTENTE
<img width="295" height="363" alt="LISTAR-IMG-3" src="https://github.com/user-attachments/assets/2b25b00e-aa3b-4e21-894e-91a623d4f3d1" />

## PESQUSIAR POR AÇÃO
<img width="325" height="270" alt="PESQUISAR-IMG-4" src="https://github.com/user-attachments/assets/07bf4f10-3e76-4bb9-a830-382c826a615e" />

## EXCLUIR UMA AÇÃO
<img width="349" height="177" alt="EXCLUIR-IMG-5" src="https://github.com/user-attachments/assets/fea757bf-8515-45b2-80a7-455ce1fb596a" />

## ALTERAR UMA AÇÃO
<img width="651" height="385" alt="ALTERAR-IMG-6" src="https://github.com/user-attachments/assets/28de0751-bba9-4861-84a2-6efad440aa7a" />


## Autor

André Diniz
