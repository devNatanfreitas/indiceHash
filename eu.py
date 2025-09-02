
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


table = Tabela('words.txt')

table.carregar(tam=50)

print(f'Total de páginas: {table.get_total_pag()}')
print(f'Total de tuplas: {table.get_total_tuplas()}')

print("Informações do índice:")
print(table.get_info_indice())















