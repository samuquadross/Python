import random
print('============== JOGO DE ADIVINHAÇÃO ==============')
num = int(input('Escolha um número entre 0 e 5: '))
r = random.randint(0,5)
if num == r:
    print('Parabéns você acertou!')
else:
    print('Você perdeu!')