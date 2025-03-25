from time import sleep 
import random 

lista_Nomes = ["Antonio","Alexandre","Marcos","Sandra","Miguel"]

lista_compras = ["arroz", "feijão", "macarrão", "farinha", "óleo", "açúcar", "sal", "leite", "queijo", "manteiga", "frutas", "legumes", "verduras"]


input("   Imprimir números!  Pressione  o botão 'Enter', para continuar ... ")


numbers1to10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1to20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]

for nu in numbers1to10:
    print(nu)
    

input(" Imprimir Números pares e impares!  Pressione  o botão 'Enter', para continuar ... ")


for nupi in numbers1to20:
    numParorImpar =  "par" if(nupi % 2 == 0) else "impar" 
    print (f"O numero  {nupi} é  {numParorImpar}")
    

input(" Imprimir de 10 até 1!  Pressione  o botão 'Enter', para continuar ... ")

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

numFactorial = int(input("Calculo de número fatorial. Informe um número .."))
numInfo = numFactorial

num = 1

while numFactorial >= 1:
    num = num * numFactorial
    numFactorial = numFactorial - 1

print(f"O Fatorial do numero {numInfo} é {num}")


input("Soma de números positivos!  Pressione  o botão 'Enter', para continuar ... ")
resultSum = 0

while (num >  0):
    num = int(input("Calculo de número fatorial. Informe um número")) 
    resultSum = resultSum + num
      

print(f"A Soma dos numeros foi {resultSum}")



input("Soma de números positivos!  Pressione  o botão 'Enter', para continuar ... ")
resultSum = 0
num = 0
question = True

while (question):
    num = int(input("Calculo de número fatorial. Informe um número")) 
    if (num > 0):
        resultSum = resultSum + num
    else:
        question = False
      

print(f"A Soma dos numeros foi {resultSum}")

input(" Tabela de multiplicação de um número (de 1 a 10)!  Pressione  o botão 'Enter', para continuar ... ")

numFactor = int(input("Tabela de multiplicação. Informe um número: ")) 

indice = 0

while (indice <= 10):
    print(f"{numFactor} x {indice} = {indice*numFactor}" )
    indice = indice + 1
      

input("Senha correta e repetição até acertar!  Pressione  o botão 'Enter', para continuar ... ")
PassCorrect = "SENHA"
question = True

while (question):
    password = input("Informe a Senha ")
    if (password == PassCorrect):
        question = False

input(" Imprimir uma lista de nomes!  Pressione  o botão 'Enter', para continuar ... ")

for nomes in lista_Nomes:
    print(f"Nome na lista de nomes {nomes}")
    

input("  Imprimir uma sequência de números e seus cubos!  Pressione  o botão 'Enter', para continuar ... ")
question = True
mum = 1

while (question):
    numCubo = int(input(" Imprimir uma sequência de números e seus cubos. Informe um numero ? "))
    if numCubo >= 1 :
        print(f"O cubo do numero do numero {numCubo} é {pow({numCubo},3)}")
        question = True
    else:
        question = False


input("Imprimir uma sequência de números e seus cubos!  Pressione  o botão 'Enter', para continuar ... ")

numCubo = int(input(" Imprimir uma sequência de números e seus cubos. Informe um numero ? "))
mum = 1

while (mum <= numCubo ):  
        print(f"O cubo do numero do numero {mum} é  {pow(mum,3)}")
        mum = mum + 1  


input(" Imprimir uma tabela de multiplicação (aninhando loops)!  Pressione  o botão 'Enter', para continuar ... ")

numFactor = 0
indice = 0

while (numFactor < 10):
    indice = 0
    numFactor = numFactor + 1
    while (indice <= 10):
        print(f"{numFactor} x {indice} =  {numFactor * indice}")
        indice = indice + 1
        

input("Contando o número de dígitos em um número!  Pressione  o botão 'Enter', para continuar ... ")

numDigit = int(input(" Contando o número de dígitos em um número. Informe um numero ? "))

print(len(str(numDigit)))


input("Imprimir os números de 1 a 20 e verificar se são múltiplos de 3 ou 5.!  Pressione  o botão 'Enter', para continuar ... ")

for num in numbers1to20:
    if num%3 == 0 and num%5 == 0:
        print(f"O numero {num}  é multiplo de 3 e 5")
    elif num%3 == 0:
        print(f"O numero {num}  é multiplo de 3")
    elif num%5 == 0:
        print(f"O numero {num}  é multiplo de 5")
        

input("Criar um programa que imprima uma tabela de multiplicação de 1 a 5 (sem usar o range).!  Pressione  o botão 'Enter', para continuar ... ")

numFactor = 0
indice = 0

while (numFactor < 5):
    indice = 0
    numFactor = numFactor + 1
    while (indice <= 10):
        print(f"{numFactor} x {indice} =  {numFactor * indice}")
        indice = indice + 1


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


input("Imprimir o somatório de todos os números pares de 1 a 100.!  Pressione  o botão 'Enter', para continuar ... ")

numSerie = 1
numPar = 0

while (numSerie < 100):
    if ((numSerie % 2) == 0):
        numPar = numPar + numSerie
    numSerie = numSerie + 1

print(f"O Somatório dos números pares de 1 a 100 é : {numPar} ")


input("Contagem regressiva!  Pressione  o botão 'Enter', para continuar ... ")

for intRange in range(10, -1,-1):
    print(f"Contagem regressiva ... {intRange}")
    sleep(1)



input("Soma de números até que o usuário digite 0.!  Pressione  o botão 'Enter', para continuar ... ")
resultSum = 0
num = 0
question = True

while (question):
    num = int(input("Calculo de número. Informe um número ")) 
    if (num > 0):
        resultSum = resultSum + num
    else:
        question = False
      

print(f"A Soma dos numeros foi {resultSum}")



input(" Tabuada!  Pressione  o botão 'Enter', para continuar ... ")

indice_fat = int(input("Informe um número para o calculo da Tabuada ")) 


for num in numbers1to10:
    print (f"{indice_fat} x {num} = {indice_fat * num}")
    


input(" Números  pares de 1 a 20!  Pressione  o botão 'Enter', para continuar ... ")


for numPare in numbers1to20:
    if(numPare % 2 == 0):
        print (f"O numero {numPare} é par")



input(" Adivinhe o número!  Pressione  o botão 'Enter', para continuar ... ")

FindNumber = False
secretNumber = random.choice(numbers1to10)
#print(secretNumber)

while(not FindNumber):
    number_info = int(input("Adivinhe o número !! Informe um numero : ")) 
    if (secretNumber == number_info):
        FindNumber = True
        input(f" Parabéns você encontrou o numero secreto  {secretNumber}")
        break
    

input(" Fatorial usanfo um for!  Pressione  o botão 'Enter', para continuar ... ")

number_fatorial = int(input(" Informe um numero para calculo Fatorial : "))

fat = 1
for i in range(number_fatorial,0,-1):
    print(i)
    fat = fat * i
    print(f"{fat}")
    
    
print(f"O Fatorial do {fat}")


input(" Lista de compras!  Pressione  o botão 'Enter', para continuar ... ")

for item in lista_compras:
    print(f" Item de compra :  {item}")



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
    

input(" Menu interativo!  Pressione  o botão 'Enter', para continuar ... ")
lista_menu = []
question = True

while (question):
    item_menu = input("Acrescente o item de menu ")
    if (item_menu != "sair"):
        lista_menu.append(item_menu)
        print("Veja o menu")
        for item_menu in lista_menu:
            print(f"Item de menu {item_menu}")

    else:
        question = False

input("Menu Completo!  Pressione  o botão 'Enter', para continuar ...")
for item_menupx in lista_menu:
    print(f"Item de menu : {item_menupx}")