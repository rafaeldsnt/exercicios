


#def apresentar(nome, idade):
#    print(f"Nome : {nome}, Idade : {idade}")


#apresentar("Alice", 30)
#apresentar(idade=30,nome="Alice")



#def saudacao(nome = "Mundo"):
#    print(f"Ola. {nome} !!")


#saudacao()
#saudacao("Alice")



#def listar_nomes(*nomes):
#    for n in nomes:
#        print(n)

#listar_nomes("Alice",2, "Charles", "Richard")


#def saudacao():
#    print("Olá do módulo !!!")


#if __name__ == "__main__":
#    saudacao()


import sys

def principal(parametros):
    for dado in parametros:
        print(dado)


def soma(numeros):
    somatorio=0
    for valor in numeros:
        somatorio = int(somatorio) + int(valor)
        
    
    print(f"o Valor da soma dos numeros é {somatorio}") 

if __name__ == "__main__":
    soma(sys.argv[1:])



