num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
while True:
    print('''[1] somar
[2] multiplicar 
[3] maior
[4] novos números
[5] sair
    ''')
    opcao = int(input(">>>>>Qual é a sua opção: "))

    if opcao == 1:
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é igual a {soma}")
    elif opcao == 2:
        mult = num1 * num2
        print(f" A multiplicação de {num1} com {num2} é igual a {mult}")
    elif opcao == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        else:
            print(f"{num2} é maior que {num1}")
    elif opcao == 4:
        num1 = int(input("Digite um novo número para primeiro valor: "))
        num2 = int(input("Digite um novo número para o segundo valor: "))

    elif opcao == 5:
        print("Fim do programa!!!")
        break

    else: 
        print("opção invalida")