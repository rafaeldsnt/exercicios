from datetime import date
from random import randint
import calendar 

input(
    "Verificação de Acesso ao Sistema! Pressione  o botão 'Enter', para continuar ... "
)

passwordCorrect = "Python-UC01"
banidosFesta = ("Antonio","Alexandre","Marcos","Sandra","Miguel")
userSystems = {
    "nome": "",
    "newPassword":""
}

#Get a data atual
current_date = date.today()

#Aramazenando o ano atual
current_year = current_date.year


nameUsr = input("Informe o seu Nome ? ")
yearBirthday = int(input("Qual é o ano do seu aniversário ? AAAA "))
password = input("Informe a sua Senha ")

if (current_year - yearBirthday) > 18 and password == passwordCorrect:
    print("Acesso Concedido!")
else:
    print("Acesso Negado!")


input(
    "Aprovado na Faculdade?! Pressione  o botão 'Enter', para continuar ... "
)

nota_1 = input("Informe a nota na Prova Parcial ? ")
nota_2 = input("Informe a nota na Prova Final  ? ")
nota_3 = input("Informe a nota ma Prova da Especial ? ")
workExtra = input("O Aluno realizou os Trabalhos Extras ? (Sim e Não)")


media_notas = float(nota_1) + float(nota_2) + float(nota_3) / 3

#print("A média das notas é ", {media_notas:.2f})

if (media_notas >= 7 or workExtra == 'Sim'):
     print("O Aluno foi Aprovado!")
else:
    print("O Aluno foi Reprovado!")
    

input(
    "Controle de Entrada em uma Festa! Pressione  o botão 'Enter', para continuar ... "
)

nameParty = input("Informe o seu Nome ? ")
yearBirthday = int(input("Qual é o ano do seu aniversário ? AAAA "))
accompaniedparents = input(" Está acompanhado dos Pais ? (Sim e Não) ")

if (((current_year - yearBirthday) > 18 or accompaniedparents == 'Sim') and (nameParty not in banidosFesta) ):
   print("Pode participar da Festa!")
else:
    print("Não pode participar da Festa!")


input(
    " Jogo de Adivinhação! Pressione  o botão 'Enter', para continuar ... "
)

num_secret = randint(0,9)

guesses1 = int(input("Advinhe um número - Infome o primeiro numero ? "))
guesses2 = int(input("Advinhe um número - Infome o segundo numero ? "))
guesses3 = int(input("Advinhe um número - Infome o terceiro numero ? "))

if (guesses1 == num_secret or guesses2 == num_secret or guesses3 == num_secret):
    print("Você acertou !! O numero secreto é ", num_secret)
else:
    print("Você não acertou !! O numero secreto é ", num_secret)


input(
    "  Cadastro de Usuário! Pressione  o botão 'Enter', para continuar ... "
)


newUser = input("Informe o seu Nome ? ")
newPassword = input("Informe o seu Login ? ")

if (len(newUser) > 3 and len(newPassword) > 6):
    if (newPassword.index('123456') or newPassword.index('senha')):
        print("Usuário Cadastrado")
        userSystems.nome = newUser
        userSystems.newPassword = newPassword
        
        print(userSystems)
    else:
        print("A Senha criada é muito fraca!")
else:
    print("O usuário e Senha não atende as orientações de Segurança")


input(
    "  Desconto em Compras! Pressione  o botão 'Enter', para continuar ... "
)

shoppingitems = int(input("Informe a quantidade de Produtos que o Cliente Comprou ? "))
totalPurchaseprice = float(input("Informe o valor total da Compra realizada pelo Cliente "))
purchasecoupon = input("Informe o valor total da Compra realizada pelo Cliente ")


if ((shoppingitems > 5 or totalPurchaseprice > 100) and (purchasecoupon == 'Não')):
    print("O Cliente poderá receberá o desconto")
else:
    print("O Cliente não poderá receberá o desconto")
    

input(
    "  Crie um programa que ..! Pressione  o botão 'Enter', para continuar ... "
)

age = int(input("Informe a idade do passageiro ? "))

if (age > 18):
    print("O passageiro pode viajar sozinho")
    
if (age == 16 or age == 17):
    print("O passageiro pode viajar, porém é necessário ter autorização dos pais")
    parentauthorization = input("O Pai ou a Mãe autorizam a viagem do menor ? Sim - Não")
    if (parentauthorization == "Sim"):
        print("O passageiro pode viajar!!")
    else:
        print("O passageiro não pode viajar!!")
elif (age < 16):
     print("O passageiro não pode viajar sozinho!!")



input(
    "  Pode Dirigir?! Pressione  o botão 'Enter', para continuar ... "
)

agedriver = int(input("Informe a sua Idade ? "))
driverslicense = int(input(" Possui carteira de motorista ? (Sim - Não)"))

if (age >= 18 or driverslicense == "Sim"):
     print("Pode Dirigir!")
else:
     print("Não pode Dirigir!")
     

input(
    "  Login no Sistema. Pressione  o botão 'Enter', para continuar ... ")

user = input("Informe o Login do seu usuário ?")
password = input("Informe a Senha do seu usuário ? ")

if user == 'admin' and password == '1234': 
    print("Acesso permitido")
else:
    print("Acesso Negado")
    

input(" Par ou Ímpar e Positivo ou Negativo? Pressione  o botão 'Enter', para continuar ... ")

numreal = float(input("Informe um número ? "))

resultado = numreal % 2

if resultado == 0:
    print("O numero ",numreal," é par ")
else:
    print("O numero ",numreal," é impar ")
    
if (numreal > 0):
    print("O numero real é positivo ")
elif (numreal < 0):
    print("O numero real é negativo ")
    

input(" Promoção de Compras? Pressione  o botão 'Enter', para continuar ... ")
    

totalPurchase = float(input("Informe o valor total da Compra realizada pelo Cliente "))
shoppingitemstoal = int(input("Informe a quantidade de Produtos que o Cliente Comprou ? "))

if (totalPurchase > 100 or shoppingitemstoal > 5):
    print("O desconto será concedido")
else:
    print("O desconto não será concedido")
    

input(" Ano Bissexto? Pressione  o botão 'Enter', para continuar ... ")

infoYear = int(input("Informe um Ano qualquer ? "))

if (calendar.isleap(infoYear)):
    print("O ano ",infoYear," é Bissexto!" )
else:
    print("O ano ",infoYear," não é Bissexto!" )

    

input(" Autorização de Entrada em um Evento! Pressione  o botão 'Enter', para continuar ... ")

ageUser = int(input(" Qual é a sua idade ? "))
parentsControl = input(" Está acompanhada ? Sim ou Não ")

if (ageUser >= 18):
    print("Entrada Autorizada !!")
elif (ageUser in range(16, 17) and parentsControl == "Sim" ):
    print("Entrada Autorizada !! Com acompanhia do Pai ou da Mãe")
else:
     print("Entrada não Autorizada !!")
     
     



     

    
    








