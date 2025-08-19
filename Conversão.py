c = int(input('Quanto você tem na conta? €'  ))
real = c * 6.40
dolar = c * 1.17
print('='* 12)
print('Com {}€ você pode comprar: \nR$ {:.1f}\n$ {:.1f}'.format(c, real, dolar))
print('='* 12)