from functions.json_functions import get_json

def exibir_estastisticas(arquivo):
    lista = get_json(arquivo)
    quant_pouco_urg = 0
    quant_urg = 0
    quant_muito_urg = 0

    quant_criacao_site = 0
    quant_design = 0
    quant_reparo = 0
    quant_desv_app = 0

    for itens in lista[1:]:
        if itens["categoria"] == "Pouco Urgente":
            quant_pouco_urg += 1
        elif itens["categoria"] == "Urgente":
            quant_urg += 1
        else:
            quant_muito_urg += 1

        if itens["setor"] == "Criação de Sites":
            quant_criacao_site += 1
        elif itens["setor"] == "Design e Identidade Visual":
            quant_design += 1
        elif itens["setor"] == "Reparo de Computadores":
            quant_reparo += 1
        else:
           quant_desv_app += 1

    print(f"""
=== ESTATÍSTICAS === 

Total de solicitações: {lista[0]['solicitacoes_quant']}

Por prioridade:
Pouco Urgente: {quant_pouco_urg}
Urgente: {quant_urg}
Muito Urgente: {quant_muito_urg}

Por categoria:
Criação de Sites: {quant_criacao_site}
Design e Identidade Visual: {quant_design}
Reparo de Computadores: {quant_reparo}
Desenvolvimento de Aplicativos: {quant_desv_app}

""")    
        
     