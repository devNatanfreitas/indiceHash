from ast import List
import math

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
                if not valor:
                    continue
                tupla = Tupla(chave=chave, valor=valor)
                chave += 1
                if pagina_atual.tamanho_pagina():
                    id_pag += 1
                    pagina_atual = Pagina(id=id_pag, capacidade=tam)
                    self.paginas.append(pagina_atual)
                pagina_atual.adicionar_tupla(tupla)

    def get_info_indice(self):
        info = []
        for pagina in self.paginas:
            for tupla in pagina.tuplas:
                info.append((tupla.chave, pagina.id))
        return info
    
    def get_total_pag(self) -> int:
        return len(self.paginas)

    def get_total_tuplas(self) -> int:
        return sum(len(p.tuplas) for p in self.paginas)
    
    def get_pagina(self, id_pagina: int) -> Pagina | None:
        if 0 <= id_pagina < len(self.paginas):
            return self.paginas[id_pagina]
        return None


class Bucket:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.entr = []
        self.overflow_bucket = None

    def cheio(self):
        return len(self.entr) >= self.capacidade

    def adicionar(self, chave: int, id_pag: int):
        if not self.cheio():
            self.entr.append((chave, id_pag))
        else:
            if self.overflow_bucket is None:
                self.overflow_bucket = Bucket(self.capacidade)
            self.overflow_bucket.adicionar(chave, id_pag)
            

    

class Hash:
    def __init__(self, fr: int):
        self.fr = fr
        self.nr = 0
        self.nb = 0
        self.buckets = []

    def funcao_hash(self, valor: int):
        hash_valor = sum(ord(c) for c in str(valor))
        return hash_valor % self.nb

    def construir(self, tabela: Tabela):
        dado_tabela = tabela.get_info_indice()
        self.nr = len(dado_tabela)    
        
        if self.nr == 0 or self.fr == 0:
            return

        self.nb = math.ceil(self.nr / self.fr)
        self.buckets = [Bucket(self.fr) for _ in range(self.nb)]
        

        for chave, valor, id_pag in dado_tabela:
            indice = self.funcao_hash(valor)
            self.buckets[indice].adicionar(chave, id_pag)
            
            
    def buscar(self, valor, tabela: Tabela):
        if not self.buckets:
            return []

        indice = self.funcao_hash(valor)
        bucket_atual = self.buckets[indice]
        
        pagina_visitar = set()
        
        while bucket_atual:
            for chave, id_pag in bucket_atual.entr:
                if chave == valor:
                    pagina_visitar.add(id_pag)
            bucket_atual = bucket_atual.overflow_bucket
            
        
        resultado = [] 
        custo = len(pagina_visitar)
        for id_pag in pagina_visitar:
            pagina = tabela.get_pagina(id_pag)
            for tupla in pagina.get_tuplas():
                if tupla.valor == valor:
                    resultado.append(tupla)

        return resultado