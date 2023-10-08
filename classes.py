# classes => reune objetos de mesmos atributos. Cada objeto tem atributos e metodos (metodo é aql parada de .algumacoisa )
# orientação a objeto => maneira de pensar em python que vc abstrai a função das coisas e interpreta como um objeto, de modo a manipulados de melhir forma.
# por exemplo, se eu tenho uma class carro, eu posso colocar varios objetos dessa mesma classe dentro desse escopo.

# __init__ inicializa a classe
# self.algumacoisa atributos
# def ação(chama a classe) => dai aq dentro c pode colocar um metodo, uma ação pra ele fazer, é uma função que representa um metodo
# self. vc cria atributos. basicamente

class Carro:

    def __init__(self, marca, cavalos, ligado):
        self.marca = marca
        self.cavalos = cavalos
        self.ligado = ligado
        self.quilometragem = 10
    
    def chama_marca(self):
        print(self.marca)

ferrari = Carro(marca: "Ferrari", cavalos: 480, ligado: True)

ferrari.chama_marca()