#notas = [7.5, 8.0, 6.5, 9.0, 5.5]
#Faça um programa que:
#Mostre todas as notas.
#Mostre a primeira nota.
#Mostre a última nota.
#Adicione uma nova nota 8.5.
#Altere a nota 5.5 para 6.0.
#Remova a nota 7.5.
#Mostre quantas notas existem agora.
#Mostre a lista final.

notas = [7.5, 8.0, 6.5, 9.0, 5.5]

for i, nota in enumerate(notas):
    print(f"{i+1}° Nota: {nota}")

print("A primeira nota é", notas[0])
print("A primeira nota é", notas[-1])
notas.append(8.5)
notas[4] = 6.0
print(f"O total de notas cadastradas é: {len(notas)}")
print(notas)
