import sqlite3

from utils.funcoes_auxiliares import printc, limpar_tela

class Receitas:
    def __init__(self):
        pass
    
    def get_infos_json(self):
        """
        Cria uma lista de dicionarios com todas as informações de receitas
        """
        self.tabela_exists()
        
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        cursor.execute("SELECT nome_autor, nome_receita, receita FROM receitas")
        
        resultados = cursor.fetchall()
        dados = []
        
        for resultado in resultados:
            nome_autor, nome_receita, receita = resultado
            dados.append(
                {'nome_autor': nome_autor,
                 'nome_receita': nome_receita,
                 'receita': receita}
            )
            
        return dados
        
    
    def visualizar_receitas(self):
        """
        Visualizar receitas disponíveis
        """
        self.tabela_exists()
        conexao = sqlite3.connect('app.db')
        
        
        cursor = conexao.cursor()
        cursor.execute("SELECT nome_autor, nome_receita, receita FROM receitas")

        resultados = cursor.fetchall()

        printc('verde', 'Receitas disponíveis: \n')
        for resultado in resultados:
            nome_autor, nome_receita, receita = resultado
            print(f"Autor: {nome_autor}\nNome da receita: {nome_receita}\nReceita Detalhada: {receita}\n\n")
        
        conexao.close()
        
    def adicionar_receita(self):
        """
        Adiconando uma receita no banco de dados
        """
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()

        nome_autor = str(input("Nome do autor da Receita: "))
        nome_receita = str(input("Nome da Receita: "))
        receita = str(input("Descrição da Receita: "))

        cursor.execute("INSERT INTO receitas (nome_autor, nome_receita, receita) VALUES (?, ?, ?)",
                    (nome_autor, nome_receita, receita))

        conexao.commit()
        conexao.close()
        
        
    def editar_receita(self):
        """
        Editar uma receita no banco de dados
        """
        conexao = sqlite3.connect('app.db')

        cursor = conexao.cursor()
        
        printc('amarelo', 'Digite o nome da receita correto, caso contrário não será feita nenhuma alteração!')

        nome_receita = str(input("Nome da Receita que deseja alterar: "))
        nome_autor = str(input("Novo Autor da Receita: "))
        nova_receita = str(input("Nova descrição da receita: "))

        cursor.execute("UPDATE receitas SET nome_autor = ?, receita = ? WHERE nome_receita = ?",
                    (nome_autor, nova_receita, nome_receita))

        conexao.commit()
        conexao.close()
        
        
    def tabela_exists(self):
        """
        Cria a tabela receita caso nao exista
        """
        conexao = sqlite3.connect('app.db')
        
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='receitas'")
        
        tabela_existe = cursor.fetchone()
        
        if not tabela_existe:
            conexao = sqlite3.connect('app.db')

            cursor = conexao.cursor()

            comando_sql = '''CREATE TABLE receitas (
                                nome_autor TEXT,
                                nome_receita TEXT,
                                receita TEXT
                            )'''
                            
            cursor.execute(comando_sql)

        cursor.close()
        conexao.close()
        