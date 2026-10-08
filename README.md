# Sistema de Planejamento Financeiro

## Descrição
Aplicação de terminal em Python que auxilia usuários a planejarem seu futuro financeiro através de simulações de investimentos com juros compostos mensais.

## Requisitos Implementados

### ✅ Requisitos Funcionais
- **Opção 1 - Simulação por Período Fixo**: Calcula a evolução mensal do patrimônio com aporte mensal e juros
- **Opção 2 - Cálculo de Meta Financeira**: Determina quantos meses são necessários para atingir um objetivo financeiro
- **Opção 3 - Sair**: Exporta todos os dados das simulações para arquivo CSV

### ✅ Requisitos Técnicos
- **Funções Modularizadas**: 
  - `validar_numero_positivo()` - Valida entradas numéricas
  - `simular_por_periodo()` - Cálculo de simulação por período
  - `calcular_meta_financeira()` - Cálculo de meta financeira
  - `exibir_historico()` - Exibição formatada dos dados
  - `exportar_csv()` - Persistência em arquivo CSV
  - `opcao1_simulacao_periodo()` - Interface da opção 1
  - `opcao2_meta_financeira()` - Interface da opção 2
  - `opcao3_sair()` - Interface de exportação e encerramento
  - `menu_principal()` - Controle do menu principal

- **Tratamento de Exceções**: 
  - Validação de entrada com try/except
  - Proteção contra entradas inválidas (letras, caracteres especiais)
  - Proteção contra números negativos ou zero
  - Tratamento de erros na exportação de CSV

- **Persistência de Dados**: 
  - Exportação em CSV com histórico mensal detalhado
  - Arquivo inclui: data, tipo de simulação, parâmetros e histórico completo
  - Resumo final com saldo inicial, final e ganho total

- **Estruturas de Repetição**:
  - `while True` para controle do menu principal
  - `for` para simulação de períodos fixos
  - `while` para cálculo de meta financeira (busca iterativa)

## Como Usar

### 1. Executar a Aplicação
```bash
python planejador_financeiro.py
```

### 2. Menu Principal
Ao iniciar, você terá 3 opções:

#### Opção 1: Simulação por Período Fixo
- Digite o valor inicial (ex: 1000)
- Digite o aporte mensal (ex: 100)
- Digite a taxa de juros mensal em % (ex: 1.5)
- Digite o número de meses (ex: 24)
- O programa exibirá a evolução mês a mês

#### Opção 2: Cálculo de Meta Financeira
- Digite o valor inicial (ex: 1000)
- Digite o aporte mensal (ex: 100)
- Digite a taxa de juros mensal em % (ex: 1.5)
- Digite o valor da meta desejada (ex: 5000)
- O programa calculará quantos meses são necessários

#### Opção 3: Sair
- O programa pergunta se deseja salvar os dados
- Digite o nome do arquivo (sem extensão .csv)
- O arquivo será criado com todos os históricos das simulações realizadas

## Exemplos de Uso

### Exemplo 1: Simulação por Período
```
Capital Inicial: R$ 1.000,00
Aporte Mensal: R$ 100,00
Taxa de Juros: 1% a.m.
Período: 12 meses

Resultado: Saldo final de aproximadamente R$ 2.341,35
```

### Exemplo 2: Meta Financeira
```
Capital Inicial: R$ 10.000,00
Aporte Mensal: R$ 500,00
Taxa de Juros: 0.8% a.m.
Meta: R$ 50.000,00

Resultado: ~73 meses (6 anos e 1 mês)
```

## Validação de Entrada

- ✅ Aceita números inteiros e decimais
- ✅ Rejeita valores negativos ou zero
- ✅ Rejeita entradas com letras ou caracteres especiais
- ✅ Solicita nova entrada em caso de erro
- ✅ Proteção contra interrupção não tratada (Ctrl+C)

## Arquivo CSV Gerado

O arquivo CSV contém:
- **Metadados**: Data de geração e tipo de simulação
- **Parâmetros**: Valores iniciais usados na simulação
- **Histórico Mensal**: Coluna por coluna:
  - Mês
  - Aporte (R$)
  - Rendimento (R$)
  - Saldo (R$)
- **Resumo Final**: Saldo inicial, final e ganho total

## Fórmula de Cálculo

A aplicação utiliza juros compostos mensais:

**Saldo(n) = (Saldo(n-1) + Juros(n-1)) + Aporte(n)**

Onde:
- **Juros(n-1)** = Saldo(n-1) × (Taxa / 100)
- **Taxa** = Taxa de juros mensal em percentual

## Estrutura do Código

```
planejador_financeiro.py
├── Funções de Validação
│   └── validar_numero_positivo()
├── Funções de Cálculo
│   ├── simular_por_periodo()
│   └── calcular_meta_financeira()
├── Funções de Interface
│   ├── exibir_historico()
│   ├── opcao1_simulacao_periodo()
│   ├── opcao2_meta_financeira()
│   └── opcao3_sair()
└── Funções de Controle
    ├── menu_principal()
    ├── exportar_csv()
    └── main()
```

## Recursos Adicionais

- 📊 Exibição formatada com tabelas
- 💾 Histórico armazenado para múltiplas simulações
- 🛡️ Tratamento robusto de erros
- 📋 Opção de combinar múltiplas simulações em um único arquivo CSV
- ⏰ Limite de proteção de 1200 meses (100 anos) para cálculos de meta

## Notas Importantes

- Todos os valores são arredondados para 2 casas decimais
- Os juros são aplicados antes do aporte mensal
- A aplicação permite múltiplas simulações na mesma sessão
- O arquivo CSV é criado no mesmo diretório onde o script está localizado
