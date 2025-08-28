print('\033[33mEscolha uma das bases de conversão:'
      '\n[ 1 ] Converter para BINÁRIO'
      '\n[ 2 ] Converter para OCTAL'
      '\n[ 3 ] Converter para HEXADECIMAL\033[0m')
op = int(input('Opção: '))
if op == 1:
    print('\033[33m============= BINÁRIO =============\033[0m')
    n1 = int(input('Digite o número: '))
    print('{} convertido para binário: {}'.format(n1, bin(n1)))
elif op == 2:
    print('\033[33m============= OCTAL =============\033[0m')
    n2 = int(input('Digite o número: '))
    print('{} convertido para octal: {}'.format(n2, oct(n2)))
elif op == 3:
    print('\033[33m============= HEXADECIMAL =============\033[0m')
    n3 = int(input('Digite o número: '))
    print('{} convertido para hexadecimal: {}'.format(n3, hex(n3)))

