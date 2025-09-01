from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3   )
print('\033[34m========= PEDRA PAPEL TESOURA =========\033[0m')
print('[ 1 ] Pedra \U0001FAA8')
print('[ 2 ] Papel \U0001F5C5')
print('[ 3 ] Tesoura \U00002702\U0000FE0F')
j = int(input('Escolha sua jogada: '))

if j == '1':
    print('O computador escolheu \033[4;034m{}\033[0m'.format(itens[computador]))
elif j == '2':
    print('O computador escolheu \033[4;034m{}\033[0m'.format(itens[computador]))
elif j == '3':
    print('O computador escolheu \033[4;034m{}\033[0m'.format(itens[computador]))

if computador == 1:  #Computador pedra
    if j == 1:
        print('\033[4;33mEmpate\033[0m')
    elif j == 2:
        print('\033[4;32mVocê venceu\033[0m')
    elif j == 3:
        print('\033[4;31mVocê perdeu\033[0m')
    else:
        print('\033[1;31m[ERRO]\033[0m')

elif computador == 2: # Computador papel
    if j == 1:
        print('\033[4;31mVocê perdeu\033[0m')
    elif j == 2:
        print('\033[4;33mEmpate\033[0m')
    elif j == 3:
        print('\033[4;32mVocê venceu\033[0m')
    else:
        print('\033[1;31m[ERRO]\033[0m')

elif computador == 3: # Computador tesoura
    if j == 1:
        print('\033[4;32mVocê venceu\033[0m')
    elif j == 2:
        print('\033[4;31mVocê perdeu\033[0m')
    elif j == 3:
        print('\033[4;33mEmpate\033[0m')
    else:
        print('\033[31m[ERRO]\033[0m')
