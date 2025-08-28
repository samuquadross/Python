a = int(input('Ano de nascimento: '))
r = (2025-a)
print("\033[34m="*45)
print('\033[34mVocê poussui {} anos de idade'.format(r))
print('\033[34m='*45)
if r == 18:
    print('\033[32m=============================================\n'
          '\033[32mVocê já pode se alistar no exército!')
elif r < 18:
    print('\033[33m=============================================\n'
          '\033[33mVocê ainda não pode se alistar no exército!')
elif r > 18:
    print('\033[31m=============================================\n'
          '\033[31mVocê já passou do tempo de se alistar!')
print("="*45)
