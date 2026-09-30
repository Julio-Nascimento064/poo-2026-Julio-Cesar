class Pessoa:
    def __init__(self, nome, cpf, mensalidade_base):
        self._nome = nome
        self._cpf = cpf
        self._mensalidade_base = mensalidade_base

    def calcular_pagamento(self):
        return self._mensalidade_base


class Aluno(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, nota_desempenho):
        super().__init__(nome, cpf, mensalidade_base)
        self.nota_desempenho = nota_desempenho

    def calcular_pagamento(self):
        if self.nota_desempenho >= 9.0:
            return self._mensalidade_base * 0.8
        return self._mensalidade_base


class Professor(Pessoa):
    def __init__(self, nome, cpf, mensalidade_base, horas_extras):
        super().__init__(nome, cpf, mensalidade_base)
        self.horas_extras = horas_extras

    def calcular_pagamento(self):
        return self._mensalidade_base + (self.horas_extras * 40.0)


def exibir_relatorio_financeiro(pessoa):
    print("\n--- Relatório Financeiro ---")
    print(f"Nome: {pessoa._nome}")
    print(f"CPF: {pessoa._cpf}")
    print(f"Valor final: R$ {pessoa.calcular_pagamento():.2f}")


def ler_float_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: o valor deve ser maior que zero.")
        except ValueError:
            print("Erro: digite apenas valores numéricos válidos.")


def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = input(mensagem)
            inteiro = int(valor)
            if inteiro > 0:
                return inteiro
            print("Erro: o valor deve ser um número inteiro maior que zero.")
        except ValueError:
            print("Erro: digite apenas números inteiros válidos.")


def ler_nota_desempenho(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if 0.0 <= valor <= 10.0:
                return valor
            print("Erro: a nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: digite apenas valores numéricos válidos.")


def gerar_relatorio_aluno():
    try:
        nome = input("Nome do aluno: ").strip()
        cpf = input("CPF do aluno: ").strip()
        mensalidade = ler_float_positivo("Mensalidade base do aluno: ")
        nota = ler_nota_desempenho("Nota de desempenho (0 a 10): ")

        aluno = Aluno(nome, cpf, mensalidade, nota)
        exibir_relatorio_financeiro(aluno)
        print("Relatório do aluno gerado com sucesso.")
    except Exception as erro:
        print(f"Erro ao gerar o relatório do aluno: {erro}")
    finally:
        print("Conclusão do processamento do relatório do aluno.")


def gerar_relatorio_professor():
    try:
        nome = input("Nome do professor: ").strip()
        cpf = input("CPF do professor: ").strip()
        mensalidade = ler_float_positivo("Mensalidade base do professor: ")
        horas_extras = ler_inteiro_positivo("Quantidade de horas extras: ")

        professor = Professor(nome, cpf, mensalidade, horas_extras)
        exibir_relatorio_financeiro(professor)
        print("Relatório do professor gerado com sucesso.")
    except ValueError:
        print("Erro: a quantidade de horas extras deve ser um número inteiro.")
    except Exception as erro:
        print(f"Erro ao gerar o relatório do professor: {erro}")
    finally:
        print("Conclusão do processamento do relatório do professor.")


def menu():
    while True:
        print("\n===== Sistema de Gestão Escolar =====")
        print("1 - Gerar relatório de aluno")
        print("2 - Gerar relatório de professor")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                gerar_relatorio_aluno()
            except KeyboardInterrupt:
                print("\nRelatório interrompido manualmente.")
            finally:
                print("Geração do relatório finalizada.")
        elif opcao == "2":
            try:
                gerar_relatorio_professor()
            except KeyboardInterrupt:
                print("\nRelatório interrompido manualmente.")
            finally:
                print("Geração do relatório finalizada.")
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    finally:
        print("Execução do sistema finalizada.")
