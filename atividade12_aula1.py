class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")


class Carro(Veiculo):
    def __init__ (self,marca,modelo,ano,portas,cor, placa):
        super().__init__(marca,modelo,ano)
        self.portas = portas
        self.cor = cor
        self.placa = placa

    def exibir_info(self):
        super().exibir_info()
        print(f"Este carro tem {self.portas} portas e possui a cor {self.cor} com a placa {self.placa}")


meu_carro = Carro("Toyota", "Corolla", 2024, 4, "azul", "KII125")
meu_carro.exibir_info()