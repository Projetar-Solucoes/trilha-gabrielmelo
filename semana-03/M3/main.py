from datetime import date
ano = date.today().year
from functions.exibir_menus import *
from functions.verificar_entrada_dados import *
from functions.json_functions import *
from functions.cadastrar_solicitacao import *
from functions.contar_categoria import *

cont = 0

categoria_text = ''
setor_text = ''

print("="*30)
print("BEM-VINDO A BACK BITE")
print("="*30)

while True:

    opcao_estatistica = verificar_opcoes(exibir_estatisticas, 1, 2, 3, 4, 5)
    
    if opcao_estatistica == 1:
        cadastrar_solicitacao()
        atualizar_quantidade("solicitacoes.json")
        

    elif opcao_estatistica == 2:
        listar_solicitacoes_format("solicitacoes.json")
        continue

    elif opcao_estatistica == 3:
        contar_categoria("solicitacoes.json")
        continue

    elif opcao_estatistica == 4:
        listar_solicitacoes_format("solicitacoes.json")
        
        continue

    else:
        break

    