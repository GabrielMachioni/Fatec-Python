import sys
import sqlite3
from time import sleep
import bcrypt

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
        # Conectando ao banco de dados
        conexao = sqlite3.connect('app.db')

        # Criando o cursor
        cursor = conexao.cursor()

        # Dados atualizados da conta
        novo_nome = str(input("Novo nome de usuário: "))

        # Executando a instrução de atualização
        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?",
                    (novo_nome, id))

        # Commit para salvar as alterações
        conexao.commit()

        # Fechando a conexão
        conexao.close()
        
        printc('amarelo', 'Nome de Usuário Alterado')
        sleep(1)
        
        
    def alter_senha(self, id):
        """
        Alterar senha do usuario no banco de dados
        """
        # Conectando ao banco de dados
        conexao = sqlite3.connect('app.db')

        # Criando o cursor
        cursor = conexao.cursor()

        # Dados atualizados da conta
        novo_senha = str(input("Nova senha: "))
        conf_senha = str(input("Confirmar senha: "))
        
        while novo_senha != conf_senha:
            printc("vermelho", "As senhas não coincidem!")
            novo_senha = str(input("Nova senha: "))
            conf_senha = str(input("Confirmar senha: "))
            limpar_tela()
            
        hash_senha = bcrypt.hashpw(novo_senha.encode('utf-8'), bcrypt.gensalt())

        # Executando a instrução de atualização
        cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?",
                    (hash_senha, id))

        # Commit para salvar as alterações
        conexao.commit()

        # Fechando a conexão
        conexao.close()
        
        printc('amarelo', 'Senha Alterada')
        sleep(1)
        
        
    def excluir_conta(self, id):
        """
        Excluir conta do usuario do banco de dados
        """
        # Conectando ao banco de dados
        conexao = sqlite3.connect('app.db')

        # Criando o cursor
        cursor = conexao.cursor()

        # Executando a instrução de exclusão
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))

        # Commit para salvar as alterações
        conexao.commit()

        # Fechando a conexão
        conexao.close()
        
        printc('vermelho', 'Conta excluída')
        sleep(2)
        sys.exit()
    