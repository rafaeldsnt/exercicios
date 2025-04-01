alunos1 = {"nome": "Rafael", "notas": [8.5, 10, 9.6]}
alunos2= {"nome": "Roger", "notas": [3.1, 7, 9]}
alunos3 = {"nome": "Carlitos", "notas": [7, 9, 4]}

alunosx = alunos1 | alunos2

for itemAlunos in alunos1.items(): 
    nome = alunos1["nome"]
    media = sum(alunos1["notas"])/len(alunos1["notas"])
    

#alunos1["media"] = media


for itemAlunosa in alunosx.items():
    print(itemAlunosa)