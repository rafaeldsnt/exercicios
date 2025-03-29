

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix4_4 = [
    [1, 2, 3, 12],
    [4, 5, 6, 15],
    [7, 8, 9, 96],
    [30, 11, 12, 25]
]

"""""
print("Elemento (0,0):", matriz[0][0])  # Saída: 1
print("Elemento (2,1):", matriz[2][1])  # Saída: 8


for linha in matriz:
    for elemento in linha:
        print(f"|{elemento}|", end='')
    print()


matriz_listcomprehension = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]

print(matriz_listcomprehension)


matrizfor = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matrizfor.append(linha)

for linha in matrizfor:
    print(linha)


soma = 0

for linha in range(4):
    for coluna in range(4):
        soma=soma + matriz4_4[linha][coluna]

print(f"A soma de todos da matrix {soma}")"

somalinha = 0
for i in range(1):
    print(i)
    print(matriz4_4[i])
    somalinha = somalinha + sum(matriz4_4[i])

print(f"A soma de todos os elentos da linha {i} da matrix {somalinha}")"

MarioValordalinha = []
for linha in range(4):
    maior = max(matrix4_4[linha])
    MarioValordalinha.append([linha,maior])

print(f"O Maior elemento de cada linha são: {MarioValordalinha}")




pares = sum(1 for linha in matriz for num in linha if num % 2 == 0)
print(f"Quantidade de números pares: {pares}")



numeros_pares = []
numeros_impares = []
for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            numeros_pares.append(matriz[i][j])
        else:
            numeros_impares.append(matriz[i][j])

print(f"Quantidade de números pares é {len(numeros_pares)} e são eles {numeros_pares}")
print(f"Quantidade de números impares é {len(numeros_impares)} e são eles {numeros_impares}")

"""


num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

matriz[linha_escolhida] = [num * valor for valor in matriz[linha_escolhida]]

for linha in matriz:
    print(linha)

