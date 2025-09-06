from obj.tupla import Tupla


class Page:
    def __init__(self, id: int, capacidade: int):
        self.id = id
        self.capacidade = capacidade
        self.tuplas = []

    def adicionar_tupla(self, tupla: Tupla):
        if len(self.tuplas) < self.capacidade:
            self.tuplas.append(tupla)
        else:
            raise Exception("Capacidade da página excedida")

    def esta_cheia(self):
        return len(self.tuplas) >= self.capacidade

    def get_tuplas(self):
        return self.tuplas

    def __repr__(self):
        return f"Pagina(id={self.id}, capacidade={self.capacidade}, tuplas={len(self.tuplas)})"
