import sqlite3

class Receitas:
    def __init__(self):
        pass
    
    def visualizar_receitas(self):
        """
        Visualizar receitas disponíveis
        """
        self.tabela_exists()
        conexao = sqlite3.connect('app.db')
        
        # Criando o cursor
        cursor = conexao.cursor()

        # Executando a consulta
        cursor.execute("SELECT nome_autor, nome_receita, receita FROM receitas")

        # Obtendo os resultados
        resultados = cursor.fetchall()

        # Exibindo os resultados
        print('Receitas disponíveis: ')
        for resultado in resultados:
            nome_autor, nome_receita, receita = resultado
            print(f"Autor: {nome_autor},\n Nome da receita: {nome_receita},\nReceita Detalhada: {receita}")
        # Fechando a conexão
        conexao.close()
        
    def adicionar_receita(self):
        """
        Adiconando uma receita no banco de dados
        """
        conexao = sqlite3.connect('app.db')
        
        # Criando o cursor
        cursor = conexao.cursor()

        # Dados da nova receita
        nome_autor = str(input("Nome do autor da Receita: "))
        nome_receita = str(input("Nome da Receita: "))
        receita = str(input("Descrição da Receita: "))

        # Executando a instrução de inserção
        cursor.execute("INSERT INTO receitas (nome_autor, nome_receita, receita) VALUES (?, ?, ?)",
                    (nome_autor, nome_receita, receita))

        # Commit para salvar as alterações
        conexao.commit()

        # Fechando a conexão
        conexao.close()
        
        
    def editar_receita(self):
        """
        Editar uma receita no banco de dados
        """
        # Conectando ao banco de dados
        conexao = sqlite3.connect('app.db')

        # Criando o cursor
        cursor = conexao.cursor()

        # Dados atualizados da receita
        nome_receita = str(input("Nome da Receita que deseja alterar: "))
        nome_autor = str(input("Novo Autor da Receita: "))
        nova_receita = str(input("Nova descrição da receita: "))

        # Executando a instrução de atualização
        cursor.execute("UPDATE receitas SET nome_autor = ?, receita = ? WHERE nome_receita = ?",
                    (nome_autor, nova_receita, nome_receita))

        # Commit para salvar as alterações
        conexao.commit()

        # Fechando a conexão
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
            # Caso a tabela não exista, criar o banco de dados e a tabela
            # Conectar ao banco de dados SQLite
            conexao = sqlite3.connect('app.db')

            # Criar um cursor para executar comandos SQL
            cursor = conexao.cursor()

            # Criar a tabela de usuários
            comando_sql = '''CREATE TABLE receitas (
                                nome_autor TEXT,
                                nome_receita TEXT,
                                receita TEXT
                            )'''
            cursor.execute(comando_sql)

        # Fechar a conexão e o cursor
        cursor.close()
        conexao.close()
        