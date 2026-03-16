while True:
    
    escolha = str(input("Comfirmar operação? "))

    match escolha:
        case "sim" | "yes" | "s" | "y":
            print("Confirmado!")
            break
        case "nao" | "no" | "n" | "nope":
            print("Rejeitado!")
            break
        case _:
            print("Selecione novamente: ")
        
        