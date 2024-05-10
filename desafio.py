menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

senha_correta = "1234"
tentativas = 3
senha = ""

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso concedido.")
        break
    else:
        tentativas -= 1
        if tentativas == 0:
            print("Número máximo de tentativas excedido. Encerrando o programa.")
            exit()
        else:
            print(f"Senha incorreta. Você tem {tentativas} tentativas restantes.")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    try:
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            if valor <= 0:
                print("Operação falhou! O valor informado é inválido.")
            else:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if valor <= 0:
                print("Operação falhou! O valor informado é inválido.")
            elif excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("Encerrando o programa. Obrigado por utilizar nossos serviços.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    except ValueError:
        print("Operação falhou! Por favor, insira um valor numérico válido.")
    except KeyboardInterrupt:
        print("\nEncerrando o programa. Obrigado por utilizar nossos serviços.")
        break
