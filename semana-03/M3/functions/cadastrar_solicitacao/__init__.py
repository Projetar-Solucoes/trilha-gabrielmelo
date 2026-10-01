from datetime import date
from functions.exibir_menus import *
from functions.verificar_entrada_dados import *
from functions.json_functions import *

def cadastrar_solicitacao():
    ano = date.today().year
    lista = get_json("solicitacoes.json")
    cont = len(lista) + 1
    nome = testar_vazio("Digite seu nome: ")
    quantidade_categoria_p_urgente = 0
    quantidade_categoria_m_urgente = 0
    quantidade_categoria_muito_urgente = 0
    setor = verificar_opcoes(exibir_setores, 1,2,3,4)
    categoria = verificar_opcoes(exibir_categorias, 1,2,3)
    assunto = testar_vazio("Digite o assunto de forma sucinta: ")
    descricao = testar_vazio("Escreva a descrição do problema: ")

    match(setor):
        case 1: 
            setor_text = "Criação de Sites"
        case 2:
            setor_text = "Design e Identidade Visual"
        case 3:
            setor_text = "Reparo de Computadores"
        case 4:
            setor_text = "Desenvolvimento de Aplicativos"

    match(categoria):
        case 1: 
            categoria_text = "Pouco Urgente"
            quantidade_categoria_p_urgente += 1
        case 2:
            categoria_text = "Urgente"
            quantidade_categoria_m_urgente += 1
        case 3:
            categoria_text = "Muito Urgente"
            quantidade_categoria_muito_urgente += 1


    iniciais = "".join(c[0] for c in nome.upper().split() )
    protocolo = f"{ano}-{cont:0>4}-{iniciais}"

    dados = {
        "protocolo": protocolo,
        "nome" : nome,
        "setor": setor_text,
        "categoria": categoria_text,
        "assunto": assunto,
        "descrição": descricao
    }

    salvar_json("solicitacoes.json", dados)