import unicodedata
v = int(input('Qual a velocidade atual do carro? '))
k = float(input('Quantos Km´s você rodou? '))
m = k * 7
print('='*34)
if v >= 80:
    print('\U000026A0\U0000FE0F Você ultrapassou o limite de velocidade!\U000026A0\U0000FE0F')
    print('Total a pagar sobre a multa: {:.2f} €'.format(m))
else:
    print('Nenhum limite de velocidade foi ultrapassado!')
print('='*34)