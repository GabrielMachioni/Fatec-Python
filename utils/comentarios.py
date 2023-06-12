import sqlite3
from utils.funcoes_auxiliares import limpar_tela, printc

class Comentarios:
    def __init__(self):
        pass
    
    def get_infos_json(self):
        """
        Cria uma lista de dicionarios com todas as informações de comentarios
        """
        self.tabela_exists()
        
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        cursor.execute("SELECT id_usuario, nome_usuario, comentario FROM comentarios")
        
        resultados = cursor.fetchall()
        dados = []
        
        for resultado in resultados:
            id_usuario, nome_usuario, comentario = resultado
            dados.append(
                {'nome_autor': id_usuario,
                 'nome_receita': nome_usuario,
                 'receita': comentario}
            )
            
        return dados
    
    
    def visualizar_comentarios(self):
        """
        Visualizar comentarios disponíveis
        """
        limpar_tela()
        self.tabela_exists()
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        cursor.execute("SELECT nome_usuario, comentario FROM comentarios")

        resultados = cursor.fetchall()

        printc('verde', 'Comentários de Usuários: \n')
        for resultado in resultados:
            nome_usuario, comentario = resultado
            print(f"Comentário de {nome_usuario}: {comentario}\n")
        
        cursor.close()
        conexao.close()
        
    def adicionar_comentario(self, id):
        """
        Adiconando um comentario no banco de dados
        """
        limpar_tela()
        self.tabela_exists()
        
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()

        nome_usuario = str(input("Seu nome: "))
        comentario = str(input("Seu comentário: "))

        cursor.execute("INSERT INTO comentarios (id_usuario, nome_usuario, comentario) VALUES (?, ?, ?)",
                    (id, nome_usuario, comentario))

        conexao.commit()
        cursor.close()
        conexao.close()
        
        
    def editar_comentario(self, id):
        """
        Editar um comentario no banco de dados
        """
        limpar_tela()
        self.tabela_exists()
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, nome_usuario, comentario FROM comentarios WHERE id_usuario = {id}")

        resultados = cursor.fetchall()

        if resultados:
            printc('verde', 'Qual comentario deseja alterar? Escolha o ID: \n')
            for resultado in resultados:
                id_comentario, nome_usuario, comentario = resultado
                print(f"ID: {id_comentario}\nComentário de {nome_usuario}: {comentario}\n\n")
                
            id_editar = str(input("ID do comentário que deseja editar: "))
            novo_comentario = str(input("Novo Comentario: "))
            
            cursor.execute("UPDATE comentarios SET comentario = ? WHERE id = ?",
                        (novo_comentario, id_editar))

            conexao.commit()
            printc('verde', 'Atualização feita!')
                
        else:
            printc('vermelho', 'Nenhum comentário feito por você foi encontrado.')
        
        cursor.close()
        conexao.close()
        
    def excluir_comentario(self, id):
        """
        Excluir um comentario
        """
        limpar_tela()
        self.tabela_exists()

        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, nome_usuario, comentario FROM comentarios WHERE id_usuario = {id}")

        resultados = cursor.fetchall()

        if resultados:
            printc('verde', 'Qual comentario deseja alterar? Escolha o ID:')
            for resultado in resultados:
                id_comentario, nome_usuario, comentario = resultado
                print(f"ID: {id_comentario}\nComentário de {nome_usuario}: {comentario}\n\n")
                
            id_comentario_excluir = int(input('ID do comentario que deseja excluir: '))
        
            consulta = "DELETE FROM comentarios WHERE id = ?"

            cursor.execute(consulta, (id_comentario_excluir,))

            conexao.commit()

            num_linhas_afetadas = cursor.rowcount

            if num_linhas_afetadas > 0:
                printc("verde", "O comentário foi excluído com sucesso.")
            else:
                printc("amarelo", "Nenhum comentário foi excluído")
                
        else:
            printc("vermelho", 'Nenhum comentário seu foi encontrado.')
            
        cursor.close()
        conexao.close()
        
        
    def tabela_exists(self):
        """
        Cria a tabela comentarios caso nao exista
        """
        limpar_tela()
        conexao = sqlite3.connect('app.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='comentarios'")
        
        tabela_existe = cursor.fetchone()
        
        if not tabela_existe:
            conexao = sqlite3.connect('app.db')

            cursor = conexao.cursor()

            comando_sql = '''CREATE TABLE comentarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_usuario INTEGER,
                                nome_usuario TEXT,
                                comentario TEXT
                            )'''
                            
            cursor.execute(comando_sql)

        cursor.close()
        conexao.close()
        