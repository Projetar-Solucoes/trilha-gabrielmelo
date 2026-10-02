from functions.json_functions import get_json

def contar_categoria(arquivo):
    lista = get_json(arquivo)
    quant_pouco_urg = 0
    quant_urg = 0
    quant_muito_urg = 0
    for itens in lista[1:]:
        if itens["categoria"] == "Pouco Urgente":
            quant_pouco_urg += 1
        elif itens["categoria"] == "Urgente":
            quant_urg += 1
        else:
            quant_muito_urg += 1

    print(f"""
Quantidade de Pouco Urgente: {quant_pouco_urg}
Quantidade de Urgente: {quant_urg}
Quantidade de Muito Urgente: {quant_muito_urg}
""")    
        
     