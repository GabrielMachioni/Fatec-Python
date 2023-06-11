import sys
from time import sleep

from utils import telas
from utils.funcoes_auxiliares import printc, limpar_tela
from utils.receitas import Receitas
from utils.importar_dados import Importar
from utils.comentarios import Comentarios
from usuario import cadastro, login, alterar_conta

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

    id = login_user.get_infos()

    user_logado(id)


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
    print(telas.tela_sobre)  # TODO: adc sobre


def user_logado(id):
    limpar_tela()
    
    op = int(input(telas.menu_login))
    while op not in [1, 2, 3, 4, 5, 8, 9]:
        limpar_tela()
        printc('vermelho', 'Opção inválida, tente novamente: ')
        op = int(input(telas.menu_login))

    if op == 1:
        ver_receita(id)

    elif op == 2:
        adicionar_receita(id)
        
    elif op == 3:
        editar_receita(id)
        
    elif op == 4:
        importar_dados(id)
        
    elif op == 5:
        comentarios(id)
    
    elif op == 8:
        config_conta(id)

    else:
        printc('verde', 'Saindo...')
        sleep(1)
        sys.exit()
    
    
def ver_receita(id):
    """
    Visualizar receitas
    """
    limpar_tela()
    receitas = Receitas()
    receitas.visualizar_receitas()
    enter = str(input('Aperte ENTER para continuar...'))
    user_logado(id)


def adicionar_receita(id):
    """
    Adiconar nova receita
    """
    limpar_tela()
    receitas = Receitas()
    receitas.adicionar_receita()
    enter = str(input('Aperte ENTER para continuar...'))
    user_logado(id)
    
    
def editar_receita(id):
    """
    Editar receita
    """
    limpar_tela()
    receitas = Receitas()
    receitas.editar_receita()
    enter = str(input('Aperte ENTER para continuar...'))
    user_logado(id)


def config_conta(id):
    """
    Opções de configuração de conta
    """
    limpar_tela()
    
    alt_cont = alterar_conta.AlterarConta()
    
    op = int(input(telas.config_conta))
    while op not in [1, 2, 3, 9]:
        limpar_tela()
        printc('vermelho', 'Opção inválida, tente novamente: ')
        op = int(input(telas.config_conta))
        
    if op == 1:
        alt_cont.alter_nome_usuario(id)
        
    elif op == 2:
        alt_cont.alter_senha(id)
        
    elif op == 3:
        alt_cont.excluir_conta(id)
        
    else:
        printc('verde', 'Saindo...')
        sleep(1)
        sys.exit()
        
    enter = str(input('Aperte ENTER para continuar...'))
    user_logado(id)
        
    
def importar_dados(id):
    """
    Importar dados
    """
    limpar_tela()
    
    importar = Importar()
    
    op = int(input(telas.importar_dados))
    while op not in [1, 2, 9]:
        limpar_tela()
        printc('vermelho', 'Opção inválida, tente novamente: ')
        op = int(input(telas.importar_dados))
        
    if op == 1:
        importar.criar_zip()
        
    elif op == 2:
        importar.importar_url()
        
    else:
        printc('verde', 'Saindo...')
        sleep(1)
        sys.exit()
        
    enter = str(input('Aperte ENTER para continuar...'))
    user_logado(id)
    
def comentarios(id):
    """
    Comentários dos usuarios
    """
    comen = Comentarios()
    op = int(input(telas.comentarios))
    while op not in [1, 2, 3, 9]:
        limpar_tela()
        printc('vermelho', 'Opção inválida, tente novamente: ')
        op = int(input(telas.comentarios))

    if op == 1:
        comen.visualizar_comentarios()

    elif op == 2:
        comen.editar_comentario(id)
        
    elif op == 3:
        comen.adicionar_comentario(id)

    else:
        printc('verde', 'Saindo...')
        sleep(1)
        sys.exit()  
        
    enter = str(input('Aperte ENTER para continuar...'))
    user_logado(id)

if __name__ == '__main__':
    main()
