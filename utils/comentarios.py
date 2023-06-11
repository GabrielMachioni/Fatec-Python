import sqlite3

class Comentarios:
    def __init__(self):
        pass
    
    def visualizar_comentarios(self):
        """
        Visualizar comentarios disponíveis
        """
        self.tabela_exists()
        conexao = sqlite3.connect('app.db')
        
        # Criando o cursor
        cursor = conexao.cursor()

        # Executando a consulta
        cursor.execute("SELECT nome_usuario, comentario FROM comentarios")

        # Obtendo os resultados
        resultados = cursor.fetchall()

        # Exibindo os resultados
        print('Comentário de Usuários: ')
        for resultado in resultados:
            nome_usuario, comentario = resultado
            print(f"Comentário de {nome_usuario}: {comentario},")
        # Fechando a conexão
        cursor.close()
        conexao.close()
        
    def adicionar_comentario(self, id):
        """
        Adiconando um comentario no banco de dados
        """
        self.tabela_exists()
        
        conexao = sqlite3.connect('app.db')
        
        # Criando o cursor
        cursor = conexao.cursor()

        # Dados para comentário
        nome_usuario = str(input("Seu nome: "))
        comentario = str(input("Seu comentário: "))

        # Executando a instrução de inserção
        cursor.execute("INSERT INTO comentarios (id_usuario, nome_usuario, comentario) VALUES (?, ?, ?)",
                    (id, nome_usuario, comentario))

        # Commit para salvar as alterações
        conexao.commit()

        # Fechando a conexão
        cursor.close()
        conexao.close()
        
        
    def editar_comentario(self, id):
        """
        Editar um comentario no banco de dados
        """
        self.tabela_exists()
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        
        cursor.execute(f"SELECT id, nome_usuario, comentario FROM comentarios WHERE id_usuario = {id}")

        resultados = cursor.fetchall()

        # Exibindo os resultados
        if resultados:
            print('Qual comentario deseja alterar? Escolha o ID:')
            for resultado in resultados:
                id_comentario, nome_usuario, comentario = resultado
                print(f"ID: {id_comentario}\nComentário de {nome_usuario}: {comentario}\n\n")
                
            id_editar = str(input("ID do comentário que deseja editar: "))
            novo_comentario = str(input("Novo Comentario: "))
            
            # Executando a instrução de atualização
            cursor.execute("UPDATE comentarios SET comentario = ? WHERE id = ?",
                        (novo_comentario, id_editar))

            conexao.commit()
            print('Atualização feita')
                
        else:
            print('Nenhum comentário feito por você foi encontrado.')
        
        cursor.close()
        conexao.close()
        
    def excluir_comentario(self, id):
        """
        Excluir um comentario
        """
        conexao = sqlite3.connect('app.db')
        
        # Criando o cursor
        cursor = conexao.cursor()
        
        consulta = "SELECT id, nome_usuario, comentario FROM comentarios WHERE id_usuario = ?"

        # Executa a consulta usando o cursor
        cursor.execute(consulta, (id))

        # Obtendo os resultados
        resultados = cursor.fetchall()

        # Exibindo os resultados
        if resultados:
            print('Qual comentario deseja alterar? Escolha o ID:')
            for resultado in resultados:
                id_comentario, nome_usuario, comentario = resultado
                print(f"ID: {id_comentario}\nComentário de {nome_usuario}: {comentario}\n\n")
                
            id_comentario_excluir = int(input('ID do comentario que deseja excluir: '))
        
            # Consulta SQL com parâmetro
            consulta = "DELETE FROM comentarios WHERE id_comentario = ?"

            # Executa a consulta usando o cursor
            cursor.execute(consulta, (id_comentario_excluir,))

            # Confirma a alteração no banco de dados
            conexao.commit()

            # Verifica quantas linhas foram afetadas pela operação
            num_linhas_afetadas = cursor.rowcount

            # Verifica se o comentário foi excluído com sucesso
            if num_linhas_afetadas > 0:
                print("O comentário foi excluído com sucesso.")
            else:
                print("Nenhum comentário foi excluído")
                
        else:
            print('Nenhum comentário seu foi encontrado.')
            
        cursor.close()
        conexao.close()
        
        
    def tabela_exists(self):
        """
        Cria a tabela comentarios caso nao exista
        """
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='comentarios'")
        tabela_existe = cursor.fetchone()
        
        if not tabela_existe:
            # Caso a tabela não exista, criar o banco de dados e a tabela
            # Conectar ao banco de dados SQLite
            conexao = sqlite3.connect('app.db')

            # Criar um cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Criar a tabela de usuários
            comando_sql = '''CREATE TABLE comentarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_usuario INTEGER,
                                nome_usuario TEXT,
                                comentario TEXT
                            )'''
            cursor.execute(comando_sql)

        # Fechar a conexão e o cursor
        cursor.close()
        conexao.close()
        