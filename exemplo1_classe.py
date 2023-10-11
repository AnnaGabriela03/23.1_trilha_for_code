class carro:
    def __init__(self, cor, ano, preco, modelo):
        self.cor = cor
        self.ano = ano
        self.preco = preco
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def acelerar(self):
        self.velocidade += 10


carro1 = carro('fusca', 'azul', 1980, 5000)
print(carro1.ligado, carro1.velocidade)
carro1.ligar()
carro1.acelerar()
print(carro1.ligado, carro1.velocidade)