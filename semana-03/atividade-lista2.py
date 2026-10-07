#personagem = ("Cococi", "Mago", 15, 100, 80)
#A tupla representa:
#(nome, classe, nível, vida, mana)

#Faça um programa que:
#Mostre o nome.
#Mostre a classe.
#Mostre o nível.
#Mostre a vida.
#Mostre a mana.
#Mostre quantas informações existem na tupla.
#Mostre todas as informações usando for.

personagem = ("Cococi", "Mago", 15, 100, 80)
print('-' * 20)
print(f"Nome: {personagem[0]}")
print(f"Classe: {personagem[1]}")
print(f"Nível: {personagem[2]}")
print(f"Vida: {personagem[3]}")
print(f"Mana: {personagem[4]}")
print('-' * 20)

print('=' * 20)
print(f"O total de informações apresentadas é: {len(personagem)}")
print('=' * 20)

for i in personagem:
    print(f"{i}")

print("sla")

