def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques, limite_saque, LIMITE_SAQUES_DIARIOS):
    if valor > 0:
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite_saque:
            print(f"O valor máximo por saque é de R$ {limite_saque:.2f}.")
        elif numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Limite diário de saques atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
    else:
        print("O valor do saque deve ser positivo.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")

def main():
    saldo = 0
    limite_saque = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES_DIARIOS = 3

    while True:
        opcao = input("\nEscolha a operação desejada:\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> ")

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, limite_saque, LIMITE_SAQUES_DIARIOS)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções do menu.")

if __name__ == "__main__":
    main()