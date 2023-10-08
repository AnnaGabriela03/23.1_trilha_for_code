# EXERCICIO A => refazendo o jogo do pedra papel e tesoura com função
import random

def escolha_do_jogador():
    escolha = input("\nPedra, papel ou tesoura? ").lower()
    while escolha not in ["pedra", "papel", "tesoura"]:
        escolha = input("Escolha inválida. \nPedra, papel ou tesoura? ").lower()
    return escolha

def escolha_do_computador():
    escolhas_possiveis = ["pedra", "papel", "tesoura"]
    return random.choice(escolhas_possiveis)

def determinar_vencedor(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        return "Empate"
    elif (
        (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
        (escolha_jogador == "papel" and escolha_computador == "pedra") or
        (escolha_jogador == "tesoura" and escolha_computador == "papel")
    ):
        return "Jogador vence"
    else:
        return "Computador vence"

def rodada():
    jogador = escolha_do_jogador()
    computador = escolha_do_computador()
    print(f"Jogador escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")
    resultado = determinar_vencedor(jogador, computador)
    print(resultado)
    return resultado

def jogar():
    jogador_pontos = 0
    computador_pontos = 0

    while jogador_pontos < 3 and computador_pontos < 3:
        resultado = rodada()
        if resultado == "Jogador vence":
            jogador_pontos += 1
        elif resultado == "Computador vence":
            computador_pontos += 1

        print(f"Jogador: {jogador_pontos}, Computador: {computador_pontos}")

    if jogador_pontos > computador_pontos:
        print("Você venceu!")
    else:
        print("Game Over!💀")

if __name__ == "__main__":
    jogar()
