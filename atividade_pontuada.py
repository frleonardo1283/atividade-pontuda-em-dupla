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
    extrato.append(f"Deposito + R$ {saldo:.2f}")
    print(f"Deposito de {valor:.2f} realizado com sucesso!")
    return saldo

def sair():
    print('\nEncerrado o sistemo. Obrigado por o Banco Cofrinho')
# dados iniciais

saldo = 500.00
extrato = []
opcao = -1

while opcao != 0:
    limpar_tela()
    mostrar_menu()
    
    opcao = int(input('\nDigite um número de 0 a 4 de acordo com a opção que queira: '))
    
    match opcao:
        case 1:
            ver_saldo(saldo)
        case 2:
            saldo = depositar(saldo, extrato)
        case 0:
            sair()
            break
        case _:
            print('Opção invalida! Escolha de 0 a 4')
        
    input('\nPressione enter pra continuar...')

