import sys
import sqlite3
from time import sleep
import bcrypt
import getpass

from utils.funcoes_auxiliares import printc, limpar_tela

class AlterarConta:
    """
    Responsável por fazer alterações no banco de dados
    """
    def __init__(self):
        pass
        
    def alter_nome_usuario(self, id):
        """
        Editar nome de usuario no banco de dados
        """
        conexao = sqlite3.connect('app.db')

        cursor = conexao.cursor()

        novo_nome = str(input("Novo nome de usuário: "))

        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?",
                    (novo_nome, id))

        conexao.commit()
        conexao.close()
        
        printc('amarelo', 'Nome de Usuário Alterado')
        sleep(1)
        
        
    def alter_senha(self, id):
        """
        Alterar senha do usuario no banco de dados
        """
        conexao = sqlite3.connect('app.db')

        cursor = conexao.cursor()

        novo_senha = getpass.getpass('Sua senha: ')
        conf_senha = getpass.getpass('Confirmar senha: ')
        
        while novo_senha != conf_senha:
            printc("vermelho", "As senhas não coincidem!")
            novo_senha = getpass.getpass('Sua senha: ')
            conf_senha = getpass.getpass('Confirmar senha: ')
            limpar_tela()
            
        hash_senha = bcrypt.hashpw(novo_senha.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?",
                    (hash_senha, id))

        conexao.commit()
        conexao.close()
        
        printc('amarelo', 'Senha Alterada')
        sleep(1)
        
        
    def excluir_conta(self, id):
        """
        Excluir conta do usuario do banco de dados
        """
        conexao = sqlite3.connect('app.db')

        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))

        conexao.commit()
        conexao.close()
        
        printc('vermelho', 'Conta excluída!')
        sleep(2)
        sys.exit()
    