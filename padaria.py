#letisgooo padaria <3
class Padeiro:
    def __init__(self, nome):
        self.nome = nome
        self.dinheiro = 0
        self.paes = 0
        pass
    
    def assar_paes(self, quantidade):
        if quantidade > 6:
            print("\nForno lotado")
        else:
            self.paes += quantidade
        pass

class Cliente:
    def __init__(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro
        self.paes = 0
        pass

    def comprar_paes(self, quantidade, padeiro):
        preco_pao = quantidade * 0.5
        if quantidade > padeiro.paes:
            print("\nAcabou o paozinho")
        elif self.dinheiro < preco_pao:
            print("\nPobre!")
        else:
            self.dinheiro -= preco_pao
            self.paes += quantidade
            Padeiro.dinheiro += preco_pao
            Padeiro.paes -= quantidade
            print(f"\nCompra aprovada! Agora, {self.nome}, tem {self.paes} pães e {self.dinheiro} reais. {padeiro.nome} tem {padeiro.paes} paes e {padeiro.dinheiro} reais.")
        pass

padeiro1 = Padeiro('Joaquim')
padeiro1.assar_paes(6)
cliente1 = Cliente('Maria', 10)
cliente1.comprar_paes(3, padeiro1)