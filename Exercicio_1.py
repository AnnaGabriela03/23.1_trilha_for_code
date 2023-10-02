# exercicio 
# tá mt ruizinho esse codigo ainda tenho que melhorar
# colocar pra printar so game over ou so vc venceu no final em vez de printar as duas msgs, talvez relacionar com a pontuação, n sei
import random

rodadas = 0
pontos_j = 0
pontos_pc = 0
escolhas = ("pedra", "papel", "tesoura")

while True:
    if pontos_j == 3:
        print("voce venceu o melhor de 3")
        break
    if pontos_pc == 3:
        print("Game Over!")
        break
    computador = random.choice(escolhas)
    você = input("escolha pedra, papel ou tesoura:")

    if você == computador:
        print("empate")
    
    if (você == "pedra" and computador == "papel") or \
        (você == "papel" and computador == "tesoura") or \
        (você == "tesoura" and computador == "pedra"):
        print("você perdeu!")
        rodadas += 1
        pontos_pc += 1
    
    if (você == "pedra" and computador == "tesoura") or \
        (você == "papel" and computador == "pedra") or \
            (você == "tesoura" and computador == "papel"):
        print("você venceu!")
        rodadas += 1
        pontos_j += 1

# exercício b
import math
soma = 0
soma_anterior = 0
for i in range (2, 60000):
    soma += 1/i/math.log(i)**2
    print(soma)