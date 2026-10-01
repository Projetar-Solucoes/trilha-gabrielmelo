def mostrar_jogador(dic):
    print("=== JOGADOR ===")
    for key, value in dic.items():
        print(f"{key.capitalize()}: {value}")


def aumentar_pontos(jogador, pontos):
    jogador["pontos"] += pontos

    print("Pontos:", jogador["pontos"])


def verificar_nivel(jogador):
    if jogador["pontos"] >= 100 and jogador["pontos"] < 200:
        jogador["nivel"] = 4

    elif jogador["pontos"] >= 200:
        jogador["nivel"] = 5

    mostrar_jogador(jogador)



jogador = {
    "nome": "Cococi",
    "pontos": 80,
    "nivel": 3,
    "vidas": 2
}

mostrar_jogador(jogador)
aumentar_pontos(jogador, 50)
verificar_nivel(jogador)
