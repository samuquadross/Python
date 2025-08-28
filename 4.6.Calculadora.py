import os
while True:
    um = 1
    dois = 2
    tres = 3
    quatro = 4
    print(' ================ CALCULADORA ================')
    i = int(input(
        '\033[1;34m Selecione a operação (Digite apenas o número): \n 1. Adição \n 2. Subtração \n 3. Divisão \n 4. Multiplicação \n\033[0m R: '))
    if i == um:
        um1 = int(input(' Digite um número: '))
        um2 = int(input(' Digite outro número: '))
        s = um1 + um2
        print('\033[32m Resultado: {} + {} = {}\033[0m'.format(um1, um2, s))

    elif i == dois:
        dois1 = int(input(' Digite um número: '))
        dois2 = int(input(' Digite outro número: '))
        s = dois1 - dois2
        print('\033[32m Resultado: {} + {} = {}\033[0m'.format(dois1, dois2, s))
    elif i == tres:
        tres1 = int(input(' Digite um número: '))
        tres2 = int(input(' Digite outro número: '))
        s = tres1 / tres2
        print('\033[32m Resultado: {} + {} = {}\033[0m'.format(tres1, tres2, s))
    elif i == quatro:
        quatro1 = int(input(' Digite um número: '))
        quatro2 = int(input(' Digite outro número: '))
        s = quatro1 * quatro2
        print('\033[32m Resultado: {} + {} = {}\033[0m'.format(quatro1, quatro2, s))
    else:
        print("\033[31m Opção inválida\033[0m")


    again = input('\n ==================================================='
                  '\n Deseja continuar? (5 para continuar | 6 para sair): ').lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if again != '5':
        print('Programa finalizado.')
        break
