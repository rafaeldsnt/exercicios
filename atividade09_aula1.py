import sys
import numpy as np


vet_dados = [15,2,94,30,8,76,2024]

def criar_imprimir_listas(vet_dados):
    print("\n\t O conteúdo do vetor é {vet_dados} ")

def criar_imprimir_lista_v2(vet_dados):
    print(f"\n\t O conteúdo do vetor é {vet_dados}")

def IterandoLista(vet_dados):
    for itemVetor in vet_dados:
        print(f"\n\t O conteúdo do vetor é {itemVetor}")


def UtilizandoNumPycomVetores(vet_dados):
    vetor_np = np.array(vet_dados)
    print(f"\n\t O conteúdo do vetor vetor_np é {vetor_np}")

def CalcularElementosVetor(vet_dados):
    somaElementos = sum(vet_dados)
    print("Soma dos elementos:", somaElementos)

def EncontrarMaioreMenorElementoVetor(vet_dados):
    vet_dados = [3, 7, 2, 9, 4]    
    maior = max(vet_dados)
    menor = min(vet_dados)
    print(f"O Maior elemento do Vetor é o {maior}. O menor elemento é o {menor}")

def InverterOrdemVetor(vet_dados):
    inverso_Vetor = vet_dados[::-1]
    print(f" A ordem inicial do Vetor é  {vet_dados}")
    print(f" A ordem inversa do Vetor é  {inverso_Vetor}")

def MultiplicarElmentosVetor(vet_dados):
    multiplicador = 2
    new_array = [element * multiplicador for element in vet_dados]
    print(f"O novo Vetor ... {new_array}")

def CountElementinVetor(vet_dados):
    SearchinElement = 3
    countElement = vet_dados.count(vet_dados)
    print(f"O elemento {SearchinElement} aparece  {countElement}")

def OrdenarVetor(vet_dados):
    VetOrdenado = sorted(vet_dados)
    print(f"O Vetor ordenado ...  {VetOrdenado}")

def RemovedElementsDuplicates(vet_dados):
    newvetor = list(dict.fromkeys(vet_dados))
    print(f"O Vetor ordenado  e os itens em duplicidade foram eliminados ...  {sorted(newvetor)}")

def OrdenateNumbersParorImparVetor(vet_dados):
    pares = [num for num in vet_dados if (num % 2 == 0) ]
    impares = [num for num in vet_dados if (num % 2 != 0) ]
    print(f"Os valores pares são ...  {sorted(pares)}")
    print(f"Os valores impares são ...  {sorted(impares)}")

def CalculateMediaVetor(vet_dados):
    mediaElementos = sum(vet_dados) / len(vet_dados)
    maxMedia = [num for num in vet_dados if (num > mediaElementos) ]
    minMedia = [num for num in vet_dados if (num < mediaElementos) ]
    print(f"A média é calculada é ...  {mediaElementos:.2f}")
    print(f"Os valores acima da média  são ...  {sorted(maxMedia)}")
    print(f"Os valores menores da média  são ...  {sorted(minMedia)}")

if __name__ == "__main__":
    CalculateMediaVetor(vet_dados)
    #OrdenateNumbersParorImparVetor(vet_dados)
    #RemovedElementsDuplicates(vet_dados)
    #OrdenarVetor(vet_dados)
    #CountElementinVetor(vet_dados)
    #MultiplicarElmentosVetor(vet_dados)
    #InverterOrdemVetor(vet_dados)
    #EncontrarMaioreMenorElementoVetor(vet_dados)
    #CalcularElementosVetor(vet_dados)
    #UtilizandoNumPycomVetores(vet_dados)
    #IterandoLista(vet_dados)
    #criar_imprimir_lista_v2(vet_dados)