#CRIAÇÃO DO DIDIONÁRIO
aluno = {}
#ENTRADA DE DADOS
aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Curso"] = input("Digite o curso do aluno: ")
aluno["Nota"] = float(input("Digite a nota do aluno: "))
#SAÍDA DE DADOS
print(f"O nome do aluno é: {aluno["Nome"]}")
print(f"O curso do aluno é: {aluno["Curso"]}")
print("Aprovado" if aluno["Nota"] >= 18 else "Reprovado")
