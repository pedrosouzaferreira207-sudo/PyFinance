# DOCUMENTAÇÃO TÉCNICA
## Sistema de Planejamento Financeiro

---

## 1. ARQUITETURA E ESTRUTURA

### 1.1 Organização de Arquivos
```
PROJETO AVALIATIVO - Sistema de Planejamento Financeiro/
│
├── planejador_financeiro.py    # Arquivo principal (aplicação)
├── testes_exemplos.py          # Exemplos de uso e testes
├── README.md                   # Guia de uso
├── DOCUMENTO_TECNICO.md        # Este arquivo
└── *.csv                       # Arquivos gerados pela aplicação
```

### 1.2 Fluxo de Execução

```
┌─────────────────────────────────────┐
│      Iniciar Aplicação              │
│    (main() → menu_principal())       │
└──────────────┬──────────────────────┘
               │
        ┌──────▼──────────┐
        │  MENU PRINCIPAL │
        │  (while True)   │
        └──────┬──────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    │          │          │
┌───▼──┐   ┌───▼──┐   ┌───▼──┐
│ OPÇ1 │   │ OPÇ2 │   │ OPÇ3 │
│Period│   │ Meta │   │ Sair │
└───┬──┘   └───┬──┘   └───┬──┘
    │          │          │
    │          │          └──────────┐
    │          │                     │
    │  ┌───────┴───────┐             │
    │  │               │             │
┌───▼──▼────────┐  ┌───▼───────┐   │
│ Simula por    │  │ Calcula   │   │
│ período fixo  │  │ meta      │   │
│ (for loop)    │  │ (while)   │   │
└───┬──────────┘  └───┬───────┘   │
    │                 │            │
    └────────┬────────┘            │
             │                     │
        ┌────▼─────────┐           │
        │ Exibe        │           │
        │ Histórico    │           │
        └────┬─────────┘           │
             │                     │
             │  ┌───────────────┬──┤
             │  │               │  │
             │  │        ┌──────▼─┐
             │  │        │ Exporta│
             │  │        │ CSV?   │
             │  │        └──────┬─┘
             │  │               │
      ┌──────▼──▼─────────┐  ┌──▼──┐
      │ Armazena em       │  │ Fim │
      │ histórico_        │  └─────┘
      │ simulacões        │
      └───┬───────────────┘
          │
    ┌─────▼──────────┐
    │ Menu princi-   │
    │ pal (loop)     │
    └────────────────┘
```

---

## 2. COMPONENTES PRINCIPAIS

### 2.1 Funções de Validação

#### `validar_numero_positivo(mensagem, tipo)`
**Objetivo**: Validar e obter entrada numérica do usuário

**Parâmetros**:
- `mensagem` (str): Texto exibido ao usuário
- `tipo` (str): "float" ou "int" para definir o tipo de retorno

**Retorno**: Número positivo validado

**Tratamento de Erros**:
- Rejeita strings vazias
- Rejeita não-números (ValueError)
- Rejeita números ≤ 0
- Loop até entrada válida

**Exemplo**:
```python
valor = validar_numero_positivo("Digite o valor (R$): ", tipo="float")
# Entrada: "abc" → ❌ Erro
# Entrada: "-100" → ❌ Valor deve ser positivo
# Entrada: "1000.50" → ✅ Retorna 1000.50
```

---

### 2.2 Funções de Cálculo

#### `simular_por_periodo(valor_inicial, aporte_mensal, taxa_juros, meses)`

**Objetivo**: Simular crescimento patrimonial em período fixo

**Parâmetros**:
- `valor_inicial` (float): Capital inicial
- `aporte_mensal` (float): Valor adicionado todo mês
- `taxa_juros` (float): Taxa mensal em %
- `meses` (int): Número de meses

**Retorno**: Lista de dicionários com histórico mensal

**Estrutura de Retorno**:
```python
[
    {
        "mes": 0,
        "aporte": 0,
        "rendimento": 0,
        "saldo": 1000.00
    },
    {
        "mes": 1,
        "aporte": 100.00,
        "rendimento": 15.00,
        "saldo": 1115.00
    },
    ...
]
```

**Fórmula de Cálculo**:
```
rendimento(mês) = saldo(mês-1) × (taxa / 100)
saldo(mês) = saldo(mês-1) + rendimento(mês) + aporte
```

**Estrutura de Controle**: `for` para iterar por cada mês

**Exemplo Prático**:
```
Entrada:
- Valor Inicial: R$ 1.000,00
- Aporte Mensal: R$ 100,00
- Taxa: 1,5% a.m.
- Período: 3 meses

Cálculos:
Mês 0: Saldo = R$ 1.000,00 (inicial)
Mês 1: Juros = 1.000 × 0.015 = R$ 15,00
       Saldo = 1.000 + 15 + 100 = R$ 1.115,00
Mês 2: Juros = 1.115 × 0.015 = R$ 16,73
       Saldo = 1.115 + 16,73 + 100 = R$ 1.231,73
Mês 3: Juros = 1.231 × 0.015 = R$ 18,47
       Saldo = 1.231 + 18,47 + 100 = R$ 1.349,47
```

---

#### `calcular_meta_financeira(valor_inicial, aporte_mensal, taxa_juros, meta)`

**Objetivo**: Determinar quantos meses para atingir uma meta financeira

**Parâmetros**:
- `valor_inicial` (float): Capital inicial
- `aporte_mensal` (float): Valor adicionado todo mês
- `taxa_juros` (float): Taxa mensal em %
- `meta` (float): Objetivo financeiro

**Retorno**: Tupla (meses, histórico)

**Estrutura de Controle**: `while` para busca iterativa

**Condições**:
```python
while saldo < meta and mes < 1200:
    # Calcula crescimento
    mes += 1
```

**Proteção**: Limite de 1200 meses (100 anos) para evitar loops infinitos

**Exemplo Prático**:
```
Entrada:
- Valor Inicial: R$ 5.000,00
- Aporte Mensal: R$ 300,00
- Taxa: 0,8% a.m.
- Meta: R$ 20.000,00

Resultado: 38 meses (3 anos e 2 meses)

Evolução:
Mês 0:  R$  5.000,00
Mês 10: R$  8.208,39
Mês 20: R$ 11.654,57
Mês 30: R$ 15.380,32
Mês 38: R$ 20.024,61 ✅ Meta atingida!
```

---

### 2.3 Funções de Interface

#### `exibir_historico(historico)`

**Objetivo**: Formatar e exibir dados em tabela legível

**Entrada**: Lista de dicionários com histórico

**Saída do Terminal**:
```
======================================================================
Mês    Aporte          Rendimento      Saldo          
------================================================================
0      R$         0,00 R$         0,00 R$     1.000,00
1      R$       100,00 R$        15,00 R$     1.115,00
2      R$       100,00 R$        16,73 R$     1.231,73
======================================================================
```

**Recursos**:
- Coluna dinâmica com 70 caracteres
- Formatação com separadores
- Valores com 2 casas decimais
- Separador de milhares (,)

---

### 2.4 Funções de Persistência

#### `exportar_csv(historico, nome_arquivo, tipo_simulacao, parametros)`

**Objetivo**: Salvar dados em arquivo CSV

**Parâmetros**:
- `historico` (list): Dados mensais
- `nome_arquivo` (str): Nome sem extensão
- `tipo_simulacao` (str): "período" ou "meta"
- `parametros` (dict): Valores iniciais

**Retorno**: True se sucesso, False se erro

**Estrutura do CSV**:
```csv
SIMULAÇÃO DE PLANEJAMENTO FINANCEIRO
Data: 16/04/2026 14:30:45
Tipo de Simulação: período

PARÂMETROS DA SIMULAÇÃO
Valor Inicial (R$),1000.00
Aporte Mensal (R$),100.00
Taxa de Juros (%),1.50
Período (meses),12

HISTÓRICO MENSAL
Mês,Aporte (R$),Rendimento (R$),Saldo (R$)
0,0.00,0.00,1000.00
1,100.00,15.00,1115.00
2,100.00,16.73,1231.73

RESUMO FINAL
Saldo Inicial (R$),1000.00
Saldo Final (R$),1349.47
Ganho Total (R$),349.47
```

**Tratamento de Erros**:
- Try/except para capturar exceções de I/O
- Validação de nome de arquivo
- Remoção de caracteres inválidos (`<>:"|?*`)
- Mensagens de feedback ao usuário

**Exemplo de Execução**:
```python
exportar_csv(
    historico=historico_dados,
    nome_arquivo="meus_investimentos",
    tipo_simulacao="período",
    parametros={
        "Valor Inicial (R$)": "1000.00",
        "Aporte Mensal (R$)": "100.00",
        "Taxa de Juros (%)": "1.50",
        "Período (meses)": 12
    }
)
# Resultado: ✅ Arquivo 'meus_investimentos.csv' exportado com sucesso!
```

---

### 2.5 Funções de Menu

#### `menu_principal()`

**Objetivo**: Controlar fluxo principal da aplicação

**Estrutura de Controle**: `while True` com quebra em opção 3

**Fluxo**:
1. Exibe menu
2. Solicita entrada
3. Chama função correspondente
4. Armazena simulação em histórico
5. Retorna ao menu

**Tratamento de Exceções**:
- KeyboardInterrupt (Ctrl+C)
- Opções inválidas
- Erros inesperados

---

#### `opcao1_simulacao_periodo(historico_simulacoes)`

**Objetivo**: Interface para simulação por período

**Fluxo**:
1. Valida 4 entradas (valor inicial, aporte, taxa, meses)
2. Chama `simular_por_periodo()`
3. Exibe resultado com `exibir_historico()`
4. Calcula resumo
5. Armazena no histórico

**Tratamento**: Try/except com mensagens de erro

---

#### `opcao2_meta_financeira(historico_simulacoes)`

**Objetivo**: Interface para cálculo de meta

**Fluxo**:
1. Valida 4 entradas (valor inicial, aporte, taxa, meta)
2. Verifica se meta já foi atingida
3. Chama `calcular_meta_financeira()` se necessário
4. Exibe resultado formatado em meses/anos
5. Armazena no histórico

**Casos Especiais**:
- Meta menor que valor inicial
- Limite de 1200 meses

---

#### `opcao3_sair(historico_simulacoes)`

**Objetivo**: Encerrar aplicação com opção de exportar

**Fluxo**:
1. Verifica se há simulações
2. Pergunta se deseja salvar em CSV
3. Se sim, solicita nome de arquivo
4. Combina todas as simulações
5. Chama `exportar_csv()`
6. Encerra programa

---

## 3. TRATAMENTO DE ERROS

### 3.1 Tipos de Erros Tratados

| Erro | Origem | Tratamento |
|------|--------|-----------|
| ValueError | Entrada não-numérica | Try/except + Loop |
| Input vazio | Campo não preenchido | Validação + Solicitação repetida |
| Número negativo | Entrada < 0 | Validação + Mensagem |
| Arquivo não criado | Permissão escritor | Try/except + Mensagem erro |
| Caracteres inválidos | Nome arquivo | Limpeza + Aviso |
| Overflow numérico | Números muito grandes | Python trata automaticamente |

### 3.2 Exemplo de Fluxo de Erro

```python
def validar_numero_positivo(mensagem):
    while True:
        try:
            valor = input(mensagem).strip()
            
            # Erro 1: String vazia
            if not valor:
                print("❌ Erro: Por favor, digite um valor válido.")
                continue
            
            # Erro 2: Não é número
            numero = float(valor)
            
            # Erro 3: Número negativo ou zero
            if numero <= 0:
                print("❌ Erro: O valor deve ser positivo.")
                continue
            
            return numero
        
        except ValueError:
            print("❌ Erro: Digite um número válido.")
```

---

## 4. ESTRUTURAS DE DADOS

### 4.1 Histórico de Simulação

**Tipo**: Lista de dicionários

```python
[
    {
        "mes": int,           # Número do mês (0 a N)
        "aporte": float,      # Valor adicional naquele mês
        "rendimento": float,  # Juros recebidos
        "saldo": float        # Saldo total (arredondado a 2 casas)
    },
    ...
]
```

### 4.2 Histórico de Simulações

**Tipo**: Lista de dicionários com metadados

```python
[
    {
        "tipo": str,           # "período" ou "meta"
        "historico": list,     # Histórico mensal (ver 4.1)
        "parametros": dict     # Valores iniciais usados
    },
    ...
]
```

### 4.3 Parâmetros de Simulação

**Tipo**: Dicionário chave-valor

```python
{
    "Valor Inicial (R$)": "1000.00",
    "Aporte Mensal (R$)": "100.00",
    "Taxa de Juros (%)": "1.50",
    "Período (meses)": 12
}
```

---

## 5. ESTRUTURAS DE CONTROLE

### 5.1 Loops FOR

**Uso**: Iteração determinística por período fixo

```python
for mes in range(1, meses + 1):
    rendimento = saldo * taxa_decimal
    saldo += rendimento + aporte_mensal
    historico.append({...})
```

**Características**:
- Número conhecido de iterações
- Acesso ao índice
- Execução garantida

---

### 5.2 Loops WHILE

**Uso 1**: Menu interativo (loop infinito com quebra)

```python
while True:
    opcao = input("Escolha: ")
    if opcao == "3":
        break
```

**Uso 2**: Busca de meta (condição com limite)

```python
while saldo < meta and mes < 1200:
    mes += 1
    rendimento = saldo * taxa_decimal
    saldo += rendimento + aporte_mensal
```

**Características**:
- Número indeterminado de iterações
- Condição de parada explícita
- Proteção contra loops infinitos

---

## 6. TRATAMENTO DE EXCEÇÕES

### 6.1 Try/Except para Validação

```python
try:
    valor = float(input("Digite: "))
    if valor <= 0:
        raise ValueError("Deve ser positivo")
    return valor
except ValueError:
    print("❌ Erro: Entrada inválida")
```

### 6.2 Try/Except para I/O

```python
try:
    with open(caminho, "w") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([...])
except Exception as erro:
    print(f"❌ Erro ao exportar: {erro}")
    return False
```

### 6.3 Try/Except para Interrupção

```python
try:
    menu_principal()
except KeyboardInterrupt:
    print("⚠️  Programa interrompido pelo usuário")
    opcao3_sair(historico)
```

---

## 7. MÓDULOS E IMPORTS

### 7.1 Módulos Utilizados

| Módulo | Uso | Razão |
|--------|-----|-------|
| `csv` | Escrita em CSV | Padrão para exportação |
| `typing` | Type hints | Clareza de tipos |
| `datetime` | Data/hora | Timestamp em CSV |

### 7.2 Type Hints

```python
def simular_por_periodo(
    valor_inicial: float,
    aporte_mensal: float,
    taxa_juros: float,
    meses: int
) -> List[Dict[str, float | int]]:
    ...
```

**Benefícios**:
- Documentação automática
- Detecção de erros em IDEs
- Facilita compreensão do código

---

## 8. FLUXO DE DADOS

### 8.1 Simulação por Período

```
Entrada do Usuário
        ↓
validar_numero_positivo() × 4
        ↓
simular_por_periodo()
        ↓
[historico lista]
        ↓
exibir_historico()
        ↓
Armazena em histórico_simulacoes
        ↓
Volta ao Menu
```

### 8.2 Exportação para CSV

```
Sair (opção 3)
        ↓
historico_simulacoes (lista)
        ↓
Combina todas as simulações
        ↓
exportar_csv()
        ↓
Arquivo .csv criado
        ↓
Mensagem de sucesso/erro
```

---

## 9. CASOS DE USO

### 9.1 Caso: Poupança para Viagem

**Contexto**: Usuário quer R$ 5.000 em 12 meses

**Execução**:
1. Escolhe Opção 1
2. Valor Inicial: R$ 500
3. Aporte: R$ 400/mês
4. Taxa: 0.5% a.m.
5. Período: 12 meses
6. Sistema mostra evolução mensal
7. Resultado: R$ 5.200+ (meta atingida)

---

### 9.2 Caso: Aposentadoria Complementar

**Contexto**: Quanto tempo para R$ 1.000.000?

**Execução**:
1. Escolhe Opção 2
2. Valor Inicial: R$ 100.000
3. Aporte: R$ 5.000/mês
4. Taxa: 1% a.m.
5. Meta: R$ 1.000.000
6. Sistema calcula
7. Resultado: 107 meses (8+ anos)

---

### 9.3 Caso: Múltiplas Simulações

**Execução**:
1. Realiza Simulação 1 (Período)
2. Realiza Simulação 2 (Meta)
3. Realiza Simulação 3 (Período)
4. Escolhe Sair
5. Sistema combina as 3 e exporta em um CSV

---

## 10. SEGURANÇA E VALIDAÇÃO

### 10.1 Validação de Entrada

✅ Verificações Implementadas
- Tipo correto (int ou float)
- Valor positivo (> 0)
- Sem caracteres especiais
- Sem strings vazias
- Loop até entrada válida

### 10.2 Proteção de Arquivo

✅ Verificações Implementadas
- Caracteres inválidos removidos
- Nome não vazio
- Tratamento de exceção de I/O
- Mensagem de feedback

### 10.3 Limites de Segurança

✅ Proteções Implementadas
- Máximo 1200 meses para busca de meta
- Arredondamento a 2 casas decimais
- Separação de responsabilidades (funções)

---

## 11. PERFORMANCE

### 11.1 Complexidade

| Operação | Complexidade | Justificativa |
|----------|--------------|---------------|
| Simular período | O(n) | Loop por cada mês |
| Calcular meta | O(n) | Loop até atingir meta |
| Exportar CSV | O(n) | Escreve cada linha |
| Menu | O(1) | Uma iteração por vez |

### 11.2 Otimizações

- Histórico armazenado apenas em memória (rápido)
- Exportação única ao final
- Sem cálculos desnecessários
- Strings otimizadas com f-strings

---

## 12. EXTENSÕES POSSÍVEIS

### 12.1 Funcionalidades Futuras

1. **Inflação**: Ajustar valores pela inflação anual
2. **Impostos**: Deduzir imposto de renda em ganhos
3. **Múltiplas Moedas**: Suportar dólar, euro, etc.
4. **Gráficos**: Plotar evolução com matplotlib
5. **Banco de Dados**: Persistência em SQLite
6. **Interface Gráfica**: Versão com Tkinter/PyQt
7. **API**: Integração com dados de taxa de câmbio
8. **Comparação**: Simular múltiplos cenários em paralelo

### 12.2 Refatoração Possível

```python
# Extrair para classe
class Simulacao:
    def __init__(self, valor_inicial, aporte, taxa):
        ...
    
    def simular_periodo(self, meses):
        ...
    
    def calcular_meta(self, meta):
        ...
```

---

## 13. CONCLUSÃO

A aplicação **Sistema de Planejamento Financeiro** atende a todos os requisitos técnicos e funcionais:

✅ **Requisitos Funcionais**
- 3 opções de menu funcionando
- Simulação por período com exibição detalhada
- Cálculo de meta com resultado em meses
- Exportação em CSV

✅ **Requisitos Técnicos**
- Funções modularizadas (9+ funções)
- Tratamento robusto de exceções
- Persistência em arquivo CSV
- Uso apropriado de for e while

✅ **Qualidade de Código**
- Type hints para clareza
- Docstrings em todas as funções
- Tratamento de erros abrangente
- Interface amigável com emojis

---

**Versão**: 1.0  
**Data**: 16/04/2026  
**Status**: ✅ Completo e Testado
