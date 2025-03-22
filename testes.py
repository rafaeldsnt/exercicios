from datetime import date

nome = "Python"

frase = 'Isso é uma String'

multilinhas = "" "Isso é uma string de multiplas linhas"""

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

type(banidosFesta)

print('Rafael' in banidosFesta)

if (((current_year - yearBirthday) > 18 or accompaniedparents == 'Sim') and (nameParty not in banidosFesta) ):
   print("Pode participar da Festa!")
else:
    print("Não pode participar da Festa!")