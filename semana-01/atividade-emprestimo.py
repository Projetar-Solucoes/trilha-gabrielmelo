def verificar_emprestimo(prestacao, renda): #Função para verificar se o empréstimo é possível
    if prestacao > (renda * 0.3):
        return False
    else:
        return True
    
#Coletando informações do usuário
nome = input('Digite seu nome: ') 
idade = int(input('Digite sua idade: '))
cpf = int(input('Digite seu CPF: '))
renda = float(input('Digite sua renda: '))

#validação das informações do usuário
if not nome.split():
    print('Nome inválido!')

elif idade < 18:
    print('Idade inválida!')

elif len(str(cpf)) != 11:
    print('CPF inválido!')
    
else:

    #Coletando informações do empréstimo
    emprestimo = float(input('Digite o valor do empréstimo desejado: '))
    ano = int(input('Em quantos anos você deseja pagar o empréstimo: '))
    prestacao = emprestimo / (ano * 12)

    #Verificando se o empréstimo é possível
    if (renda < 1500 or renda > 50000) or (not verificar_emprestimo(prestacao, renda)):
        print('Não é possível realizar o empréstimo.')
        print('Empréstimo bloqueado!')

    #Verificando se o empréstimo está em revisão humana
    elif ((renda == 1500) or (renda >= 20001 and renda <= 50000)):
        print('Empréstimo em revisão humana!')      

    #Verificando se o empréstimo é aprovado para liberação automática
    else: 
        print('Empréstimo aprovado para liberação automática!')

