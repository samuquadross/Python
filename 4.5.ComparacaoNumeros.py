print('========================================')
n = int(input('Digite um numero: '))
r = int(input('Digite um numero: '))
print('========================================')

if n > r:
    print('\033[32m{} é o primeiro maior número'.format(n))
elif r > n:
    print('\033[32m{} é o segundo maior número'.format(r))
elif n > r:
    print('\033[32m{} é o segundo maior número'.format(n))
elif r > n:
    print('\033[32m{} é o primeiro maior número'.format(r))
elif n == r:
    print('\033[31mNão existe maior, pois os números são iguais')
elif r == n:
    print('\033[31mNão existe maior, pois os números são iguais')
