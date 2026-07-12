from conexao import conectar

def cadastrar_operacao():
    conexao = conectar()
    cursor = conexao.cursor()

    ticker = input('Ticker: ').upper()
    tipo = input('Tipo (Compra/Venda): ').capitalize()
    quantidade = int(input('Quantidade: '))
    preco = input('Preço: ')
    data = input('Data (AAAA-MM-DD): ')

    sql = """
    INSERT INTO operacoes
    (ticker, tipo, quantidade, preco, data_operacao)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (ticker, tipo, quantidade, preco, data)

    cursor.execute(sql, valores)
    conexao.commit()

    print('Operação cadastrada com Sucesso!')

    cursor.close()
    conexao.close()

def consultar_historico():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = 'SELECT * FROM operacoes'

    cursor.execute(sql)
    operacoes = cursor.fetchall()

    if not operacoes:
        print('Nenhuma operação cadastrada.')
    else:
        print('===== HISTÓRICO ======')

        for operacao in operacoes:
            print(f'ID: {operacao[0]}')
            print(f'Ticker: {operacao[1]}')
            print(f'Tipo: {operacao[2]}')
            print(f'Quantidade: {operacao[3]}')
            print(f'Preço: {operacao[4]}')
            print(f'Data: {operacao[5]}')
            print('--'*10)

    cursor.close()
    conexao.close()

def pesquisar_ticker():
    conexao = conectar()
    cursor = conexao.cursor()

    ticker = input('Digite o ticker: ').upper().strip()

    sql = """
    SELECT * FROM operacoes
    where ticker = %s
    """

    cursor.execute(sql, (ticker,))
    operacao = cursor.fetchall()

    if not operacao:
        print('Nenhuma operação cadastrada.')
    else:
        print(f'===== Detalhes da Ação {ticker} =====')
        info = ['ID:', 'Ticker:', 'Tipo:', 'Quantidade:', 'Preço:', 'Data:']
        for item in operacao:
            for pos, i in enumerate(item):
                print(info[pos], i)
            print('--'*10)

    cursor.close()
    conexao.close()

def excluir_operacao():
    conexao = conectar()
    cursor = conexao.cursor()

    id = int(input('Digite o ID: '))
    confirma = str(input('Tem certeza? [S/N]: ')).upper().strip()
    if confirma == 'S':
        sql = """
            delete from operacoes
            where id = %s
        """

        cursor.execute(sql, (id,))
        conexao.commit()

        if cursor.rowcount > 0:
            print('Operação excluída com sucesso!')
        else:
            print('Nenhuma operação encontrada com esse ID.')

        cursor.close()
        conexao.close()

    else:
        print('Voltando ao menu...')

def alterar_operacao():
    conexao = conectar()
    cursor = conexao.cursor()

    consultar_historico()

    id = int(input('Digite o ID da operação: '))

    sql = """
        SELECT * FROM operacoes WHERE id = %s
    """

    cursor.execute(sql, (id,))
    operacao = cursor.fetchone()

    if operacao:
        print(f'TICKER: {operacao}')

        ticker = input('Ticker: ').upper()
        tipo = input('Tipo (Compra/Venda): ').capitalize()
        quantidade = int(input('Quantidade: '))
        preco = input('Preço: ')
        data = input('Data (AAAA-MM-DD): ')

        sql = """
        update operacoes
        set ticker = %s,
            tipo = %s,
            quantidade = %s,
            preco = %s,
            data_operacao = %s
        WHERE id = %s
        """

        cursor.execute(sql, ( ticker,
                              tipo,
                              quantidade,
                              preco,
                              data,
                              id))
        conexao.commit()

        if cursor.rowcount > 0:
            print('Operação alterada com sucesso!')
        else:
            print('Nenhuma operação foi alterada.')

    else:
        print('Operação não encontrada.')


