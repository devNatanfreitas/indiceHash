
from ast import List


class Tupla:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

    def __repr__(self):
        return f"Tupla(chave={self.chave}, valor={self.valor})"


class Pagina:
    def __init__(self, id: int, capacidade: int):
        self.id = id
        self.capacidade = capacidade
        self.tuplas = []

    def adicionar_tupla(self, tupla: Tupla):
        if len(self.tuplas) < self.capacidade:
            self.tuplas.append(tupla)
        else:
            raise Exception("Capacidade da página excedida")

    def tamanho_pagina(self):
        return len(self.tuplas) >= self.capacidade

    def get_tuplas(self):
        return self.tuplas

    def __repr__(self):
        return f"Pagina(capacidade={self.capacidade}, tuplas={self.tuplas})"



class Tabela:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.paginas = []

    def carregar(self, tam):
        with open(self.arquivo, 'r', encoding='utf-8') as file:
            id_pag = 0
            linhas = file.readlines()
            pagina_atual = Pagina(id=id_pag, capacidade=tam)
            self.paginas.append(pagina_atual)
            chave = 1
            for linha in linhas: 
                valor = linha.strip()
                tupla = Tupla(chave=chave, valor=valor)
                chave += 1
                if pagina_atual.tamanho_pagina():
                    id_pag += 1
                    pagina_atual = Pagina(id=id_pag, capacidade=tam)
                    self.paginas.append(pagina_atual)
                pagina_atual.adicionar_tupla(tupla)

    # def get_info_indice(self):
    #     info = []
    #     for pagina in self.paginas:
    #         for tupla in pagina.tuplas:
    #             info.append((tupla.chave, pagina.id))
    #     return info
    
    def get_total_pag(self) -> int:
        return len(self.paginas)

    def get_total_tuplas(self) -> int:
        return sum(len(p.tuplas) for p in self.paginas)


class Bucket:
    def __init__(self, tabela: Tabela):
        self.tuplas = []
        self.adicionar(tabela)

    def adicionar(self, tabela: Tabela):
        for pagina in tabela.paginas:
            for tupla in pagina.tuplas:
                self.tuplas.append(tupla)

    def buscar(self, chave: int):
        id_pag_enc = []
        for tupla, id_pag in self.tuplas:
            if tupla.chave == chave:
                id_pag_enc.append(id_pag)
        return id_pag_enc

class Hash:
    def __init__(self, n: int):
        self.n = n
        self.buckets = [Bucket() for _ in range(n)]

    def funcao_hash(self, valor: int) -> int:
        hash_valor = sum(ord(c) for c in str(valor))
        return hash_valor % self.n

    def construir(self, dado_tabela: list[tuple]):
        for chave, valor, id_pag in dado_tabela:
            indice = self.funcao_hash(valor)
            self.buckets[indice].adicionar(chave, id_pag)
            
            
    def buscar(self, chave: int) -> List[int]:
        indice = self.funcao_hash(chave)
        bucket = self.buckets[indice]
        
        ender = []
        for chave, id_pag in bucket.tuplas:
            ender.append(id_pag)
        return ender
