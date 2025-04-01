texto = "O rato roeu a roupa do rei de roma"


palavras_2 = ["não", "existe", "nenhuma", "comida", "azul", "existe"]

contagem = {}
contagem2 = {}

for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1


for itempatalavra in palavras_2:
    contagem2[itempatalavra] = contagem2.get(itempatalavra, 0) + 1


print(contagem) 

print(contagem2) 