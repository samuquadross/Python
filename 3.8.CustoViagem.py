n = float(input('Qual a distância da sua viagem? '))
r = n * 0.50
m = n * 0.45
print('\033[33m============= TABELA DE PREÇO =============')
print('Viagens abaixo de 200km: 0.50 €/km ')
print('Viagens acima de 200km: 0.45 €/km')
print('\033[33m===========================================')
if n <= 200.0:
    print('\033[32mO preço da viagem será: {}€'.format(r))
else:
    print('\033[32mO preço da viagem será: {}€'.format(m))
