import sys
import random
from itertools import groupby
import statistics
from collections import Counter

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

    while(Question):
         number = int(input(" Informe um numero ? "))
         if(number > 0):
            count = ListNumbersOrdenada.count(number)
            print(f"O elemento {number} aparece  {count} vezes ")
         else: 
            Question = False


def RemocaoDuplicatas():
    
    ListNumbersDuplicados=[]

    while(len(ListNumbersDuplicados) <= 9):
        number_readDupli = int(input(" Informe um numero ? "))    
        ListNumbersDuplicados.append(number_readDupli)   
        
    
    print(f"Segue a lista com itens duplicados ... {ListNumbersDuplicados}")   
    ListNumbersDuplicados = [itemlist for itemlist, group in groupby(ListNumbersDuplicados)]
    print(f"Segue a lista sem duplicados ... {ListNumbersDuplicados}")
        
        
def EstatisticasLista():
    ListNumbersEstatisticas=[]

    while(len(ListNumbersEstatisticas) <= 9):
        number_readEstatisticas = int(input(" Informe um numero ? "))    
        ListNumbersEstatisticas.append(number_readEstatisticas)
    
    
    print(f"O Maior item da lista é ... {max(ListNumbersEstatisticas)}")
    print(f"O Menor item da lista é ... {min(ListNumbersEstatisticas)}")
    print(f"A média dos itens da lista é ... {sum(ListNumbersEstatisticas) / len(ListNumbersEstatisticas)}")
    print(f"A mediana dos itens da lista é ... {statistics.median(ListNumbersEstatisticas)}")
    

def InversaoLista():
    
    fraseRead = (input(" Escreva uma frase ")) 
    print(f" A frase que foi informada é .. {fraseRead}")
    print(f" A frase invertida  é .. {fraseRead[::-1]}")


def  IntersecaoListas():
    
    ListOne=[]
    Listtwo=[]

    (input(" Informe 5 numeros para compor a Primeira lista..  Pressione  o botão 'Enter', para continuar ..."))

    while(len(ListOne) <= 4):
        number_one = int(input(" Informe um numero ? "))  
        ListOne.append(number_one)
    
    (input(" Informe 5 numeros para compor a Segunda lista..  Pressione  o botão 'Enter', para continuar ..."))
    
    while(len(Listtwo) <= 4):
        number_two = int(input(" Informe um numero ? "))  
        Listtwo.append(number_two)
    
    itensIguais = [elemento for elemento in ListOne if elemento in Listtwo]
    
    if len(itensIguais) == 0:
        print(f"As correspondências das listas são {itensIguais}")
    else:
        print(f"A correspondência das listas é {itensIguais}")
        
def  IndiceMultiplos3():
     
    listMultiplos = [num for num in range(1,50) if (num % 3 == 0) ]
    
    print(f" Os Múltiplos de 1 a 50, são: {listMultiplos}")
    
def  TamanhoPalavra(): 
    
    SizeWords = {}
    
    fraseRead = (input(" Escreva uma frase ")) 
    
    countPalavas = fraseRead.split()
    
    listKeys = []
    
    for item in countPalavas:
        SizeWords[len(item)] = item
        listKeys.append(len(item))

        
    for itemkey in listKeys:
        print (f" ----------------------------------------  ----------------------------------")
        print (f" ---------------------------------------- ... Tamanho   x     Palavra")
        print (f"A ordem crescente do tamanho das palavras ... {itemkey} x {SizeWords[itemkey]}")
        print (f" ----------------------------------------  ----------------------------------")
    
    
if __name__ == "__main__":
    #SomaElementos()
    #NumbersImparRange()
    #ListNumbersOrdenada()
    #ContagemOcorrencias()
    #RemocaoDuplicatas()
    #EstatisticasLista()
    #InversaoLista()
    #IntersecaoListas()
    #IndiceMultiplos3()
    TamanhoPalavra()