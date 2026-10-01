from datetime import date
ano = date.today().year
from functions.exibir_menus import *
from functions.verificar_entrada_dados import *
from functions.json_functions import *
from functions.cadastrar_solicitacao import *

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
        print(f"Quantidade de Solicitações {cont}")
        continue

    elif opcao_estatistica == 3:
        
        categoria_ver_total = verificar_opcoes(exibir_quantidade_categoria, 1,2,3)

        match categoria_ver_total: 
            case 1:
                print(f"\nNúmero de solicitações pouco urgente - {quantidade_categoria_p_urgente}")

            case 2:
                print(f"\nNúmero de solicitações urgente - {quantidade_categoria_m_urgente}")

            case 3:
                print(f"\nNúmero de solicitações muito urgente - {quantidade_categoria_muito_urgente}")

        continue

    elif opcao_estatistica == 4:
        listar_solicitacoes_format("solicitacoes.json")
        
        continue

    else:
        break

    