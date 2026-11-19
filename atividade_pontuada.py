import os

# limpar tela
def limpar_tela():
    os.system('cls')

# mostrar menu
def mostrar_menu():
    print('''=== BANCO COFRINHO · CAIXA ===
       1 - Ver saldo
       2 - Depositar
       3 - Sacar
       4 - Ver extrato
       0 - Sair''')
    print("-" * 30)

# autenticar acesso
def autenticar():
    senha_correta = '123'

    for tentativa in range(1, 4):
        senha = input('Digite a senha de acesso: ')

        if senha == senha_correta:
            print('Acesso permitido!')
            return True

        tentativas_restantes = 3 - tentativa
        if tentativas_restantes > 0:
            print(f'Senha incorreta. Tentativas restantes: {tentativas_restantes}')

    print('Acesso bloqueado. Número máximo de tentativas excedido.')
    return False

# ver saldo
def ver_saldo(saldo):
    print(f'\nSaldo atual: R$ {saldo:.2f}')
    
# depositar
def depositar(saldo, extrato):
    valor = float(input('Digite o valor para deposito: R$ '))
    
    if valor <= 0:
        print('Error: O valor do depósito deve ser maior que zero')
        return saldo
    
    saldo += valor
    extrato.append(f"Deposito + R$ {valor:.2f}")
    print(f"Deposito de {valor:.2f} realizado com sucesso!")
    return saldo

# sacar
def sacar(saldo, extrato):
    valor = float(input('Digite o valor para saque: R$ '))
    
    if valor <= 0:
        print('Error: O valor do saque deve ser maior que zero')
        return saldo

    if valor > 1000.00:
        print('Error: O valor máximo permitido por saque é R$ 1.000,00')
        return saldo
    
    if valor > saldo:
        print('Error: Saldo insuficiente para saque')
        return saldo
    
    saldo -= valor
    extrato.append(f"Saque - R$ {valor:.2f}")
    print(f"Saque de {valor:.2f} realizado com sucesso!")
    return saldo

#extrato
def ver_extrato(extrato):
    print("\n=== EXTRATO ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)

    quantidade_depositos = sum(1 for item in extrato if item.startswith("Deposito"))
    quantidade_saques = sum(1 for item in extrato if item.startswith("Saque"))

    total_depositos = sum(
        float(item.split("R$ ")[1])
        for item in extrato
        if item.startswith("Deposito")
    )
    total_saques = sum(
        float(item.split("R$ ")[1])
        for item in extrato
        if item.startswith("Saque")
    )

    print("\n=== RESUMO ===")
    print(f"Depósitos realizados: {quantidade_depositos}")
    print(f"Total depositado: R$ {total_depositos:.2f}")
    print(f"Saques realizados: {quantidade_saques}")
    print(f"Total sacado: R$ {total_saques:.2f}")
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def sair():
    print('\nEncerrado o sistemo. Obrigado por o Banco Cofrinho')
# dados iniciais

saldo = 500.00
extrato = []
opcao = -1

if autenticar():
    while opcao != 0:
        limpar_tela()
        mostrar_menu()

        entrada = input('\nDigite um número de 0 a 4 de acordo com a opção que queira: ')

        if not entrada.isdigit():
            print('Error: Digite apenas números de 0 a 4')
            input('\nPressione enter pra continuar...')
            continue

        opcao = int(entrada)
        
        match opcao:
            case 1:
                ver_saldo(saldo)
            case 2:
                saldo = depositar(saldo, extrato)
            case 3:
                saldo = sacar(saldo, extrato)
            case 4:
                ver_extrato(extrato)
            case 0:
                sair()
                break
            case _:
                print('Opção invalida! Escolha de 0 a 4')
            
        input('\nPressione enter pra continuar...')