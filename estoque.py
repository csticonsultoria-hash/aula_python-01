#criação do dicionário estoque
estoque = {
    "camisa":50,
    "calça":15,
    "boné":25,
    "tenis naique":35,
}
#Mostrar estoque atual
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(f"{produto} : {quantidade}")
#Pedindo dados para o usuário do sistema
nome_produto = input("\nInforme o nome do produto vendido: ")
quantidade_vendida = int(input("\nInforme a quantidade vendida: "))
#Atualizar o estoque
if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print("Venda Realizada com sucesso!!!camisa")
else:
    print("Produto não encontrado")
#Mostrar estoque atializado
for produto, quantidade in estoque.items():
    print(f"{produto} | {quantidade}")