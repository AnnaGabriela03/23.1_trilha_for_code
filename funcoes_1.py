#  aulinha goxtosa de funções adoroooh
# def subtracao(y= 10, x = 10):
#     variavel_subtracao = x - y
#     return variavel_subtracao


# def ehpar(numero):
#    return numero % 2 == 0

# print(ehpar(10))
# print(subtracao())

# funções 2
import os
import time

def inicializa_valores():
    segundo = 0
    minuto = 0
    hora = 0
    return segundo, minuto, hora


def checa_virada_unidade(segundo, minuto, hora):
    if segundo == 60:
        if minuto == 59:
            minuto = 0
            segundo = 0
            hora += 1
        else:
            segundo = 0
            minuto += 1

    return segundo, minuto, hora

def printa(segundo, minuto, hora):
    if segundo < 10:
        segundo = f'0{segundo}'
    if minuto < 10:
        minuto = f'0{minuto}'
    if hora < 10:
        hora = f'0{hora}'
    print(f'{hora}:{minuto}:{segundo}')


def main():
    segundo, minuto, hora = inicializa_valores()

    while True:
        os.system('cls')

        segundo, minuto, hora = checa_virada_unidade(segundo, minuto, hora)
        printa(segundo, minuto, hora)

        time.sleep(1)
        segundo += 1

main()