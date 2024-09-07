import datetime

class Conta:
    def __init__(self, numero_conta, saldo_inicial=0, limite_saque=500, limite_saques=3):
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial
        self.limite_saque = limite_saque
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = ""

    def depositar(self):
        try:
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                self.saldo += valor
                self.extrato += f"{datetime.datetime.now()} - Depósito: R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Valor inválido.")

    def sacar(self):
        try:
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > self.saldo
            excedeu_limite = valor > self.limite_saque
            excedeu_saques = self.numero_saques >= self.limite_saques

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print(f"Operação falhou! O valor do saque excede o limite de R$ {self.limite_saque}.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                self.saldo -= valor
                self.extrato += f"{datetime.datetime.now()} - Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Operação falhou! O valor informado é inválido.")
        except ValueError:
            print("Operação falhou! Valor inválido.")

    def exibir_extrato(self):
        print(f"\n==== EXTRATO - Conta {self.numero_conta} ====")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def transferir(self, conta_destino, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.extrato += f"{datetime.datetime.now()} - Transferência Enviada: R$ {valor:.2f} para Conta {conta_destino.numero_conta}\n"
            conta_destino.extrato += f"{datetime.datetime.now()} - Transferência Recebida: R$ {valor:.2f} da Conta {self.numero_conta}\n"
            print(f"Transferência de R$ {valor:.2f} para a conta {conta_destino.numero_conta} realizada com sucesso.")
        else:
            print("Operação falhou! Saldo insuficiente ou valor inválido.")

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self):
        numero_conta = input("Informe o número da nova conta: ")
        if numero_conta in self.contas:
            print("Conta já existe! Por favor, tente novamente.")
        else:
            self.contas[numero_conta] = Conta(numero_conta)
            print(f"Conta {numero_conta} criada com sucesso!")

    def obter_conta(self, numero_conta):
        return self.contas.get(numero_conta)

def exibir_menu():
    menu = """
    [n] Nova Conta
    [d] Depositar
    [s] Sacar
    [t] Transferir
    [e] Extrato
    [q] Sair
    => """
    return input(menu)

def main():
    banco = Banco()

    while True:
        opcao = exibir_menu()

        if opcao == "n":
            banco.criar_conta()

        elif opcao == "d":
            numero_conta = input("Informe o número da conta para depósito: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                conta.depositar()
            else:
                print("Conta não encontrada!")

        elif opcao == "s":
            numero_conta = input("Informe o número da conta para saque: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                conta.sacar()
            else:
                print("Conta não encontrada!")

        elif opcao == "t":
            numero_conta_origem = input("Informe o número da conta de origem: ")
            conta_origem = banco.obter_conta(numero_conta_origem)
            if conta_origem:
                numero_conta_destino = input("Informe o número da conta de destino: ")
                conta_destino = banco.obter_conta(numero_conta_destino)
                if conta_destino:
                    valor = float(input("Informe o valor da transferência: "))
                    conta_origem.transferir(conta_destino, valor)
                else:
                    print("Conta de destino não encontrada!")
            else:
                print("Conta de origem não encontrada!")

        elif opcao == "e":
            numero_conta = input("Informe o número da conta para extrato: ")
            conta = banco.obter_conta(numero_conta)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada!")

        elif opcao == "q":
            print("Saindo... Obrigado por usar o sistema bancário.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
