from datetime import date

totmaior = 0
totmenor = 0
for pess in range(1,8):
    atual = date.today().year
    nasc = int(input('Em que ano a {}ª pressoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('=================================')
print('Ao todo existem: '
      '\n\033[4;32m{}\033[0m pessoa(s) maior(es) de idade'
      '\n\033[4;32m{}\033[0m pessoa(s) menor(es) de idade '.format(totmaior, totmenor))


