class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self):
        return self.salario_base * 0.05


class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_bonus(self):
        return super().calcular_bonus() + 1000.00

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas

    def calcular_bonus(self):
        return self.total_vendas * 0.10


# --- ÁREA DE TESTES ---

# 1. Instanciando os objetos
f1 = Funcionario("Carlos", 2000.00)
g1 = Gerente("Ana", 3000.00)
v1 = Vendedor("João", 2000.00, 15000.00)

# 2. Imprimindo os resultados
print("=== TESTE DE BÔNUS ===")
print(f"Bônus de {f1.nome} (Funcionário): R$ {f1.calcular_bonus():.2f}")
print(f"Bônus de {g1.nome} (Gerente):     R$ {g1.calcular_bonus():.2f}")
print(f"Bônus de {v1.nome} (Vendedor):    R$ {v1.calcular_bonus():.2f}")