from operacoes import *


opc = ('Cadastrar Operação', 'Consultar Histórico',
       'Pesquisar por Ticker', 'Excluir Operação',
       'Alterar Operação', 'Sair')


while True:
    print('======= Controle de Operações ========')
    for pos, item in enumerate(opc):
        print(f'[{pos+1}] - {item}')
    opcao = int(input('Qual opção: '))
    if opcao == 1:
        cadastrar_operacao()
    elif opcao == 2:
        consultar_historico()
    elif opcao == 3:
        pesquisar_ticker()
    elif opcao == 4:
        excluir_operacao()
    elif opcao == 5:
        alterar_operacao()
    else:
        print('Saindo...')
        break

