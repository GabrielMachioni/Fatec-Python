import http.server
import socketserver
import json
import zipfile

from utils.funcoes_auxiliares import printc, limpar_tela
from utils.receitas import Receitas
from utils.comentarios import Comentarios

           
class Importar:
    """
    Responsável por importar dados
    """
    def __init__(self):
        self.dados = {}
    
    def recuperar_dados(self):
        """
        Recuperar dados principais do projeto
        """
        self.dados = {
            'autores_projeto': {
                'aluno_1': 'César Silva Pedro',
                'ra_aluno_1': '2840481921015',
                'aluno_2': 'Gabriel Gomes Machioni',
                'ra_aluno_2': '2840482021014'
            },
            'tema': 'Blog de Receitas',
            'objetivos': 'O projeto apresentado está utilizando a linguagem "Python" e o banco de dados "Sqlite".',
            'receitas': Receitas().get_infos_json(),
            'comentarios': Comentarios().get_infos_json()
        }
        return self.dados
        
    def criar_zip(self):
        """
        Cria zip com json
        """
        self.recuperar_dados()
        
        json_data = json.dumps(self.dados)
        
        with open('dados.json', 'w') as file:
            file.write(json_data)
            
        with zipfile.ZipFile('dados.zip', 'w') as zip_file:
            zip_file.write('dados.json')
    
    def importar_url(self):
        self.criar_zip()
        
        class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
            def do_POST(self):
                if self.path == '/export':
                    self.send_response(200)
                    self.end_headers()
                        
                    printc("verde", "Dados exportados com sucesso.")
        
        with socketserver.TCPServer(("", 8000), MyRequestHandler) as httpd:
            printc("verde", "Servidor rodando em: http://localhost:8000/")
            
            httpd.serve_forever()
            