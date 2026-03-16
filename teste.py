import json
import os

ARQUIVO = "notas.json"

def carregar_notas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, list):
                    return dados
                else:
                    print("Formato de arquivo inválido. Iniciando com lista vazia.")
                    return []
        except (json.JSONDecodeError, IOError):
            print("Erro ao ler o arquivo de notas. Iniciando com lista vazia.")
            return []
    return []

def salvar_notas(notas):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(notas, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar as notas: {e}")

def adicionar_nota():
    try:
        titulo = input("Título da nota: ").strip()
        conteudo = input("Conteúdo da nota: ").strip()
    except KeyboardInterrupt:
        print("\nOperação cancelada.")
        return
    
    if not titulo or not conteudo:
        print("Título e conteúdo não podem ficar em branco.")
        return
    
    notas = carregar_notas()
    
    nova_nota = {
        "titulo": titulo,
        "conteudo": conteudo
    }
    
    notas.append(nova_nota)
    salvar_notas(notas)
    print("Nota salva com sucesso!")

def listar_notas(notas=None):
   
    if notas is None:
        notas = carregar_notas()
    
    if not notas:
        print("Nenhuma nota cadastrada ainda.")
        return
    
    print("\n=== Lista de Notas ===")
    for i, nota in enumerate(notas, 1):
        titulo = nota.get("titulo", "Sem título")
        print(f"{i:2d} - {titulo}")
    print()

def ler_nota():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma nota disponível.")
        return
    
    listar_notas(notas)
    
    try:
        indice = int(input("Digite o número da nota que deseja ler: "))
        if 1 <= indice <= len(notas):
            nota = notas[indice - 1] 
            print("\n" + "="*40)
            print(f"Título: {nota['titulo']}")
            print("-"*40)
            print(nota['conteudo'])
            print("="*40 + "\n")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas um número válido.")
    except KeyboardInterrupt:
        print("\nOperação cancelada.")

def deletar_nota():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma nota para excluir.")
        return
    
    listar_notas(notas)
    
    try:
        indice = int(input("Digite o número da nota a ser excluída: "))
        if 1 <= indice <= len(notas):
            nota_removida = notas.pop(indice - 1)
            salvar_notas(notas)
            print(f"Nota '{nota_removida.get('titulo', 'sem título')}' excluída com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite apenas um número válido.")
    except KeyboardInterrupt:
        print("\nOperação cancelada.")

def menu():
    while True:
        print("\n" + "="*30)
        print("       APP DE NOTAS")
        print("="*30)
        print("1 → Adicionar nova nota")
        print("2 → Listar todas as notas")
        print("3 → Ler uma nota")
        print("4 → Excluir uma nota")
        print("5 → Sair")
        print("-"*30)
        
        try:
            opcao = input("Escolha uma opção (1-5): ").strip()
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        
      
        if opcao == "1":
            adicionar_nota()
        elif opcao == "2":
            listar_notas()
        elif opcao == "3":
            ler_nota()
        elif opcao == "4":
            deletar_nota()
        elif opcao == "5":
            print("\nSaindo!")
            break
        else:
            print("Opção inválida. Escolha entre 1 e 5.")

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")