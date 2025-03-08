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
    print("A idade do usuário é maior ou igual que 16 anos")
else:
     print("A idade do usuário é menor que 16 anos")

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





