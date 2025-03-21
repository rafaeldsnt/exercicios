

#Atribuição de Variáveis


print("Atribuição de Variáveis")   


print("Item 1")

Idade = 5
print("Minha idade é  ",Idade) 

input("Pressione  o botão 'Enter', para continuar ... ") 

print("Atribuição de Variáveis")

print("Item 2")

nome = "Rafael"

print("Meu nome é  ",nome) 

input("Pressione  o botão 'Enter', para continuar ... ") 

print(chr(27) + "[2J")

#Operações Aritméticas com Variáveis


print("Operações Aritméticas com Variáveis")



a = 4
b = 5

print("Variáveis atribuídas -> A é ", a ," -> B é " ,b)

print("Soma", a + b)
print("Subtração", a - b)
print("Muliplicação", a * b)
print("Divisão", a / b)

print("Novos Valores")

a = 5
b = 96

print("Novo valores -> variáveis atribuídas -> A é ", a ," -> B é " ,b)

print("Soma", a + b)
print("Subtração", a - b)
print("Muliplicação", a * b)
print("Divisão", a / b)

input("Pressione  o botão 'Enter', para continuar ... ") 

#Manipulação de Strings

print("Manipulação de Strings")

nome_com_idade = "A professora Ana Maria tem 35 anos. Tem olhos castanhos e seu cabelo é preto e curto. Usa óculos para ver de perto e carrega sempre dois livros em uma bolsa vermelha com alças"

print("String utilizada como referência ", nome_com_idade)  

print("O tamanho da string é  ",len(nome_com_idade))

nome_completo = "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu"

print((nome_completo).upper())


input("Pressione  o botão 'Enter', para continuar ... ") 

print("Entrada de Dados")

nome_inf = input("Qual é o seu nome ? ")
idade_inf = input("Qual é a sua Idade ? ")

print(" Olá ", nome_inf, "! Você tem ", idade_inf, "anos.")

input("Pressione  o botão 'Enter', para continuar ... ") 

print("Desafio da Troca de Variáveis")

p = 4
t = 9

x = p
b = t

print("Imprimindo a variavel p",p)
print("Imprimindo a variavel t",t)

print("Imprimindo a variavel x",x)
print("Imprimindo a variavel b",t)

resultado = "Iguais" if x == p else "Diferentes"

print("A variável p tem que ser igual a x. Elas são", resultado)

resultado2 = "Iguais" if b == x else "Diferentes"

print("A variável b tem que ser igual a t. Elas são", resultado2)


input("Pressione  o botão 'Enter', para continuar ... ") 

print("Cálculo da Área de um Retângulo")


largura = input("Informe a largura do triângulo ")
altura  = input("Informe a altura do triângulo ")

resultado_triangulo = (int(largura) * int(altura)) / 2 

print("A área do retângulo é:", (int(largura) * int(altura)) / 2 )

input("Pressione  o botão 'Enter', para continuar ... ") 

print("Calculando o Perímetro de um Quadrado")

largura = input("Informe o valor de um lado do quadrado ")

print("A área do retângulo é:", ( int(largura) * 4 ))

input("Pressione  o botão 'Enter', para continuar ... ") 

print("Aumentando o Salário")

salario = input("Informe o valor do seu salario ")

salario_resultado = ((int(salario) / 100) * 10) + int(salario)

print("Seu novo salário será de", salario_resultado,". Foi dado 10% de aumento")

print(" == Fim do Desafio == ")





