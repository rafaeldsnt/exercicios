import sys
import random


def SomaElementos():

    ListNumbers=[]

    while(len(ListNumbers) <= 4):
        number_read = int(input(" Informe um numero ? "))
        ListNumbers.append(number_read)

    print(f"O somatório dos numeros lidos é : {sum(ListNumbers)}")


def NumbersImparRange():
    numb_impares = [num for num in range(0,50) if (num % 2 != 0) ]
    print(f"Os numeros impares do range de 0 a 50 são : {numb_impares}")


def ListNumbersOrdenada():

    ListNumbersOrdenada=[]

    while(len(ListNumbersOrdenada) <= 4):
        number_read = int(input(" Informe um numero ? "))
        ListNumbersOrdenada.append(number_read)
        sorted(ListNumbersOrdenada, key=abs, reverse=True)
        print(f"List Ordenada {ListNumbersOrdenada}")
        
print(f"O somatório dos numeros lidos é : {ListNumbersOrdenada}")



def ContagemOcorrencias():

    Question = True

    ListNumbersOrdenada = range(0,10)

    print(ListNumbersOrdenada)

    ListNumbersOrdenada = random.choices(ListNumbersOrdenada, k=5)

    print(f" After random {ListNumbersOrdenada}")

    while(Question):
         number = int(input(" Informe um numero ? "))
         if(number > 0):
            count = ListNumbersOrdenada.count(number)
            print(f"O elemento {number} aparece  {count} vezes ")
         else: 
            Question = False

if __name__ == "__main__":
    #SomaElementos()
    #NumbersImparRange()
    #ListNumbersOrdenada()
    ContagemOcorrencias()