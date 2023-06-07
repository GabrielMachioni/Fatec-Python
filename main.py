import sys
from time import sleep

from utils import telas
from utils.funcoes_auxiliares import printc, limpar_tela
from usuario import cadastro, login

def main():
    """
    Tela principal
    """
    limpar_tela()
    op = int(input(telas.menu_principal))
    while op not in [1, 2, 8, 9]:
        limpar_tela()
        printc('vermelho', 'Opção inválida, tente novamente: ')
        op = int(input(telas.menu_principal))

    if op == 1:
        fazer_login()

    elif op == 2:
        fazer_cadastro()
    
    elif op == 8:
        mostrar_sobre()

    else:
        printc('verde', 'Saindo...')
        sleep(1)
        sys.exit()


def fazer_login():
    """
    Fazer Login do Usuário
    """
    limpar_tela()
    login_user = login.Login()

    login_user.get_infos()

    user_logado()


def fazer_cadastro():
    """
    Fazer Cadastro do Usuário
    """
    limpar_tela()
    new_user = cadastro.Cadastro()

    printc('amarelo', telas.menu_cadastro)

    new_user.get_informations()
    sleep(1)
    main()


def mostrar_sobre():
    """
    Mostrar tela Sobre
    """
    limpar_tela()
    print(telas.tela_sobre)


def user_logado():
    limpar_tela()
    
    op = int(input(telas.menu_login))
    while op not in [1, 2, 8, 9]:
        limpar_tela()
        printc('vermelho', 'Opção inválida, tente novamente: ')
        op = int(input(telas.menu_login))

    if op == 1:
        ...

    elif op == 2:
        ...
    
    elif op == 8:
        ...

    else:
        printc('verde', 'Saindo...')
        sleep(1)
        sys.exit()
    

if __name__ == '__main__':
    main()

