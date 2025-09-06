import time

from obj.hash import Hash
from obj.table import Table

if __name__ == "__main__":  
    # 1. Definir o nome do arquivo a ser lido
    NOME_ARQUIVO = "words.txt"

    # 2. Carregar os dados na tabela
    tamanho_pagina = 100 # Quantas palavras por página
    tabela = Table(NOME_ARQUIVO)
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