import os
from time import sleep

from usuario.cadastro import criar_cadastro
from utils.sobre import informacao_projeto

while True:
    print(
"""
1 - Login
2 - Cadastrar
3 - Sobre

9 - Sair
""")

    op = int(input('Escolha uma opção: '))

    if op in [1, 2, 3, 9]:
        break
    
    os.system('cls')
    print('Opção Inválida!')
    sleep(2)
    
    
if op == 1:
    #login()
    ...
    
elif op == 2:
    criar_cadastro()
    
elif op == 3:
    informacao_projeto()
    
else:
    exit()
    
