menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
extrato = 0
while True:
    opcao = input(menu)
    if opcao == "d":
        while True:
            valor_deposito = float(input("Informe o valor do depósito: R$"))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += 1
                print(
                    f"""
Depósito realizado com sucesso! Seu saldo atual é de: 
R${saldo:.2f}
"""
                )
                break
            else:
                print(
                    """
Valor de deposito invalido. 
Por favor, insira um valor maior que 0 
                    """
                )
    elif opcao == "s":
        if numero_saque == 3:
            print("Você atingiu o limite de saques diários.")
        else:
            while True:
                valor_saque = float(input("Informe o valor do saque: R$"))
                if valor_saque > limite:
                    print("Valor máximo de saque é de R$500,00")
                elif valor_saque > 0 and valor_saque <= saldo:
                    saldo -= valor_saque
                    numero_saque += 1
                    extrato += f"Total de saques: R${valor_saque:.2f}"
                    print(f"Sa atual R$ {valor_saque:.2f}")
                    break
                else:
                    print("Valor de saldo insuficiente")
                    break
    elif opcao == "e":
        print(
            f"""
====================
Seu extrato:
Saldo: R${saldo:.2f}
Limite diário de saque: {limite}
Número de saques diários: {numero_saque}de{LIMITE_SAQUE}
====================
            """
        )
        if extrato > 0:
            print("Não foram realizadas operações." if not extrato else extrato)
    elif opcao == "q":
        print("Terminando todas as operações...")
        break
    else:
        print(
            """
            Opção inválida. 
            Por favor selecione novamente a operação desejada.
            """
        )
