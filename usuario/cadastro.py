import sqlite3
import bcrypt
import getpass

from utils.funcoes_auxiliares import printc, limpar_tela

class Cadastro:
    """
    Responsável por cadastrar usuário
    """
    def __init__(self):
        self.usuario = ''
        self.hash_senha = ''

    def get_informations(self):
        """
        Pegar informações do Usuário
        """
       
        self.usuario = str(input('Informe seu nome de usuário: '))
        senha_user = getpass.getpass('Sua senha: ')
        confirm_senha = getpass.getpass('Confirme sua senha: ')

        while senha_user != confirm_senha:
            limpar_tela()
            printc('vermelho', 'Senhas diferentes, tente novamente! ')

            senha_user = getpass.getpass('Sua senha: ')
            confirm_senha = getpass.getpass('Confirme sua senha: ')

        self.hash_senha = bcrypt.hashpw(senha_user.encode('utf-8'), bcrypt.gensalt())
        self.registrar_user()


    def registrar_user(self):
        """
        Registrar usuário no banco
        """
        self.__exist_db()
 
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()

        comando_sql = "INSERT INTO usuarios (nome, senha) VALUES (?, ?)"
        valores = (self.usuario, self.hash_senha)
        cursor.execute(comando_sql, valores)

        conexao.commit()

        cursor.close()
        conexao.close()


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
            