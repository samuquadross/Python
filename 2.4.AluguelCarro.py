d = int(input('Quantos dias o automóvel foi usado? '))
k = int(input('Quantos KM rodados? '))
r1 = d * 60
r2 = k * 0.15
r3 = r1 + r2
print('='*12)
print('O total a se pagar é: {}€\n{}€ de diária \n{:.2f}€ de KM rodados'.format(r3, r1, r2))
print('='*12)
