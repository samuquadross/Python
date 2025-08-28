a = int(input('Ano de nascimento: '))
r = (2025-a)

if a > 2025 or a < 1875:
    print('Introduza um ano válido!')
    exit()
else:
    print('Você possui {} anos de idade'.format(r))
if r == 18:
    print('\033[32mVocê já pode se alistar no exército!')
elif r < 18:
    print('\033[33mVocê ainda não pode se alistar no exército!')
    print('\033[33mFaltam {} anos'.format(18-r))
elif r > 18:
    print('\033[31mVocê já passou do tempo de se alistar!')
    
