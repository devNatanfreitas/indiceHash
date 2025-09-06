class Bucket:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.entradas = []
        self.overflow_bucket = None

    def esta_cheio(self):
        return len(self.entradas) >= self.capacidade

    def adicionar(self, chave: int, id_pag: int) -> bool:
        if not self.esta_cheio():
            self.entradas.append((chave, id_pag))
            return False
        else:
            if self.overflow_bucket is None:
                self.overflow_bucket = Bucket(self.capacidade)
            self.overflow_bucket.adicionar(chave, id_pag)
            return True
