# def escopo1():
#     a = 10

# escopo1()

# print(a)

# recursividade
# def fatorial(numero):
#     fat = 1
#     while numero > 1:
#         fat += numero
#         numero -= 1
#     return fat

# def fatorial1(numero):
#     if numero == 0 or numero == 1:
#         return 1
#     else:
#         return numero * fatorial1(numero - 1)

# print(fatorial(5))

# def somar1(x,y):
#     return x + y

# aumento = lambda a, b: (a*b / 100)

# print(aumento(a:100, b: 5))

# exeções

def recebe_pin():
    senha = input("digite seu pin >> ")
    try:
        senha = int(senha)
    except:
        print("senha inválida, tente digitar um número")
        senha = input("digite seu pin >> ")

    print(senha)

recebe_pin()

# list comprehensions
numeros_pares_20 = []
for i in range(11):
    numeros_pares_20.append(i*2)
print(numeros_pares_20)

pares_ate_40 = [i*2 for i in range(21)]
print(pares_ate_40)
