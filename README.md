## 📋 Requisitos Principais

### ✅ 1. Interface Gráfica (1,0 ponto)
- [ ] Criar interface gráfica obrigatória
- [ ] Ilustrar estruturas de dados
- [ ] Mostrar funcionamento do índice hash
- [ ] Incluir campo para entrada da chave de busca
- [ ] Exibir resultado da busca e número da página
- [ ] Mostrar registros durante table scan

### ✅ 2. Funcionalidades Principais

#### 2.1 Construção do Índice
- [ ] Implementar carregamento do arquivo de dados
- [ ] Dividir dados em páginas conforme tamanho especificado
- [ ] Criar buckets com base no cálculo NB
- [ ] Aplicar função hash para mapear chaves

#### 2.2 Busca por Tupla
- [ ] Implementar busca usando índice construído
- [ ] Aplicar função hash na chave fornecida
- [ ] Localizar e ler página correspondente
- [ ] Exibir resultado na interface

#### 2.3 Table Scan
- [ ] Implementar botão para table scan
- [ ] Percorrer páginas sequencialmente
- [ ] Listar registros até encontrar a chave
- [ ] Calcular e exibir custo de leitura

### ✅ 3. Entidades/Estruturas (POO)

#### 3.1 Classe Tupla
- [ ] Implementar representação de linha da tabela
- [ ] Incluir valor da chave de busca
- [ ] Incluir dados da linha

#### 3.2 Classe Tabela (1,5 pontos)
- [ ] Implementar container para todas as tuplas
- [ ] Carregar dados do arquivo
- [ ] Organizar tuplas em estrutura adequada

#### 3.3 Classe Página (1,0 + 1,0 pontos)
- [ ] Implementar entrada para tamanho da página
- [ ] Calcular quantidade de páginas necessárias
- [ ] Representar divisão física da tabela
- [ ] Gerenciar alocação de tuplas por página

#### 3.4 Classe Bucket (0,5 pontos)
- [ ] Implementar mapeamento chave → endereço da página
- [ ] Calcular quantidade de buckets (NB > NR/FR)
- [ ] Definir tamanho dos buckets (FR)

#### 3.5 Função Hash (1,0 ponto)
- [ ] Projetar e implementar função hash
- [ ] Mapear chave de busca → endereço do bucket
- [ ] Documentar escolha da função

### ✅ 4. Parâmetros de Configuração

#### 4.1 Arquivo de Dados
- [ ] Usar arquivo com 466 mil palavras em inglês
- [ ] Source: https://github.com/dwyl/english-words
- [ ] Processar uma palavra por linha como chave única

#### 4.2 Configurações Dinâmicas
- [ ] Tamanho da página (entrada do usuário)
- [ ] Número de buckets (calculado: NB > NR/FR)
- [ ] Tamanho dos buckets (FR)
- [ ] Campo para chave de busca

### ✅ 5. Tratamento de Problemas

#### 5.1 Resolução de Colisões
- [ ] Implementar algoritmo para tratar colisões
- [ ] Calcular taxa de colisões (0,5 pontos)
- [ ] Exibir estatística na interface

#### 5.2 Overflow de Buckets
- [ ] Implementar algoritmo para resolver overflow
- [ ] Calcular taxa de overflows (0,5 pontos)
- [ ] Exibir estatística na interface

### ✅ 6. Funcionalidades de Pesquisa (2,0 pontos)
- [ ] Implementar busca por chave usando índice
- [ ] Retornar tupla e número da página
- [ ] Calcular e mostrar custo (acessos a disco)
- [ ] Validar funcionamento completo

### ✅ 7. Estatísticas e Métricas (0,5 pontos)
- [ ] Calcular estimativa de custo para busca indexada
- [ ] Calcular custo do table scan (páginas lidas)
- [ ] Exibir todas as métricas na interface
- [ ] Comparar eficiência entre métodos

### ✅ 8. Table Scan Completo (0,5 pontos)
- [ ] Implementar percurso sequencial
- [ ] Mostrar progresso na interface
- [ ] Calcular custo total
- [ ] Comparar com busca indexada

## 🔄 Fluxo de Funcionamento

### Etapa 1: Preparação
- [ ] Carregar arquivo de dados em memória
- [ ] Dividir linhas em páginas conforme tamanho

### Etapa 2: Construção do Índice
- [ ] Criar NB buckets de tamanho FR
- [ ] Aplicar função hash em cada tupla
- [ ] Armazenar mapeamento chave → endereço da página

### Etapa 3: Busca
- [ ] Receber chave de busca do usuário
- [ ] Aplicar função hash para encontrar página
- [ ] Ler página e buscar tupla
- [ ] Exibir resultado e custo

### Etapa 4: Table Scan
- [ ] Ativar botão após entrada da chave
- [ ] Percorrer páginas sequencialmente
- [ ] Mostrar progresso até encontrar chave
- [ ] Exibir custo total do scan

## 📊 Critérios de Avaliação

| Critério | Pontos | Status |
|----------|---------|---------|
| Interface gráfica | 1,0 | [ ] |
| Carga de dados nas páginas | 1,5 | [ ] |
| Entrada para tamanho da página | 1,0 | [ ] |
| Cálculo da quantidade de páginas | 1,0 | [ ] |
| Função hash | 1,0 | [ ] |
| Cálculo da quantidade de buckets | 0,5 | [ ] |
| Funcionamento com pesquisa | 2,0 | [ ] |
| Taxa de colisões | 0,5 | [ ] |
| Taxa de overflows | 0,5 | [ ] |
| Table scan | 0,5 | [ ] |
| Estimativa de custo | 0,5 | [ ] |
| **TOTAL** | **10,0** | |

## 🚀 Próximos Passos

### Sprint 1: Estruturas Básicas
- [ ] Definir arquitetura do projeto
- [ ] Implementar classes básicas (Tupla, Página, Bucket)
- [ ] Criar interface gráfica inicial

### Sprint 2: Core do Sistema
- [ ] Implementar função hash
- [ ] Desenvolver carregamento de dados
- [ ] Construir índice hash

### Sprint 3: Funcionalidades de Busca
- [ ] Implementar busca indexada
- [ ] Desenvolver table scan
- [ ] Calcular estatísticas

### Sprint 4: Refinamentos
- [ ] Tratar colisões e overflows
- [ ] Finalizar interface
- [ ] Preparar apresentação

## 📝 Notas Importantes
- Interface gráfica é **obrigatória**
- Usar **POO** como padrão
- Arquivo de dados: 466 mil palavras inglesas
- Apresentação obrigatória para a equipe
