import sqlite3 
import bcrypt
from time import sleep
import getpass

from utils.funcoes_auxiliares import printc, limpar_tela

class Login:
    """
    Responsável por logar usuário
    """
    def __init__(self):
        self.usuario = ''
        self.hash_senha = ''
        self.id = 0

    def get_infos(self):
        """
        Adquirir informações do usuário
        """
        self.__exist_db()
        
        self.usuario = str(input('Nome de usuário: '))
        senha = getpass.getpass('Sua senha: ')

        while not self.__verificar_credenciais(senha):
            limpar_tela()
            self.usuario = str(input('Nome de usuário: '))
            senha = getpass.getpass('Sua senha: ')
            
        return self.id


    def __verificar_credenciais(self, senha):
        """
        Verificar credenciais do usuário no Banco de Dados
        """
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()

        try:
            comando_sql = "SELECT * FROM usuarios WHERE nome = ?"
            cursor.execute(comando_sql, (self.usuario,))
            usuario = cursor.fetchone()
            
            self.id = usuario[0]

            if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario[2]):
                printc('verde',"Login bem-sucedido.")
                sleep(1)
                cursor.close()
                conexao.close()
                return True
            
        except:
            printc('vermelho', 'Usuário não cadastrado!')
        
        sleep(1)
        cursor.close()
        conexao.close()

        return False
    
    def __exist_db(self):
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
        tabela_existe = cursor.fetchone()

        if not tabela_existe:
            conexao = sqlite3.connect('app.db')

            cursor = conexao.cursor()

            comando_sql = '''CREATE TABLE usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                senha TEXT
                            )'''
                            
            cursor.execute(comando_sql)

        cursor.close()
        conexao.close()
