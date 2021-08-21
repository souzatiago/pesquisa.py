import subprocess as s

while True:
    print('Pesquisar no Google ou digitar URL')
    pesquisa = str(input())
    print('Aguarde, Carregando...')
    s.Popen(['xdg-open', 'http://www.google.com/search?q={}'.format(entrada)])
