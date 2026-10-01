def is_negative(value):
    while (value < 0):
        print("=" * 50)
        print("Não é aceito valores negativos tente novamente")
        print("=" * 50)
        value = float(input("Digite o valor correto: "))
    return value

preco_produto = float(input("Digite o preço do produto: "))
preco_produto = is_negative(preco_produto)

quantidade_produto = int(input("Digite a quantidade do produto: "))
quantidade_produto = int(is_negative(quantidade_produto))

porcentagem_desconto = float(input("Digite a porcentagem do desconto: ")) / 100
porcentagem_desconto = is_negative(porcentagem_desconto) / 100
print(porcentagem_desconto)

sub_total = preco_produto * quantidade_produto
desconto_final = sub_total * porcentagem_desconto
total = sub_total - desconto_final

print("-" * 30)

if (total >= 0):
    print(f"Valor do subtotal {sub_total}")
    print(f"Valor do desconto {desconto_final:.2f}")
    print(f"Valor do final da compra {total:.2f}")

else:
    print("Não foi possível realizar a operação com descontos maiores que 100%")

print("-" * 30)
input("Aperte enter para finalizar o programa ...")
