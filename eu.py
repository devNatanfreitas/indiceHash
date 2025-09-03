import math
import time
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

    def esta_cheia(self):
        return len(self.tuplas) >= self.capacidade

    def get_tuplas(self):
        return self.tuplas

    def __repr__(self):
        return f"Pagina(id={self.id}, capacidade={self.capacidade}, tuplas={len(self.tuplas)})"


class Tabela:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.paginas = []

    def carregar(self, tam_pagina: int):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as file:
                id_pag = 0
                linhas = file.readlines()
                
                if not linhas:
                    return

                pagina_atual = Pagina(id=id_pag, capacidade=tam_pagina)
                self.paginas.append(pagina_atual)
                chave_id = 1
                for linha in linhas: 
                    valor = linha.strip()
                    if not valor:
                        continue
                    
                    tupla = Tupla(chave=chave_id, valor=valor)
                    chave_id += 1
                    
                    if pagina_atual.esta_cheia():
                        id_pag += 1
                        pagina_atual = Pagina(id=id_pag, capacidade=tam_pagina)
                        self.paginas.append(pagina_atual)
                    
                    pagina_atual.adicionar_tupla(tupla)
        except FileNotFoundError:
            print(f"ERRO: O arquivo '{self.arquivo}' não foi encontrado.")
            exit()


    def get_info_indice(self):
        info = []
        for pagina in self.paginas:
            for tupla in pagina.tuplas:
                info.append((tupla.chave, tupla.valor, pagina.id))
        return info
    
    def table_scan(self, valor_busca: str):
        custo = 0
        for pagina in self.paginas:
            custo += 1 
            for tupla in pagina.get_tuplas():
                if tupla.valor == valor_busca:
                    return tupla, custo
        
        return None, custo

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


class Hash:
    def __init__(self, fr: int):
        self.fr = fr 
        self.nr = 0  
        self.nb = 0  
        self.buckets = []
        self.total_colisoes = 0
        self.total_overflows = 0

    def funcao_hash(self, valor_str: str) -> int:
        hash_valor = sum(ord(c) for c in valor_str)
        return hash_valor % self.nb

    def construir(self, tabela: Tabela):
        dados_tabela = tabela.get_info_indice()
        self.nr = len(dados_tabela)    
        
        if self.nr == 0 or self.fr <= 0:
            print("Não é possível construir o índice: sem dados ou FR inválido.")
            return

        self.nb = math.ceil(self.nr / self.fr)
        self.buckets = [Bucket(self.fr) for _ in range(self.nb)]
        
        for chave_id, valor_str, id_pag in dados_tabela:
            indice = self.funcao_hash(valor_str)
            bucket_alvo = self.buckets[indice]

            if len(bucket_alvo.entradas) > 0:
                self.total_colisoes += 1
            
            ocorreu_overflow = bucket_alvo.adicionar(chave_id, id_pag)
            if ocorreu_overflow:
                self.total_overflows += 1
            
    def buscar(self, valor_busca: str, tabela: Tabela):
        if not self.buckets:
            return None, 0

        indice = self.funcao_hash(valor_busca)
        bucket_atual = self.buckets[indice]
        
        paginas_a_visitar = set()
        
        while bucket_atual:
            for _, id_pag in bucket_atual.entradas:
                paginas_a_visitar.add(id_pag)
            bucket_atual = bucket_atual.overflow_bucket
            
        resultado = None
        custo = len(paginas_a_visitar)
        
        for id_pag in paginas_a_visitar:
            pagina = tabela.get_pagina(id_pag)
            if pagina:
                for tupla in pagina.get_tuplas():
                    if tupla.valor == valor_busca:
                        resultado = tupla
                        return resultado, custo, id_pag
        
        return None, custo, None

    def get_estatisticas(self):
        if self.nr == 0:
            return {
                "total_registros": 0, "total_colisoes": 0, "taxa_colisao (%)": 0,
                "total_overflows": 0, "taxa_overflow (%)": 0,
            }
        
        taxa_colisao = (self.total_colisoes / self.nr) * 100
        taxa_overflow = (self.total_overflows / self.nr) * 100
        
        return {
            "total_registros": self.nr,
            "total_colisoes": self.total_colisoes,
            "taxa_colisao (%)": round(taxa_colisao, 2),
            "total_overflows": self.total_overflows,
            "taxa_overflow (%)": round(taxa_overflow, 2),
        }


if __name__ == "__main__":  
    # 1. Definir o nome do arquivo a ser lido
    NOME_ARQUIVO = "words.txt"

    # 2. Carregar os dados na tabela
    tamanho_pagina = 100 # Quantas palavras por página
    tabela = Tabela(NOME_ARQUIVO)
    tabela.carregar(tam_pagina=tamanho_pagina)
    
    # Só continua se a tabela tiver sido carregada com sucesso
    if tabela.get_total_tuplas() > 0:
        print(f"Arquivo '{NOME_ARQUIVO}' carregado com sucesso!")
        print(f"Total de Tuplas: {tabela.get_total_tuplas()}")
        print(f"Total de Páginas: {tabela.get_total_pag()}")
        print("-" * 30)

        # 3. Construir o índice hash
        tamanho_bucket_fr = 50 # Quantas tuplas por bucket
        indice_hash = Hash(fr=tamanho_bucket_fr)
        indice_hash.construir(tabela)

        # 4. Exibir estatísticas
        estatisticas = indice_hash.get_estatisticas()
        print("Estatísticas do Índice Hash:")
        for key, value in estatisticas.items():
            print(f"  {key}: {value}")
        print("-" * 30)

        # 5. Fazer buscas
        palavra_a_buscar = "Apple" # Mude para qualquer palavra que você espera que esteja no arquivo
        
        # Busca com Table Scan
        print(f"Buscando '{palavra_a_buscar}' com Table Scan...")
        inicio = time.time()
        resultado_scan, custo_scan = tabela.table_scan(palavra_a_buscar)
        fim = time.time()
        print(f"  Tempo de Busca: {fim - inicio:.6f} segundos")
        if resultado_scan:
            print(f"  Encontrado: {resultado_scan}")
            print(f"  Custo (páginas lidas): {custo_scan}")
        else:
            print(f"  Não encontrado. Custo total (páginas lidas): {custo_scan}")
        print("-" * 20)

        # Busca com Índice Hash
        print(f"Buscando '{palavra_a_buscar}' com Índice Hash...")
        inicio = time.time()
        resultado_hash, custo_hash, pag_id = indice_hash.buscar(palavra_a_buscar, tabela)
        fim = time.time()
        print(f"  Tempo de Busca: {fim - inicio:.6f} segundos")
        if resultado_hash:
            print(f"  Encontrado: {resultado_hash}")
            print(f"  Localizado na Página ID: {pag_id}")
            print(f"  Custo (páginas lidas): {custo_hash}")
        
        else:
            print(f"  Não encontrado. Custo (páginas verificadas): {custo_hash}")
        print("-" * 30)