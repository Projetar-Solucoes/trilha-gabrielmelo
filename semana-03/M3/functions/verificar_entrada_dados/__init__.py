def verificar_opcoes(function, *opcoes):
    while True:
        try:
            function()
            opc = int(input())

        except (TypeError, ValueError):
            print("Digite apenas números")
            continue
        else:
            if (opc not in opcoes):
                print("Opção inválida tente novamente...")
                continue
            else:
                break

    return opc

def testar_vazio( frase ):
    name = input(frase).strip().title()
    while name == "":
        name = input("Campo inválido digite novamente: ").strip().title()

    return name 