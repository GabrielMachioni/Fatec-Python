import sqlite3 
import bcrypt
from time import sleep

from utils.funcoes_auxiliares import printc, limpar_tela

class Login:
    """
    Responsável por logar usuário
    """
    def __init__(self):
        self.usuario = ''
        self.hash_senha = ''

    def get_infos(self):
        """
        Adquirir informações do usuário
        """
        self.usuario = str(input('Nome de usuário: '))
        senha = str(input('Sua senha: '))

        while not self.__verificar_credenciais(senha):
            limpar_tela()
            self.usuario = str(input('Nome de usuário: '))
            senha = str(input('Sua senha: '))


    def __verificar_credenciais(self, senha):
        """
        Verificar credenciais do usuário no Banco de Dados
        """
        # Conectar ao banco de dados
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()

        # Buscar o usuário pelo nome
        comando_sql = "SELECT * FROM usuarios WHERE nome = ?"
        cursor.execute(comando_sql, (self.usuario,))
        usuario = cursor.fetchone()

        # Verificar se o usuário existe e se a senha está correta
        if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario[2]):
            printc('verde',"Login bem-sucedido.")
            sleep(1)
            cursor.close()
            conexao.close()
            return True
        
        printc('vermelho', "Nome de usuário ou senha inválidos.")
        sleep(1)
        cursor.close()
        conexao.close()

        return False
