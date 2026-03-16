#CRIAÇÃO DO DICIONÁRIO
estadio = {}

#ENTRADA DE DADOS
for i in range(5):
   nome_material = input("Digite o nom edo material de contrução: ") #chave
   valor = input("Informe o valor unitário:") #valor 
   
   estadio[nome_material] = valor
   
#SAÍDA DE DADOS
print("---Lista de Materiais de Construção---")
for estadio[nome_material], valor in estadio.items():
        print(f"{estadio[nome_material]} | {valor}")



#SAÍDA DE DADOS
#print(f"O nome do aluno é: {aluno["Nome"]}")
#print(f"O curso do aluno é: {aluno["Curso"]}")
#print("Aprovado" if aluno["Nota"] >= 18 else "Reprovado")
