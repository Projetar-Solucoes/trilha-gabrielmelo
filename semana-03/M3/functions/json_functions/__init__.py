from os import path
import json

def salvar_json(nome_arquivo, dic):

    if path.exists(nome_arquivo) and path.getsize(nome_arquivo) > 0:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados_atuais = json.load(arquivo)

    else:
        dados_atuais = []
        
    dados_atuais.append(dic)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados_atuais, arquivo, indent=4, ensure_ascii=False)


def listar_solicitacoes(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    print(dados)

def listar_solicitacoes_format(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    for dado in dados:
        print("-=" * 50)
        for key, item in dado.items():
            print(f"{key} - {item}")
        print("-=" * 50)


def get_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    
    return dados

def atualizar_quantidade(nome_arquivo):
    solicitacoes = get_json(nome_arquivo)
    solicitacoes[0]["solicitacoes_quant"] += 1

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(solicitacoes, arquivo, indent=4, ensure_ascii=False) 