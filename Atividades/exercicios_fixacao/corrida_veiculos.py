from abc import ABC, abstractmethod

# 1. Classe Abstrata / Interface
class Veiculo(ABC):
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

# 2. Subclasses
class Carro(Veiculo):
    def acelerar(self):
        print(f"O carro {self.modelo} acelera: Vroom! Ganhou velocidade rapidamente.")

class Moto(Veiculo):
    def acelerar(self):
        print(f"A moto {self.modelo} acelera: Randandandan! Ultrapassando pelo corredor.")

class Caminhao(Veiculo):
    def acelerar(self):
        print(f"O caminhão {self.modelo} acelera: VRRRRR! Retomando força com carga máxima.")

# 4. Desafio de Aprofundamento (Bônus)
class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"O carro elétrico {self.modelo} acelera: *Zunido sutil*... Torque instantâneo!")

# 3. Execução Polimórfica (Simulação de Corrida)
pista_de_corrida = [
    Carro("Civic Type R"),
    Moto("Yamaha MT-07"),
    Caminhao("Volvo FH 540"),
    CarroEletrico("Tesla Model S")  # Classe bônus adicionada à lista
]

print("--- INÍCIO DA CORRIDA ---")
for veiculo in pista_de_corrida:
    veiculo.acelerar()