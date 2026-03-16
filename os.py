import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando:",e)
        
def mostrar_ip():
    executar_comando("ipconfig")

def renovar_ip():
    executar_comando("ipconfig /renew")
    
def mostrar_ip_completo():
    executar_comando("ipconfig /all")
    
def ping_host():
    host = input("Digite o IP ou HOSTNAME: ")
    executar_comando(f"ping {host}")

def menu():
    while True:
        print("\n========Ferramenta de Rede========")
        print("1 - MOSTRAR IP")
        print("2 - RENOVAR IP")
        print("3 - MOSTRAR CONFIGURAÇÕES DE REDE COMPLETA")
        print("4 - PING")
        print("0 - SAIR")
        print("===========Criado Por Frederick===============")
        opcao = str(input("Escolha: "))
        
        match opcao:
            case "1":
                mostrar_ip()
            case "2":
                renovar_ip()
            case "3":
                mostrar_ip_completo()
            case "4":
                ping_host()
            case "0":
                print("Saindo")
                break
            case _:
                print("Eita caba sabido!!!")
                
if __name__ == "__main__":
    menu()
        
        
        