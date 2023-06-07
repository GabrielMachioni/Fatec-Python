import sqlite3
import bcrypt

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
        senha_user = str(input('Informe sua senha: '))
        confirm_senha = str(input('Confirme sua senha: '))

        while senha_user != confirm_senha:
            limpar_tela()
            printc('vermelho', 'Senhas diferentes, tente novamente! ')

            senha_user = str(input('Informe sua senha: '))
            confirm_senha = str(input('Confirme sua senha: '))

        self.hash_senha = bcrypt.hashpw(senha_user.encode('utf-8'), bcrypt.gensalt())
        self.registrar_user()


    def registrar_user(self):
        """
        Registrar usuário no banco
        """
        self.__exist_db()
        
         # Conectar novamente ao banco de dados
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()

        # Executar comando SQL para inserir os dados do usuário na tabela
        comando_sql = "INSERT INTO usuarios (nome, senha) VALUES (?, ?)"
        valores = (self.usuario, self.hash_senha)
        cursor.execute(comando_sql, valores)

        # Confirmar a operação no banco de dados
        conexao.commit()

        # Fechar a conexão e o cursor
        cursor.close()
        conexao.close()


    def __exist_db(self):
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
        tabela_existe = cursor.fetchone()

        if not tabela_existe:
            # Caso a tabela não exista, criar o banco de dados e a tabela
            # Conectar ao banco de dados SQLite
            conexao = sqlite3.connect('app.db')

            # Criar um cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Criar a tabela de usuários
            comando_sql = '''CREATE TABLE usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                senha TEXT
                            )'''
            cursor.execute(comando_sql)

        # Fechar a conexão e o cursor
        cursor.close()
        conexao.close()
            