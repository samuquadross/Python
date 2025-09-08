print('\033[1;33m========== Número Primo ==========\033[0m')
num = int(input("Digite um número: "))
r = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[32m ", end='')
        r += 1
    else:
        print("\033[31m", end='')
    print("{} ".format(i), end="")
print('\n\033[1;33m==================================\033[0m')
print('\033[1;34mO numero \033[4m{}\033[0m \033[1;34mfoi divisível \033[4m{}\033[0m \033[1;34mvezes'.format(num, r))

