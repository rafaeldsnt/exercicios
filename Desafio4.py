input(
    "positivo, negativo ou zero -  Peça ao usuário um número e diga se ele é positivo, negativo ou zero! Pressione  o botão 'Enter', para continuar ... "
)

num1 = int(input("Informe um numero qualquer ? "))

if num1 > 0:
    print("O numero é positivo")
elif num1 < 0:
     print("O numero é negativo")
else:
    print("O numero é zero")

input("Pressione  o botão 'Enter', para continuar ... ")



input(
    "Solicite ao usuário sua idade e informe se ele pode votar (maior ou igual a 16 anos)! Pressione  o botão 'Enter', para continuar ... "
)

idade = int(input("Qual é a sua Idade ? "))

if idade >= 16:
    print("A idade do usuário é maior ou igual que 16 anos. Já pode Votar!")
else:
     print("A idade do usuário é menor que 16 anos. Não pode Votar!")

input("Pressione  o botão 'Enter', para continuar ... ")


input(
    "Peça dois números ao usuário e exiba o maior deles! Pressione  o botão 'Enter', para continuar ... ")

num1 = input("Informe o primeiro numero ? ")
num2 = input("Informe o segundo  numero ? ")

if num1 > num2:
    maiorNum = num1
else:
    maiorNum = num2

print("O Maior numero é ",maiorNum)


input(
    " Faça um programa que peça um número e diga se ele é par ou ímpar.! Pressione  o botão 'Enter', para continuar ... ")


num = float(input("Informe o primeiro numero ? "))

resultado = num % 2

if resultado == 0:
    print("O numero ",num," é par ")
else:
    print("O numero ",num," é impar ")
    
    
    
input(
    " Crie um programa que peça um nome de usuário e uma senha. Se o nome for 'admin' e a senha '1234', mostre 'Acesso permitido'. Caso contrário, 'Acesso negado'! Pressione  o botão 'Enter', para continuar ... ")


user = input("Informe o Login do seu usuário ?")
password = input("Informe a Senha do seu usuário ? ")



if user == 'admin' and password == '1234': 
    print("Acesso permitido")
else:
    print("Acesso Negado")
    

    
input(
    " Peça ao usuário um número e verifique se ele está entre 10 e 50. Pressione  o botão 'Enter', para continuar ... ")


numBetween10and50 = int(input("Informe num numero ? "))

if numBetween10and50 in range(10, 50):
    print("O numero", num, "está entre 10 e 50")
else:
    print("O numero", num, " não está entre 10 e 50")
    

input(
    "Desenvolva um programa que calcule o IMC de uma pessoa e exiba sua classificação! Pressione  o botão 'Enter', para continuar ... "
)

peso_usr = input("Informe seu peso ? ")
altura_usr = input("Informe sua altura ? ")
mensage = "Você está: "

valor_IMC = float(peso_usr) / pow(float(altura_usr), 2)

print("O valor do IMC é  ", valor_IMC)

if valor_IMC < 18.5:
     print(mensage + "Abaixo do peso")
elif valor_IMC in range(18.5, 24.9) :
     print(mensage + "com o Peso ideal")
elif valor_IMC in range(25, 29.9):
     print(mensage + "com Sobrepeso")
elif valor_IMC > 30:
     print(mensage + "com Obesidade")


input(
    "Peça três números ao usuário e verifique se eles podem formar um triângulo! Pressione  o botão 'Enter', para continuar ... "
)

num1 = int(input("Informe o primeiro numero (primeiro lado) ? "))
num2 = int(input("Informe o segundo numer (segundo lado)  ? "))
num3 = int(input("Informe o terceiro numero (base lado) ? "))

if (num1 + num2) > num3: 
    print("Os numeros podem formar um triângulo")
else: 
    print("Os numeros não podem formar um triângulo")
    

input(
    "Crie um programa que peça ao usuário uma temperatura em Celsius e informe se ele está em um clima! Pressione  o botão 'Enter', para continuar ... "
)

num1 = float(input("Qual é a Temperatura atual em Celsius ? "))

if 0 > num1: 
      print("Muito frio!")
elif num1 in range(1, 20):
      print("Clima agradável!")
else:
      print("Calorão!")
      
      
input(
    "Desafio Final: Simulador de Descontos! Pressione  o botão 'Enter', para continuar ... "
)
    
valorTotalcompra = float(input("Qual foi o valor da sua compra ? "))


if valorTotalcompra > 200:
    valor_Desconto = float(valorTotalcompra) * 0.05
    print("O valor do desconto é  R$ ", (valor_Desconto))

    print(
    "O valor da compra com o desconto é R$ ",
    (float(valorTotalcompra) - float(valor_Desconto)),
    )
elif valorTotalcompra > 500: 
    valor_Desconto = float(valorTotalcompra) * 0.15
    print("O valor do desconto é  R$ ", (valor_Desconto))

    print(
    "O valor da compra com o desconto é R$ ",
    (float(valorTotalcompra) - float(valor_Desconto)),
    )
elif valorTotalcompra > 200 and valorTotalcompra < 500:
     valor_Desconto = float(valorTotalcompra) * 0.1
     print("O valor do desconto é  R$ ", (valor_Desconto))

     print(
     "O valor da compra com o desconto é R$ ",
     (float(valorTotalcompra) - float(valor_Desconto)),
     )
else:
    print("Sua compra está fora o range de Descontos!!!")
    
    
input(
    "Desafio Extra! E se quisermos que o programa também aconselhe o usuário sobre como se vestir? Pressione  o botão 'Enter', para continuar ... "
)

num1 = float(input("Qual é a Temperatura atual em Celsius ? "))

if 0 > num: 
      print("Use roupas térmicas e se mantenha aquecido!")
elif num > 0 and num < 20: 
      print("Beba bastante água e use roupas leves!")
else:
      print("Calorão! Tome Cuidado!!! Beba bastente água e ande na sombra! ")
      




   
    




















    



