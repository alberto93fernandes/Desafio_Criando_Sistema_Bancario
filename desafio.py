from datetime import datetime


# Desafio: Criar um sistema bancário simples com funcionalidades de depósito, saque e extrato.

menu = """
    Bem-vindo ao Banco Wayne!
    Escolha uma opção:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:
    opcao = input("")

    # Realizar depósito
    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        if valor <= 0:
            print("Valor inválido. O depósito deve ser maior que zero.")
        else:
            saldo += valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Formata a data e hora atual
            extrato += f"Depósito: R$ {valor:.2f} | Data: {data_hora}\n"

            # extrato += f"Depósito: R$ {valor:.2f}\n" # Adiciona o depósito ao extrato
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")

        print("Depósito")
    
    # Realizar saque
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))# float para garantir que o valor seja um número decimal
        if valor <= 0:
            print("Valor inválido. O saque deve ser maior que zero.")
       
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        
        elif valor > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f} por saque.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de {LIMITE_SAQUES} saques saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"Saque: R$ {valor:.2f} | Data: {data_hora}\n"
            
            # extrato += f"saque: R$ {valor:.2f}\n" #isso mostra o valor do saque no extrato
            numero_saques += 1
            print("Saque realizado com sucesso! Saldo atual: R$ {:.2f}".format(saldo))

        else:
            print("Operação falhou. Selecione uma opção válida.")
      
        
    # Exibir extrato   
    elif opcao == "e":
        print("\n============Extrato=============")
        print("Não foram realizadas movimentações." if not extrato else extrato) #verifica se o extrato está vazio se não estiver vazio, exibe o extrato.
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=================================")
    
    # Sair do programa  
    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida, por favor tente novamente.")

    
