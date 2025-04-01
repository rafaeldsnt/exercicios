# Definindo uma classe chamada 'Carro'
class Carro:
    # Método construtor (__init__) para inicializar os atributos
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo
        self.ano = ano  # Atributo
        self.ligado = True  # Atributo com valor padrão

    # Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} está ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    # Método para desligar o carro
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} está desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    # Método para exibir informações do carro
    def exibir_info(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}.")

# Criando um objeto da classe Carro
#meu_carro = Carro("Toyota", "Corolla", 2020)

meu_carro = Carro("FIAT", "TORO", 2021)

# Usando métodos do objeto
meu_carro.exibir_info()  # Exibe as informações do carro
meu_carro.ligar()  # Liga o carro
meu_carro.exibir_info()  # Exibe as informações do carro novamente
meu_carro.desligar()  # Desliga o carro
meu_carro.exibir_info()  # Exibe as informações do carro novamente