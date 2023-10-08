# recursão => fazer um loop sem um loop,vc chama a função dentro da função etc

# Quando se tem uma variavel fora e uma dentro da função,
# geralmente se considera que está dento da função. 
# Para se utilixar essa variavel de fora usa global variavel.

variavel = 0 #gobal

def fatorial(n):
    global variavel
    variavel = 5
    if n == 0 or n == 1:
        return 1
    else:
        return n + fatorial(n - 1)
    
print(fatorial)

funcao = lambda n: n*n**2

#list comprehension

lista = [x**2 for x in range(10)] #o range é inclusive e começa do 0
print(lista)

#pra meio que achar erro humano, parecido com  if else
try:
    int("jwdf")
except:
    print("não foi possível converter")

# generator => função que dfjkfkj tem que ser colocada em uma variavel.
# Além disso, em vez de return, usa se yield.

def gen(n):
    lista = [i for i in range(n)]
    for i in lista:
        yield i


var1 = gen(10)
print(next(var1))