# Funções para operações bancárias existentes

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
    except ValueError:
        print("Operação falhou! Por favor, insira um valor numérico válido.")
    
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite_saques, limite):
    try:
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

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
    except ValueError:
        print("Operação falhou! Por favor, insira um valor numérico válido.")
    
    return saldo, extrato, numero_saques

def extrato_bancario(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# Funções para cadastro de usuários e contas

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

def criar_conta_corrente(usuario):
    nova_conta = ContaCorrente(usuario)
    usuario.contas.append(nova_conta)
    return nova_conta

class ContaCorrente:
    numero_sequencial = 1
    agencia = '0001'

    def __init__(self, usuario):
        self.usuario = usuario
        self.numero_conta = ContaCorrente.numero_sequencial
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        ContaCorrente.numero_sequencial += 1


def filtrar_por_cpf(lista_usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario.cpf == cpf]
    return usuarios_filtrados

def listar_contas(usuarios):
    print("\nLista de Contas Correntes:")
    for usuario in usuarios:
        print(f"Usuário: {usuario.nome} - CPF: {usuario.cpf}")
        for conta in usuario.contas:
            print(f"    Conta Corrente: {conta.numero_conta} - Saldo: R$ {conta.saldo:.2f}")


# Sistema bancário

menu = """
[c] Criar Usuário
[l] Criar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[m] Listar Contas
[q] Sair

=> """

senha_correta = "1234"
tentativas = 3
senha = ""

usuarios = []

def autenticar():
    global senha
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

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")

    # Verifica se o CPF já está cadastrado
    if any(usuario.cpf == cpf for usuario in usuarios):
        print("CPF já cadastrado!")
        return

    novo_usuario = Usuario(nome, cpf)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")

def criar_conta():
    cpf = input("Digite o CPF do usuário: ")
    usuarios_encontrados = filtrar_por_cpf(usuarios, cpf)
    if not usuarios_encontrados:
        print("Usuário não encontrado.")
        return

    usuario = usuarios_encontrados[0]
    conta = criar_conta_corrente(usuario)
    print(f"Conta corrente criada para {usuario.nome}. Número da conta: {conta.numero_conta}")

def operacao_deposito():
    cpf = input("Digite o CPF do usuário: ")
    usuarios_encontrados = filtrar_por_cpf(usuarios, cpf)
    if not usuarios_encontrados:
        print("Usuário não encontrado.")
        return

    usuario = usuarios_encontrados[0]
    
    if not usuario.contas:
        print("Usuário não possui conta corrente.")
        return
        
    conta_numero = int(input("Digite o número da conta corrente: "))
    conta_encontrada = next((conta for conta in usuario.contas if conta.numero_conta == conta_numero), None)
    if not conta_encontrada:
        print("Conta corrente não encontrada.")
        return

    print(f"Depósito para o usuário {usuario.nome} com CPF {usuario.cpf} e conta corrente número {conta_encontrada.numero_conta}.")
    conta_encontrada.saldo, conta_encontrada.extrato = depositar(conta_encontrada.saldo, conta_encontrada.extrato)

def operacao_saque():
    cpf = input("Digite o CPF do usuário: ")
    usuarios_encontrados = filtrar_por_cpf(usuarios, cpf)
    if not usuarios_encontrados:
        print("Usuário não encontrado.")
        return

    usuario = usuarios_encontrados[0]
    
    if not usuario.contas:
        print("Usuário não possui conta corrente.")
        return
        
    conta_numero = int(input("Digite o número da conta corrente: "))
    conta_encontrada = next((conta for conta in usuario.contas if conta.numero_conta == conta_numero), None)
    if not conta_encontrada:
        print("Conta corrente não encontrada.")
        return

    print(f"Saque para o usuário {usuario.nome} com CPF {usuario.cpf} e conta corrente número {conta_encontrada.numero_conta}.")
    conta_encontrada.saldo, conta_encontrada.extrato, conta_encontrada.numero_saques = sacar(conta_encontrada.saldo, conta_encontrada.extrato, conta_encontrada.numero_saques, limite_saques, limite)

def operacao_extrato():
    cpf = input("Digite o CPF do usuário: ")
    usuarios_encontrados = filtrar_por_cpf(usuarios, cpf)
    if not usuarios_encontrados:
        print("Usuário não encontrado.")
        return

    usuario = usuarios_encontrados[0]
    
    if not usuario.contas:
        print("Usuário não possui conta corrente.")
        return
        
    conta_numero = int(input("Digite o número da conta corrente: "))
    conta_encontrada = next((conta for conta in usuario.contas if conta.numero_conta == conta_numero), None)
    if not conta_encontrada:
        print("Conta corrente não encontrada.")
        return

    print(f"Extrato para o usuário {usuario.nome} com CPF {usuario.cpf} e conta corrente número {conta_encontrada.numero_conta}.")
    extrato_bancario(conta_encontrada.saldo, conta_encontrada.extrato)

def main():
    autenticar()

    while True:
        opcao = input(menu)

        try:
            if opcao == "c":
                criar_usuario()

            elif opcao == "l":
                criar_conta()

            elif opcao == "d":
                operacao_deposito()

            elif opcao == "s":
                operacao_saque()

            elif opcao == "e":
                operacao_extrato()

            elif opcao == "m":
                listar_contas(usuarios)

            elif opcao == "q":
                print("Encerrando o programa. Obrigado por utilizar nossos serviços.")
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

        except KeyboardInterrupt:
            print("\nEncerrando o programa. Obrigado por utilizar nossos serviços.")
            break

if __name__ == "__main__":
    main()
