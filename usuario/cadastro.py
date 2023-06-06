import sqlite3

def criar_cadastro():
    criar_tabela()
    adicionar_usuario()
    
    
def criar_tabela():
    conexao = sqlite3.connect('user.db')
    cursor = conexao.cursor()

    # Criação da tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            senha TEXT 
        )
    ''')

    conexao.commit()
    conexao.close()
    

def adicionar_usuario():
    nome = input("Seu nome: ")
    while True:
        senha = input("Senha: ")
        conf_senha = input("confirmar Senha: ")
        
        if senha == conf_senha:
            break
        
        print('Senhas diferentes, tente novamente!')
    
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO usuario (nome, senha)
        VALUES (?, ?)
    ''', (nome, senha))

    conexao.commit()
    conexao.close()
    print("Usuário adicionado com sucesso!")
