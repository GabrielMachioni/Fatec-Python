import http.server
import socketserver
import json
import zipfile

from utils.funcoes_auxiliares import printc, limpar_tela

           
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
                'aluno_1': '',
                'aluno_2': ''
            },
            'receitas': [],
            'conta_logada': {
                'nome': '',
                'id': 0
            }
        }
        
    def criar_zip(self):
        # Exportar dados para JSON
        json_data = json.dumps(self.dados)
        # Criar arquivo JSON
        with open('dados.json', 'w') as file:
            file.write(json_data)
            
        # Compactar arquivo JSON em um arquivo zip
        with zipfile.ZipFile('dados.zip', 'w') as zip_file:
            zip_file.write('dados.json')
    
    def importar_url(self):
        class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
            def do_POST(self):
                if self.path == '/export':
                    content_length = int(self.headers.get('Content-Length'))
                    post_data = self.rfile.read(content_length)
                    self.send_response(200)
                    self.end_headers()
                    with open('dados.zip', 'wb') as file:
                        file.write(post_data)
                    print("Dados exportados com sucesso.")
        
        # Inicia o servidor local
        with socketserver.TCPServer(("", 8000), MyRequestHandler) as httpd:
            print(f"Servidor rodando em http://localhost:8000/")
            httpd.serve_forever()
            