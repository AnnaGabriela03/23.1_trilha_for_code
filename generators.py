# lista = [1,2,3,4]

# def function(x):
#     return x**2

# for i in lista:
#     print(function(i))

# def generator(lista):
#     for i in lista:
#         yield i**2
# #  tem que ser definido em uma função antes
# g = generator (lista)
# for i in range(4):
#     print(next(g))

lista = [1,2,3,4]

def function(x):
    return x**2


for i in lista:
    print(function(i))

def generator(lista):
    for i in lista:
        yield i**2
        
g = generator(lista)
for i in range(4):
    print(next(g))