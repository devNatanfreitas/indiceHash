class Tupla:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

    def __repr__(self):
        return f"Tupla(chave={self.chave}, valor={self.valor})"
