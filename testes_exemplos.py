from index import (
    simular_por_periodo,
    calcular_meta_financeira,
    exibir_historico,
    exportar_csv
)


def teste_simulacao_periodo():
    print("\n" + "="*70)
    print("TESTE 1: SIMULAÇÃO POR PERÍODO FIXO")
    print("="*70)
    print("\nParâmetros:")
    print("  - Valor Inicial: R$ 1.000,00")
    print("  - Aporte Mensal: R$ 100,00")
    print("  - Taxa de Juros: 1,5% a.m.")
    print("  - Período: 12 meses")

    historico = simular_por_periodo(
        valor_inicial=1000.00,
        aporte_mensal=100.00,
        taxa_juros=1.5,
        meses=12
    )

    exibir_historico(historico)

    saldo_inicial = historico[0]["saldo"]
    saldo_final = historico[-1]["saldo"]
    ganho = saldo_final - saldo_inicial

    print(f"\n📊 Resumo:")
    print(f"   Saldo Inicial: R$ {saldo_inicial:,.2f}")
    print(f"   Saldo Final: R$ {saldo_final:,.2f}")
    print(f"   Ganho Total: R$ {ganho:,.2f}")

    return historico


def teste_meta_financeira():
    print("\n" + "="*70)
    print("TESTE 2: CÁLCULO DE META FINANCEIRA")
    print("="*70)
    print("\nParâmetros:")
    print("  - Valor Inicial: R$ 5.000,00")
    print("  - Aporte Mensal: R$ 500,00")
    print("  - Taxa de Juros: 0,8% a.m.")
    print("  - Meta: R$ 50.000,00")

    meses, historico = calcular_meta_financeira(
        valor_inicial=5000.00,
        aporte_mensal=500.00,
        taxa_juros=0.8,
        meta=50000.00
    )

    exibir_historico(historico)

    anos = meses // 12
    meses_restantes = meses % 12

    print(f"\n📊 Resultado:")
    print(f"   Meses necessários: {meses}")
    print(f"   Período: {anos} ano(s) e {meses_restantes} mês/meses")
    print(f"   Saldo Final: R$ {historico[-1]['saldo']:,.2f}")

    return meses, historico


def teste_exportacao_csv():
    print("\n" + "="*70)
    print("TESTE 3: EXPORTAÇÃO PARA CSV")
    print("="*70)

    print("\nGerando simulação de teste...")
    historico = simular_por_periodo(
        valor_inicial=1000.00,
        aporte_mensal=200.00,
        taxa_juros=2.0,
        meses=6
    )

    parametros = {
        "Valor Inicial (R$)": "1000.00",
        "Aporte Mensal (R$)": "200.00",
        "Taxa de Juros (%)": "2.00",
        "Período (meses)": 6
    }

    sucesso = exportar_csv(
        historico=historico,
        nome_arquivo="teste_simulacao",
        tipo_simulacao="período",
        parametros=parametros
    )

    if sucesso:
        print("\n✅ Experimente abrir o arquivo 'teste_simulacao.csv' em um editor de texto")
        print("   ou em uma planilha eletrônica (Excel, Google Sheets, etc.)")


def teste_tratamento_erros():
    print("\n" + "="*70)
    print("TESTE 4: TRATAMENTO DE ERROS")
    print("="*70)
    print("\n⚠️  NOTA: Os testes a seguir demonstram situações de erro.")
    print("   Na aplicação real, o usuário será solicitado a tentar novamente.\n")

    print("1️⃣  Teste com valor zero:")
    print("   Entrada: 0")
    print("   Resultado: ❌ Será solicitado outro valor (valor deve ser positivo)\n")

    print("2️⃣  Teste com valor negativo:")
    print("   Entrada: -1000")
    print("   Resultado: ❌ Será solicitado outro valor (valor deve ser positivo)\n")

    print("3️⃣  Teste com letras:")
    print("   Entrada: abc")
    print("   Resultado: ❌ Será solicitado outro valor (deve ser um número)\n")

    print("4️⃣  Teste com caracteres especiais:")
    print("   Entrada: 1@2#3")
    print("   Resultado: ❌ Será solicitado outro valor (deve ser um número)\n")

    print("5️⃣  Teste com meta menor que valor inicial:")
    print("   Valor Inicial: R$ 10.000,00")
    print("   Meta: R$ 5.000,00")
    print("   Resultado: ⚠️  Aviso de que a meta já foi atingida\n")


def teste_casos_reais():
    print("\n" + "="*70)
    print("TESTE 5: CASOS REAIS DE PLANEJAMENTO")
    print("="*70)

    print("\n📌 CASO 1: Poupança para Viagem (12 meses)")
    print("-" * 70)
    print("Objetivo: Juntar R$ 5.000,00 para uma viagem em um ano")

    historico1 = simular_por_periodo(
        valor_inicial=500.00,
        aporte_mensal=400.00,
        taxa_juros=0.5,
        meses=12
    )

    print(f"Saldo final: R$ {historico1[-1]['saldo']:,.2f}")
    print(f"Resultado: ✅ {'Meta atingida!' if historico1[-1]['saldo'] >= 5000 else 'Meta não atingida'}")

    print("\n📌 CASO 2: Aposentadoria Complementar (20 anos)")
    print("-" * 70)
    print("Objetivo: Acumular capital para aposentadoria")

    historico2 = simular_por_periodo(
        valor_inicial=50000.00,
        aporte_mensal=1000.00,
        taxa_juros=1.0,
        meses=240
    )

    print(f"Saldo final: R$ {historico2[-1]['saldo']:,.2f}")
    ganho = historico2[-1]['saldo'] - historico2[0]['saldo']
    print(f"Ganho total: R$ {ganho:,.2f}")

    print("\n📌 CASO 3: Quantos Meses para 1 Milhão?")
    print("-" * 70)
    print("Objetivo: Descobrir o tempo para atingir R$ 1.000.000,00")

    meses, historico3 = calcular_meta_financeira(
        valor_inicial=100000.00,
        aporte_mensal=5000.00,
        taxa_juros=1.2,
        meta=1000000.00
    )

    anos = meses // 12
    meses_remainder = meses % 12
    print(f"Tempo necessário: {anos} anos e {meses_remainder} meses ({meses} meses)")
    print(f"Resultado: Em {meses} meses você terá R$ {historico3[-1]['saldo']:,.2f}")


def menu_testes():
    print("\n" + "="*70)
    print("EXEMPLOS E TESTES - SISTEMA DE PLANEJAMENTO FINANCEIRO")
    print("="*70)
    print("\nEssas são simulações não-interativas para demonstrar")
    print("o funcionamento de cada componente da aplicação.\n")

    print("Testes disponíveis:")
    print("1. Simulação por Período Fixo")
    print("2. Cálculo de Meta Financeira")
    print("3. Exportação para CSV")
    print("4. Tratamento de Erros")
    print("5. Casos Reais de Planejamento")
    print("6. Executar Todos os Testes")
    print("0. Voltar\n")

    while True:
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            teste_simulacao_periodo()
        elif opcao == "2":
            teste_meta_financeira()
        elif opcao == "3":
            teste_exportacao_csv()
        elif opcao == "4":
            teste_tratamento_erros()
        elif opcao == "5":
            teste_casos_reais()
        elif opcao == "6":
            teste_simulacao_periodo()
            teste_meta_financeira()
            teste_exportacao_csv()
            teste_tratamento_erros()
            teste_casos_reais()
            print("\n" + "="*70)
            print("✅ TODOS OS TESTES CONCLUÍDOS!")
            print("="*70)
            break
        elif opcao == "0":
            print("\nAtlé logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

        print("\n" + "-"*70 + "\n")
        continuar = input("Pressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    menu_testes()
