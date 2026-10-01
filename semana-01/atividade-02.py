nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
area = input("Digite a área em que você atua: ")
experiencia = input("Digite sua experiência prévia: ")


print("\n" + "="*50)
print(f"Nome:        {nome:=<20} tipo: {type(nome)}")
print(f"Idade:       {idade:<20} tipo: {type(idade)}")
print(f"Altura:      {altura:<20} tipo: {type(altura)}")
print(f"Area:        {area:<20} tipo: {type(area)}")
print(f"Experiência: {experiencia:<20} tipo: {type(experiencia)}")
print("="*50)
