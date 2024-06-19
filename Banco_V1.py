menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = """"""
numero_saques = 0



while True:
    
    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")
        valor = float(input("Qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            
            print("Valor inválido!")


    elif opcao == "s":
        print("Saque")
        sacar = float(input("Quanto deseja sacar? "))
        if numero_saques < 3:
            if sacar > 500:
                print("O valor limite de saque é R$500,00")
            else:
                if sacar <= saldo:
                    print(f"Saque de {sacar:.2f} efetuado com sucesso!")
                    extrato += f"Saque: R${sacar:.2f}\n"
                    saldo -= sacar
                    numero_saques += 1
                else:
                    print("Valor inválido!")
        else: 
            print("Oeraçao falhou, limite de 3 saques excedido ")
    

    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Total: R${saldo:.2f}\n")


    elif opcao == "q":
        break


    else:
        print("Operação invalida, por favor selecione novamente a operação desejada!")