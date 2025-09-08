print('========== Número Primo ==========')
num = int(input("Digite um número: "))
r = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[32m ", end='')
        r += 1
    else:
        print("\033[31m", end='')
    print("{} ".format(i), end="")
print('\n\033[0m==================================')
print('O numero \033[4;34m{}\033[0m foi divisível \033[4;34m{}\033[0m vezes'.format(num, r))
if r == 2:
    print('\033[32mE por isso ele é PRIMO!\033[0m')
else:
    print('\033[31mE por isso ele NÃO É PRIMO!\033[0m')
