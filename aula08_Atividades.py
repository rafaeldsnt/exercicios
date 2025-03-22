import sys

"""
função de saudação
- não recebe parametros 
"""

def saudacao():
    print("Olá, seja bem-vindo(a) ao Python-UC01")


def test_saudacao():
    saudacao()
    
"""
função de somar
- recebe um vetor com numeros e calcula da soma dos mesmos 
"""

def somar(numeros):
    somatorio=0
    for valor in numeros:
        somatorio = int(somatorio) + int(valor)
    return somatorio


    #& 'c:\Python310\python.exe' 'C:\Users\50129532025.1\Documents\Python-UC1\Python-UC1\exercicios\aula08_Atividades.py' 3 4 3 3


def test_somar():
    somatorio = somar(3,1,2,5)
    print(f"O somatório dos numeros passos por parametros é {somatorio}")


"""
Exercício 3: Função par_ou_impar
Função par_ou_impar
- recebe um vetor com numeros e verfica se é Par ou Impar
"""

def VerificaParouImpar(num):
     
     boolParImp = False
     
     if (num % 2 == 0):
        boolParImp = True
     else:
        boolParImp = False        
        return boolParImp

def test_VerificaParouImpar():
     result = VerificaParouImpar(5)
     if (result):
        print("O numero é Par") 
     else:
        print("O numero é Impar") 

    
"""
Exercício 4: Função fatorial
Função par_ou_impar
- recebe um vetor com numeros e verfica se é Par ou Impar
"""

def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


def test_fatorial():
    num = 5
    resultado = fatorial(num)
    print(f"\n\n\tO numero fatorial de {num}! \n\n\t é {resultado}")

if __name__ == "__main__":
    # Chamando a função
    #test_somar()
    #test_saudacao()
    #test_VerificaParouImpar()
    #test_fatorial()
    
    
    