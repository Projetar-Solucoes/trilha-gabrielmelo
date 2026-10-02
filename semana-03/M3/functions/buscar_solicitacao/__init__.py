from functions.json_functions import get_json

def buscar_solicitacao(nome_arquivo):
    dados = get_json(nome_arquivo)
    protocolo = input("Digite o protoloco da solicitação que busca: ")
    for itens in dados[1:]:
        if itens["protocolo"] == protocolo:
            print("-="*50)
            print(f'Protocolo: {itens["protocolo"]}')
            print(f'Nome: {itens["nome"]}')
            print(f'Setor: {itens["setor"]}')
            print(f'Categoria: {itens["categoria"]}')
            print(f'Assunto: {itens["assunto"]}')
            print(f'Descrição: {itens["descrição"]}')
            print("-="*50)
            break
    else:
        print("Solicitação não encontrada")
