import os

while True:
    print('Pesquisar no Google ou digitar URL')
    pesquisa = str(input())
    print('Aguarde, Carregando... ')
    os.startfile('https://www.google.com/search?q={}'.format(pesquisa))
