class ContaBancaria:
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_SAQUE = 500

    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self):
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                self.saldo += valor
                self.extrato.append(f"Depósito: R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")
            else:
                print("O valor do depósito deve ser positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    def sacar(self):
        try:
            valor = float(input("Informe o valor do saque: "))
            if valor > 0:
                if valor > self.saldo:
                    print("Saldo insuficiente!")
                elif valor > self.LIMITE_SAQUE:
                    print(f"O valor máximo por saque é de R$ {self.LIMITE_SAQUE:.2f}.")
                elif self.numero_saques >= self.LIMITE_SAQUES_DIARIOS:
                    print("Limite diário de saques atingido.")
                else:
                    self.saldo -= valor
                    self.extrato.append(f"Saque: R$ {valor:.2f}")
                    self.numero_saques += 1
                    print("Saque realizado com sucesso!")
            else:
                print("O valor do saque deve ser positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\n".join(self.extrato))
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("=========================================")

    def iniciar(self):
        while True:
            opcao = input("\nEscolha a operação desejada:\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair\n=> ")

            if opcao == "d":
                self.depositar()
            elif opcao == "s":
                self.sacar()
            elif opcao == "e":
                self.exibir_extrato()
            elif opcao == "q":
                print("Obrigado por utilizar nosso sistema!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma das opções do menu.")

if __name__ == "__main__":
    conta = ContaBancaria()
    conta.iniciar()

