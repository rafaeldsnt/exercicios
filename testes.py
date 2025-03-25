from datetime import date

import socket

banidosIPs = ("12.0.0.1","12.0.0.5","12.0.0.4","12.0.0.12","12.0.0.9")
creditrestriction = ("Antonio","Alexandre","Marcos","Sandra","Miguel")

#Get a data atual
current_date = date.today()

#Aramazenando o ano atual
current_year = current_date.year
"""
nome = "Python"

frase = 'Isso é uma String'



print(type(multilinhas))

print(nome[0])

for posicao in nome:
    print(posicao)


verdadeiro = True

falso = False

print(type(verdadeiro))
print(type(falso))

n = int(input("informe um numero entre 100 e 201! "))

if n in range(100, 201):
    print("está ..")
else:
    print("não está ")

banidosFesta = ("Antonio","Alexandre","Marcos","Sandra","Miguel")

#Get a data atual
current_date = date.today()

#Aramazenando o ano atual
current_year = current_date.year


nameParty = input("Informe o seu Nome ? ")
yearBirthday = int(input("Qual é o ano do seu aniversário ? AAAA "))
accompaniedparents = input(" Está acompanhado dos Pais ? (Sim e Não)")
banidosIPs = ("12.0.0.1","12.0.0.5","12.0.0.4","12.0.0.12","12.0.0.9")

type(banidosFesta)

print('Rafael' in banidosFesta)

if (((current_year - yearBirthday) > 18 or accompaniedparents == 'Sim') and (nameParty not in banidosFesta) ):
   print("Pode participar da Festa!")
else:
    print("Não pode participar da Festa!")
    


input("  Acesso a um Site ! Pressione  o botão 'Enter', para continuar ... ")


input("  Aguardande estamos identificando seu IP ! Pressione  o botão 'Enter', para continuar ... ")


computerIp = socket.gethostbyname(socket.gethostname())

print(computerIp)

if (computerIp not in banidosIPs):
    print("Acesso garantido")
else:
     print("Acesso Negado!")
     


input("  Pode Fazer Empréstimo?  Pressione  o botão 'Enter', para continuar ... ")

nameUserCredit = (input("Qual é o seu nome ? "))
YearBirthdayUser = int(input(" Em que ano você nasceu ? YYYYY "))
currentSalary = float(input(" Qual é a sua renda atual ? "))

print(YearBirthdayUser)
print(current_year)

print((current_year - YearBirthdayUser))

print((nameUserCredit not in creditrestriction))
print((YearBirthdayUser - current_year) > 21)
print(currentSalary >= 2000)


if ((nameUserCredit not in creditrestriction) and ((current_year - YearBirthdayUser) > 21) and currentSalary >= 2000):
    print("Pode realizar o Emprestimo!!!")
else: 
    print("Não Pode realizar o Emprestimo!!!") 
     

input("   Crie um programa que  Pergunte a temperatura  Pressione  o botão 'Enter', para continuar ... ")

currentTemperature = int(input("Qual é a temperatua Atual em Celsius ? "))

if (currentTemperature > 30):
    print("Está quente !")
elif (currentTemperature > 10 and currentTemperature <= 30):
    print("Temperatura agradável ")
elif (currentTemperature < 10):
     print("Está frio!")
else:
    print("Temperatura não registrada!!!")





input("   Maior de Três Números  Pressione  o botão 'Enter', para continuar ... ")

listNumbers = []

firstNUmber = int(input("Qual é o primeiro número ?  "))
listNumbers.append(firstNUmber)
secondNUmber = int(input("Qual é o segundo número ?  "))
listNumbers.append(secondNUmber)
thirdNUmber = int(input("Qual é o terceiro número ?  "))
listNumbers.append(thirdNUmber)

print(f"O maior dos três números é o  {max(listNumbers)}")



numbers1to20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]


input(" Imprimir Números pares e impares!  Pressione  o botão 'Enter', para continuar ... ")

for nupi in numbers1to20:
    numParorImpar =  "par" if(nupi % 2 == 0) else "impar" 
    print (f"O numero  {nupi} é  {numParorImpar}")


increment = 10

while(increment > 0):
    print(f"Número : {increment}" )
    increment = increment - 1



input(" Criar um programa que pergunta o nome até que ele digite 'sair'!  Pressione  o botão 'Enter', para continuar ... ")

nomeUserInfo = ""

while(nomeUserInfo != "sair"):
    nomeUserInfo = input(" Informe o seu nome ?")
    print(f"Nome informado {nomeUserInfo}")
    

input("Calcular o fatorial de um número usando while!  Pressione  o botão 'Enter', para continuar ... ")

numFactorial = int(input("Calculo de número fatorial. Informe um número"))
numInfo = numFactorial
result = 0

num = 1

while numFactorial >= 1:
    num = num * numFactorial
    numFactorial = numFactorial - 1

print(f"O Fatorial do numero {numInfo} é {num}")





input("Senha correta e repetição até acertar!  Pressione  o botão 'Enter', para continuar ... ")
PassCorrect = "SENHA"
question = True

while (question):
    password = input("Informe a Senha ")
    if (password == PassCorrect):
        question = False

lista_Nomes = ["Antonio","Alexandre","Marcos","Sandra","Miguel"]

for nomes in lista_Nomes:
    print(f"Nome na lista de nomes {nomes}")



numbers1to20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]

input("Imprimir os números de 1 a 20 e verificar se são múltiplos de 3 ou 5.!  Pressione  o botão 'Enter', para continuar ... ")

for num in numbers1to20:
    if num%3 == 0 and num%5 == 0:
        print(f"O numero {num}  é multiplo de 3 e 5")
    elif num%3 == 0:
        print(f"O numero {num}  é multiplo de 3")
    elif num%5 == 0:
        print(f"O numero {num}  é multiplo de 5")
        


input(" Criar um programa que peça ao usuário para digitar uma sequência de números até que ele digite um número maior que 100!  Pressione  o botão 'Enter', para continuar ... ")

inputNum = True
lista_Numeros = []

while (inputNum):
    numDigit = int(input("Criar um programa que peça ao usuário para digitar uma sequência de números até que ele digite um número maior que 100!. Informe um numero ? "))
    if(numDigit < 100):
        lista_Numeros.append(numDigit)
        print(f"A quantidade numeros informados é {len(lista_Numeros)}")
    else:
        inputNum = False 

print(f"A quantidade numeros informados é {len(lista_Numeros)}")


input("Imprimir o somatório de todos os números pares de 1 a 100.!  Pressione  o botão 'Enter', para continuar ... ")

numSerie = 1
numPar = 0

while (numSerie < 100):
    if ((numSerie % 2) == 0):
        numPar = numPar + numSerie
    numSerie = numSerie + 1

print(f"O Somatório dos números pares de 1 a 100 é : {numPar} ")


 
    
input("Contagem regressiva!  Pressione  o botão 'Enter', para continuar ... ")

intRange = 10

for intRange in range(10, -1,-1):
    print(f"Contagem regressiva ... {intRange}")
    sleep(1)
    
    


#numbers1to10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lista_compras = ["arroz", "feijão", "macarrão", "farinha", "óleo", "açúcar", "sal", "leite", "queijo", "manteiga", "frutas", "legumes", "verduras"]




input("  Sequência de Fibonacci!  Pressione  o botão 'Enter', para continuar ... ")

number_fibo =int( input(" Digite Quantos termos você deseja :"))

a = 0
b = 1
prox_i = b  
cont = 1

while cont <= number_fibo:
    print(prox_i, end=" ")
    cont += 1
    a, b = b, prox_i
    prox_i = a + b
    
""" 
    
