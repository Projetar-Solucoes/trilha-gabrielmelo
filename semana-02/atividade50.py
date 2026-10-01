cont, soma  = 0 , 0
for i in range (1, 7):
    num = int(input(f"Digite {i}° valor: "))

    if num % 2 == 0:
        soma += num
        cont += 1
print("\n")
print("=" * 50)
print(f"Você informou {cont} números pares \nE soma deles é: {soma}")
print("=" * 50)
