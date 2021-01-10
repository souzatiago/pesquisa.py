import os
import time

while True:

    print('Pesquisar no Google ou digitar URL')
    pesquisa = str(input())
    print('Aguarde, Carregando... ')
    time.sleep(1)
    os.startfile('https://www.google.com/search?q={}'.format(pesquisa))
