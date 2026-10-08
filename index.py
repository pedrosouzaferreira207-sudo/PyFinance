import csv
from typing import List, Tuple, Dict
from datetime import datetime


def validar_numero_positivo(mensagem: str, tipo: str = "float") -> float | int:
    while True:
        try:
            valor = input(mensagem).strip()

            if not valor:
                print("❌ Erro: Por favor, digite um valor válido.")
                continue

            if tipo == "int":
                numero = int(valor)
            else:
                numero = float(valor)

            if numero <= 0:
                print("❌ Erro: O valor deve ser positivo (maior que 0).")
                continue

            return numero

        except ValueError:
            print(f"❌ Erro: Digite um número válido (sem letras ou caracteres especiais).")


def simular_por_periodo(
    valor_inicial: float,
    aporte_mensal: float,
    taxa_juros: float,
    meses: int
) -> List[Dict[str, float | int]]:
    historico = []
    saldo = valor_inicial
    taxa_decimal = taxa_juros / 100

    historico.append({
        "mes": 0,
        "aporte": 0,
        "rendimento": 0,
        "saldo": round(saldo, 2)
    })

    for mes in range(1, meses + 1):
        rendimento = saldo * taxa_decimal
        saldo += rendimento
        saldo += aporte_mensal

        historico.append({
            "mes": mes,
            "aporte": round(aporte_mensal, 2),
            "rendimento": round(rendimento, 2),
            "saldo": round(saldo, 2)
        })

    return historico


def calcular_meta_financeira(
    valor_inicial: float,
    aporte_mensal: float,
    taxa_juros: float,
    meta: float
) -> Tuple[int, List[Dict[str, float | int]]]:
    historico = []
    saldo = valor_inicial
    taxa_decimal = taxa_juros / 100
    mes = 0

    historico.append({
        "mes": 0,
        "aporte": 0,
        "rendimento": 0,
        "saldo": round(saldo, 2)
    })

    if saldo >= meta:
        return 0, historico

    while saldo < meta and mes < 1200:
        mes += 1

        rendimento = saldo * taxa_decimal
        saldo += rendimento
        saldo += aporte_mensal

        historico.append({
            "mes": mes,
            "aporte": round(aporte_mensal, 2),
            "rendimento": round(rendimento, 2),
            "saldo": round(saldo, 2)
        })

    if mes >= 1200:
        print("\n⚠️  Aviso: Não foi possível atingir a meta em 1200 meses (100 anos).")
        print("Verifique se os parâmetros estão corretos.")

    return mes, historico


def exibir_historico(historico: List[Dict[str, float | int]]) -> None:
    print("\n" + "=" * 70)
    print(f"{'Mês':<6} {'Aporte':<15} {'Rendimento':<15} {'Saldo':<15}")
    print("-" * 70)

    for linha in historico:
        print(
            f"{linha['mes']:<6} "
            f"R$ {linha['aporte']:<13,.2f} "
            f"R$ {linha['rendimento']:<13,.2f} "
            f"R$ {linha['saldo']:<13,.2f}"
        )

    print("=" * 70)


def exportar_csv(
    historico: List[Dict[str, float | int]],
    nome_arquivo: str,
    tipo_simulacao: str,
    parametros: Dict
) -> bool:
    try:
        if not nome_arquivo.strip():
            print("❌ Erro: Nome de arquivo inválido.")
            return False

        nome_arquivo = "".join(c for c in nome_arquivo if c not in '<>:"|?*')
        caminho_arquivo = f"{nome_arquivo}.csv"

        with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)

            writer.writerow(["SIMULAÇÃO DE PLANEJAMENTO FINANCEIRO"])
            writer.writerow([f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"])
            writer.writerow([f"Tipo de Simulação: {tipo_simulacao}"])
            writer.writerow([])

            writer.writerow(["PARÂMETROS DA SIMULAÇÃO"])
            for chave, valor in parametros.items():
                writer.writerow([chave, valor])
            writer.writerow([])

            writer.writerow(["HISTÓRICO MENSAL"])
            writer.writerow(["Mês", "Aporte (R$)", "Rendimento (R$)", "Saldo (R$)"])

            for linha in historico:
                writer.writerow([
                    linha["mes"],
                    f"{linha['aporte']:.2f}",
                    f"{linha['rendimento']:.2f}",
                    f"{linha['saldo']:.2f}"
                ])

            writer.writerow([])
            writer.writerow(["RESUMO FINAL"])
            saldo_final = historico[-1]["saldo"]
            saldo_inicial = historico[0]["saldo"]
            ganho_total = saldo_final - saldo_inicial

            writer.writerow(["Saldo Inicial (R$)", f"{saldo_inicial:.2f}"])
            writer.writerow(["Saldo Final (R$)", f"{saldo_final:.2f}"])
            writer.writerow(["Ganho Total (R$)", f"{ganho_total:.2f}"])

        print(f"\n✅ Arquivo '{caminho_arquivo}' exportado com sucesso!")
        return True

    except Exception as erro:
        print(f"\n❌ Erro ao exportar arquivo: {erro}")
        return False


def menu_principal() -> None:
    print("\n" + "=" * 70)
    print(" " * 15 + "SISTEMA DE PLANEJAMENTO FINANCEIRO")
    print("=" * 70)

    historico_simulacoes = []

    while True:
        print("\n📋 MENU PRINCIPAL")
        print("-" * 70)
        print("1. Simulação por Período Fixo")
        print("2. Cálculo de Meta Financeira")
        print("3. Sair (e salvar dados)")
        print("-" * 70)

        try:
            opcao = input("\nEscolha uma opção (1, 2 ou 3): ").strip()

            if opcao == "1":
                opcao1_simulacao_periodo(historico_simulacoes)

            elif opcao == "2":
                opcao2_meta_financeira(historico_simulacoes)

            elif opcao == "3":
                opcao3_sair(historico_simulacoes)
                break

            else:
                print("❌ Opção inválida. Digite 1, 2 ou 3.")

        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrompido pelo usuário.")
            opcao3_sair(historico_simulacoes)
            break

        except Exception as erro:
            print(f"❌ Erro inesperado: {erro}")


def opcao1_simulacao_periodo(historico_simulacoes: List) -> None:
    print("\n" + "=" * 70)
    print("OPÇÃO 1: SIMULAÇÃO POR PERÍODO FIXO")
    print("=" * 70)

    try:
        valor_inicial = validar_numero_positivo("\nDigite o valor inicial (R$): ", tipo="float")
        aporte_mensal = validar_numero_positivo("Digite o aporte mensal (R$): ", tipo="float")
        taxa_juros = validar_numero_positivo("Digite a taxa de juros mensal (%): ", tipo="float")
        meses = validar_numero_positivo("Digite o número de meses: ", tipo="int")

        print("\n⏳ Processando simulação...")
        historico = simular_por_periodo(valor_inicial, aporte_mensal, taxa_juros, meses)

        exibir_historico(historico)

        saldo_inicial = historico[0]["saldo"]
        saldo_final = historico[-1]["saldo"]
        ganho_total = saldo_final - saldo_inicial

        print(f"\n📊 RESUMO:")
        print(f"   Saldo Inicial: R$ {saldo_inicial:,.2f}")
        print(f"   Saldo Final: R$ {saldo_final:,.2f}")
        print(f"   Ganho Total: R$ {ganho_total:,.2f}")

        historico_simulacoes.append({
            "tipo": "período",
            "historico": historico,
            "parametros": {
                "Valor Inicial (R$)": f"{valor_inicial:.2f}",
                "Aporte Mensal (R$)": f"{aporte_mensal:.2f}",
                "Taxa de Juros (%)": f"{taxa_juros:.2f}",
                "Período (meses)": meses
            }
        })

    except Exception as erro:
        print(f"\n❌ Erro na simulação: {erro}")


def opcao2_meta_financeira(historico_simulacoes: List) -> None:
    print("\n" + "=" * 70)
    print("OPÇÃO 2: CÁLCULO DE META FINANCEIRA")
    print("=" * 70)

    try:
        valor_inicial = validar_numero_positivo("\nDigite o valor inicial (R$): ", tipo="float")
        aporte_mensal = validar_numero_positivo("Digite o aporte mensal (R$): ", tipo="float")
        taxa_juros = validar_numero_positivo("Digite a taxa de juros mensal (%): ", tipo="float")
        meta = validar_numero_positivo("Digite o valor da meta financeira (R$): ", tipo="float")

        if meta <= valor_inicial:
            print("⚠️  Aviso: A meta é menor ou igual ao valor inicial.")
            print("   A meta já foi atingida!")
            meses = 0
            historico = [{
                "mes": 0,
                "aporte": 0,
                "rendimento": 0,
                "saldo": round(valor_inicial, 2)
            }]
        else:
            print("\n⏳ Processando cálculo de meta...")
            meses, historico = calcular_meta_financeira(
                valor_inicial, aporte_mensal, taxa_juros, meta
            )

        exibir_historico(historico)

        saldo_final = historico[-1]["saldo"]

        if meses > 0:
            anos = meses // 12
            meses_restantes = meses % 12
            print(f"\n📊 RESULTADO:")
            print(f"   Tempo necessário: {meses} meses ({anos} ano(s) e {meses_restantes} mês/meses)")
            print(f"   Saldo atingido: R$ {saldo_final:,.2f}")
        else:
            print(f"\n📊 RESULTADO:")
            print(f"   Meta já atingida no início!")
            print(f"   Saldo atual: R$ {saldo_final:,.2f}")

        historico_simulacoes.append({
            "tipo": "meta",
            "historico": historico,
            "parametros": {
                "Valor Inicial (R$)": f"{valor_inicial:.2f}",
                "Aporte Mensal (R$)": f"{aporte_mensal:.2f}",
                "Taxa de Juros (%)": f"{taxa_juros:.2f}",
                "Meta Financeira (R$)": f"{meta:.2f}",
                "Meses para Atingir a Meta": meses
            }
        })

    except Exception as erro:
        print(f"\n❌ Erro no cálculo: {erro}")


def opcao3_sair(historico_simulacoes: List) -> None:
    print("\n" + "=" * 70)
    print("OPÇÃO 3: SAIR")
    print("=" * 70)

    if not historico_simulacoes:
        print("\n✅ Nenhuma simulação foi realizada.")
        print("Programa encerrado.")
        return

    print(f"\n📊 Total de simulações realizadas: {len(historico_simulacoes)}")

    salvar = input("\nDeseja salvar os dados em um arquivo CSV? (s/n): ").strip().lower()

    if salvar == "s":
        nome_arquivo = input("Digite o nome do arquivo (sem .csv): ").strip()

        if nome_arquivo:
            historico_completo = []
            parametros_completos = {}

            for idx, simulacao in enumerate(historico_simulacoes, 1):
                if idx > 1:
                    historico_completo.append({
                        "mes": "-",
                        "aporte": "-",
                        "rendimento": "-",
                        "saldo": "-"
                    })

                tipo = simulacao["tipo"].upper()
                historico_completo.append({
                    "mes": f"--- SIMULAÇÃO {idx}: {tipo} ---",
                    "aporte": "-",
                    "rendimento": "-",
                    "saldo": "-"
                })

                historico_completo.extend(simulacao["historico"])
                parametros_completos[f"Simulação {idx}"] = tipo

            tipo_sim = (
                "Combinado (Período + Meta)"
                if len(set(s["tipo"] for s in historico_simulacoes)) > 1
                else historico_simulacoes[0]["tipo"].capitalize()
            )

            exportar_csv(
                historico_completo,
                nome_arquivo,
                tipo_sim,
                parametros_completos
            )
        else:
            print("❌ Nome de arquivo inválido.")

    print("\n✅ Programa encerrado.")


def main() -> None:
    menu_principal()


if __name__ == "__main__":
    main()
