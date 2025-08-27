s = float(input('Qual seu salário atual: '))
a10 = 10
a15 = 15
r10 = s + (s * a10/100)
r15 = s + (s * a15/100)

print('\033[33m======================= TABELA =======================')
print('Salários superiores á 1250.00€ recebem 10% de aumento')
print('Salários inferiores á 1250.00€ recebem 15% de aumento')
print('======================================================')

if s >= 1250.00:
    print('\033[34mSeu aumento foi de {}%'.format(a10))
    print('\033[32mSalário: {}€'.format(r10))
else :
    print('\033[34mSeu aumento foi de {}%'.format(a15))
    print('\033[32mSalário: {}€'.format(r15))