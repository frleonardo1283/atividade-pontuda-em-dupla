import os

# limpar tela
def limpar_tela():
    os.system('cls')

# ver saldo
def ver_saldo():
    print(f'\nSaldo atual: R$ {saldo:.2f}')
    
# mostrar menu
def mostrar_menu():
    print('''=== BANCOO COFRINHO · CAIXA ===
    1 - Ver saldo
    2 - Depositar
    3 - Sacar
    4 - Ver extrato
    0 - Sair
    ''')
    print("-" * 30)

# depositar
def depositar(saldo, extrato):
    valor = float(input('Digite o valor para deposito: R$ '))
    
    if valor <= 0:
        print('Error: O valor do depósito deve ser maior que zero')
        return saldo
    
    valor += saldo
    extrato.append(f"Deposito + R$ {saldo:.2f}")
    print(f"Deposito de {valor:.2f} com sucesso!")
    return saldo

# dados iniciais

saldo = 500.00
extatrato = []
opcao = -1


