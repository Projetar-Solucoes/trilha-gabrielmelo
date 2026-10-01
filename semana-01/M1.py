#nome, setor, categoria, assunto e descrição

print("="*30)
print("BEM-VINDO A BACK BITE")
print("="*30)

print('\n')
nome = input("Digite seu nome: ")
print('\n')

def exibir_setores():
    print("selecione o setor que você deseja")
    print("="*50)
    print("| Digite 1 para - Criação de Sites               |")
    print("| Digite 2 para - Design e Identidade Visual     |")
    print("| Digite 3 para - Reparo de Computadores         |")
    print("| Digite 4 para - Desenvolvimento de Aplicativos |")
    print("="*50)

def exibir_categorias():
    print("selecione a categoria que você deseja")
    print("="*50)
    print("| Digite 1 para - Pouco Urgente                  |")
    print("| Digite 2 para - Urgente                        |")
    print("| Digite 3 para - Muito Urgente                  |")
    print("="*50)

exibir_setores()
setor = int(input())

while setor not in [1,2,3,4]:
    print ("setor invalido tente novamente") 
    exibir_setores()
    setor = int(input())

exibir_categorias()
categoria = int(input())

while categoria not in [1,2,3]:
    print ("categoria invalida tente novamente") 
    exibir_categorias()
    categoria = int(input())

assunto = input("Escreva o assunto da contatação de forma sucinta: ")
descricao = input("Escreva a descrição do problema: ") 

setor_text = ''
categoria_text = ''

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
    case 2:
        categoria_text = "Urgente"
    case 3:
        categoria_text = "Muito Urgente"

print("\n")
print(f'Olá {nome} recebemos sua solicitação ao setor {setor_text} com a categoria {categoria_text} cujo assunto é {assunto} e seu problema {descricao} retornaremos em brave com a resposta')

input("Preciona enter para finalizar...")
