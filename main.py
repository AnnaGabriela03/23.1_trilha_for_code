import random

numero = random.randint(1, 100)
tentativas = 0

while tentativas < 10:
    chute = int(input("digite um número: "))
    if chute == numero:
        print("voce acertou")
        break
    elif chute < numero:
        print("chute muito pequeno")
    else:
        print("chute muito grande")
    tentativas = tentativas + 1