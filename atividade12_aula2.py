class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

# Função que usa polimorfismo
def fazer_barulho(animal):
    animal.fazer_som()

# Criando objetos
meu_cachorro = Cachorro()
meu_gato = Gato()

# Usando a função com diferentes objetos
fazer_barulho(meu_cachorro)  # Saída: Au Au!
fazer_barulho(meu_gato)  # Saída: Miau!