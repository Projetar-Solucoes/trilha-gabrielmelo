from datetime import date
ano = date.today().year

cont = 0
quantidade_categoria_p_urgente = 0
quantidade_categoria_m_urgente = 0
quantidade_categoria_muito_urgente = 0
categoria_text = ''

def exibir_setores():
    print("\n")
    print("selecione o setor que você deseja")
    print("="*50)
    print("| Digite 1 para - Criação de Sites               |")
    print("| Digite 2 para - Design e Identidade Visual     |")
    print("| Digite 3 para - Reparo de Computadores         |")
    print("| Digite 4 para - Desenvolvimento de Aplicativos |")
    print("="*50)
def exibir_categorias():
    print("\n")
    print("selecione a categoria que você deseja")
    print("="*50)
    print("| Digite 1 para - Pouco Urgente                  |")
    print("| Digite 2 para - Urgente                        |")
    print("| Digite 3 para - Muito Urgente                  |")
    print("="*50)
def exibir_estatisticas():
    print("\n")
    print("selecione a estastisca que você deseja")
    print("="*50)
    print("| Digite 1 para - Exibir a quantidade de solicitações |")
    print("| Digite 2 para - Exibir quantidade por prioridade    |")
    print("| Digite 3 para - Exibir outras contagens             |")
    print("| Digite 4 para - Sair                                |")
    print("="*50)
def exibir_quantidade_categoria():
    print("\n")
    print("selecione a estastisca que você deseja")
    print("="*55)
    print("| Digite 1 para - Exibir pouco Urgente                |")
    print("| Digite 2 para - Exibir Urgente                      |")
    print("| Digite 3 para - Exibir muito Urgente                |")
    print("="*55)
def testar_vazio( frase ):
    name = input(frase).strip().title()
    while name == "":
        name = input("Campo inválido digite novamente: ").strip().title()

    return name 

cont += 1
print("="*30)
print("BEM-VINDO A BACK BITE")
print("="*30)

nome = testar_vazio("Digite seu nome: ")

exibir_setores()
setor = input()
    
while setor != "1" and setor != "2" and setor != "3" and setor != "4":
    print ("setor invalido tente novamente") 
    exibir_setores()
    setor = (input())

match(setor):
    case "1": 
        setor_text = "Criação de Sites"
    case "2":
        setor_text = "Design e Identidade Visual"
    case "3":
        setor_text = "Reparo de Computadores"
    case "4":
        setor_text = "Desenvolvimento de Aplicativos"

exibir_categorias()
categoria = input().strip()

while categoria != "1" and categoria != "2" and categoria != "3":
    print ("categoria inválida tente novamente") 
    exibir_categorias()
    categoria = input().strip()

match(categoria):
    case "1": 
        categoria_text = "Pouco Urgente"
        quantidade_categoria_p_urgente += 1
    case "2":
        categoria_text = "Urgente"
        quantidade_categoria_m_urgente += 1
    case "3":
        categoria_text = "Muito Urgente"
        quantidade_categoria_muito_urgente += 1

print("\n")
assunto = testar_vazio("Digite o assunto de forma sucinta: ")

print("\n")
descricao = testar_vazio("Escreva a descrição do problema: ")

setor_text = ''
iniciais = "".join(c[0] for c in nome.upper().split() )
protocolo = f"{ano}-{cont:0>4}-{iniciais}"

print("\n")
print("-=" * 20)
print (protocolo)
print (f"Nome: {nome}")
print (f"Categoria: {categoria_text}")
print (f"Assunto: {assunto}")
print (f"Descrição: {descricao}")
print("-=" * 20)

while True:
    exibir_estatisticas()
    opcao_estatistica = input("")

    while opcao_estatistica.strip() != "1" and opcao_estatistica.strip() != "2" and opcao_estatistica.strip() != "3" and opcao_estatistica.strip() != "4":

        print("Opção inválida digite novamente:")
        exibir_estatisticas()
        opcao_estatistica = input()

    if opcao_estatistica == "1":
        print(f"Quantidade de Solicitações {cont}")

    elif opcao_estatistica == "2":

        exibir_quantidade_categoria()
        categoria_ver_total = input("Digite a categoria que vc quer ver a quantidade: ")

        while categoria_ver_total != "1" and categoria_ver_total != "2" and categoria_ver_total != "3":
            print("Categoria invalida")

            exibir_quantidade_categoria()
            categoria_ver_total = input("\nDigite a categoria que você quer ver a quantidade: ")

        match categoria_ver_total: 
            case "1":
                print(f"\nNúmero de solicitações pouco urgente - {quantidade_categoria_p_urgente}")

            case "2":
                print(f"\nNúmero de solicitações urgente - {quantidade_categoria_m_urgente}")

            case "3":
                print(f"\nNúmero de solicitações muito urgente - {quantidade_categoria_muito_urgente}")

    elif opcao_estatistica == "3":
        print("Em desenvolvimento...")

    else:
        break
