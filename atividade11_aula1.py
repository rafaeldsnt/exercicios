

pessoa = {"nome" : "Rafael", "idade" : 45 , "cidade":"Petropolis"}

print(f"Dados da pessoa {pessoa}")

pessoa["idade"] = 48

pessoa["email"] = "rafaeldsn@hikrjrkrj.com.br"

pessoa["sexo"] = "M"

del pessoa["nome"]
del pessoa["email"]

print(f"Dados da pessoa após idade..  {pessoa}")

for item in pessoa.values():
    print(item)

