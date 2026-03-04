maria = {"Arroz", "Banana","Arroz"}
joaquina = {"Arroz", "Lentilha"}
cirilo = {"Arroz","Aveia"}
fredy = {"Arroz", "Trigo"}

comum = maria.intersection(maria,joaquina,cirilo,fredy)
print(comum)

total = maria.union(maria,joaquina,cirilo,fredy)
print(total)
print(len(total))

itens_maria = set(maria)
print(itens_maria)