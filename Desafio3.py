# Import math Library
import math

input("Calculadora básica - Informe dois numeros inteiros para o sistema realizar as operações básicas! Pressione  o botão 'Enter', para continuar ... ")

num1 = input("Informe o primeiro numero ? ")
num2 = input("Informe o segundo  numero ? ")

print("Variáveis atribuídas -> primeiro é ", num1 ," -> segundo é " ,num2)

print("Soma", int(num1) + int(num2))
print("Subtração", int(num1)  - int(num2))
print("Muliplicação", int(num1) * int(num2))
print("Divisão", int(num1) / int(num2))

input("Pressione  o botão 'Enter', para continuar ... ")  

input("Média de notas - Informe três notas para calcularmos a média aritmética! Pressione  o botão 'Enter', para continuar ... ")

nota_1 = input("Informe a primeira nota ? ")
nota_2 = input("Informe a segunda nota  ? ")
nota_3 = input("Informe a terceira nota ? ")


media_notas = (float(nota_1) + float(nota_2) + float(nota_3) / 3)

print("A média das notas é  ", media_notas)

input("Pressione  o botão 'Enter', para continuar ... ")

input("Conversor de temperatura - Conversão de temperatura de Celsius para Fahrenheit! Pressione  o botão 'Enter', para continuar ... ")

temperatura_C = input("Informe a temperatura em Celsius para conversão ? ")

valor_Fahrenheit = ( float(temperatura_C) * 1.8 ) + 32

print("O Valor de",float(temperatura_C), "Celsius convertido em Fahrenheit é ", valor_Fahrenheit )

input("Pressione  o botão 'Enter', para continuar ... ")

input("Área de um círculo - Calculo da area de um círculo! Pressione  o botão 'Enter', para continuar ... ")

raio_circulo = input("Informe o raio de um circulo ? ")

valor_raioCirculo = (  math.pi * pow(float(raio_circulo),2) )

print("O valor da area do círculo é ", valor_raioCirculo )

input("Pressione  o botão 'Enter', para continuar ... ") 

input("Calculadora de IMC - Calculo do IMC! Pressione  o botão 'Enter', para continuar ... ")

peso_usr= input("Informe seu peso ? ")
altura_usr= input("Informe sua altura (em cm) ? ")

valor_IMC = ( float(peso_usr) / pow(float(altura_usr),2) )

print("O valor do IMC é  ", valor_IMC )

input("Pressione  o botão 'Enter', para continuar ... ")

input("Desconto em compras - Calculo do valor final de uma compra com um desconto de 10%! Pressione  o botão 'Enter', para continuar ... ")

valorTotalcompra= input("Informe p valor total da Compra ? ")

valor_Desconto = ( float(valorTotalcompra) * 0.1)

print("O valor do desconto é  R$ ", (valor_Desconto)  )

print("O valor da compra com o desconto é R$ ", ( float(valorTotalcompra) - float(valor_Desconto)) )

input("Pressione  o botão 'Enter', para continuar ... ")


input("Tempo de viagem - Calculo de tempo de viagem! Pressione  o botão 'Enter', para continuar ... ")

valorDistancia= input("Qual é a distância da viagem ? ")
valorVelocidade= input("Informe a velocidade média  ?")

valor_Tempo = ( float(valorDistancia) / float(valorVelocidade))

print("O tempo necessário é ", valor_Tempo  )

input("Pressione  o botão 'Enter', para continuar ... ")


input("Juros simples- Calculo do montante final de um investimento com juros simples! Pressione  o botão 'Enter', para continuar ... ")

valorInicial = input("QUal é o valor inicial de investimentos ? ")
valortxJuros= input("Informe a taxa de Juros ? ")
numMeses= input("Informe o tempo de Investimentos (em Meses) ? ")

jurosCalculado = ( float(valorInicial) * (float(valortxJuros) / 100) * float(numMeses) )

print(" Total Investido R$", float(valorInicial)  )

print(" Total ganho em juros mensal R$", float(jurosCalculado)  )

print(" Total ganho em juros mensal R$", (float(jurosCalculado) + float(valorInicial)) )

input("Pressione  o botão 'Enter', para continuar ... ")


input("Fórmula de Bhaskara- Calculo de resolva uma equação do segundo grau usando a formula de Bhaskara! Pressione  o botão 'Enter', para continuar ... ")

valorA = input("Informe o valor de A? ")
valorB= input(" Informe o valor de B? ")
valorC= input(" Informe o valor de C? ")

delta = (pow(int(valorB),2)) - 4 * int(valorA) * int(valorC)

if valorA == 0:
    print("O valor de A, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = ((int(valorB) * -1) + delta ** (1 / 2)) / (2 * int(valorA))
    x2 = ((int(valorB) * -1) - delta ** (1 / 2)) / (2 * int(valorA))
    print(" Valor de X1 é ", float(x1)  )
    print(" Valor de X2 é ", float(x2)  )

input("Pressione  o botão 'Enter', para continuar ... ")

input("Conversor de moedas- Calculo de conversão reais para dólares! Pressione  o botão 'Enter', para continuar ... ")

valorReais = input("Qual é o valor  ? ")
valorCotacao= input("Qual é o valor da Cotação do Dólar ? ")

valorDolares= ( float(valorReais) / (float(valorCotacao)))

print(" O valor de R$", float(valorReais), "convertido em dolares é ",  (float(valorDolares)))