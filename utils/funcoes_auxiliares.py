import platform
import os

def printc(cor, msg):
    """Imprimir mensagem com cores"""
    cores = {
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'vermelho': '\033[91m',
        'reset': '\033[0m'
    }

    cor_formatada = cores.get(cor.lower(), cores['reset'])
    print(f'{cor_formatada}{msg}{cores["reset"]}')


def limpar_tela():
    """Limpar tela de acordo com o SO do usuário"""
    sistema_operacional = platform.system()
    if sistema_operacional == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
