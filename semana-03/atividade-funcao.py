def mostrar_personagem(dic):
    print("=== PERSONAGEM ===")
    for key, value in dic.items():
        print(f"{key.capitalize()}: {value}")


def aumentar_nivel(dic):
    print("Nível antes: ", dic["nivel"])
    dic["nivel"] += 1
    print("Nível depois: ", dic["nivel"])

personagem = {
    "nome": "Cococi",
    "classe": "Mago",
    "nivel": 10,
    "vida": 100
} 

mostrar_personagem(personagem)
aumentar_nivel(personagem)