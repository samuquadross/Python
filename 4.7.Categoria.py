n = int(input('Ano de nascimento: '))
idade = (2025-n)
print('Você possui \033[1;32m{}\033[m anos de idade'.format(idade))
if idade <= 9:
    print('Categoria: \033[1;32mMirim \033[m')
elif idade <= 14:
    print('Categoria: \033[1;32mInfantil \033[m')
elif idade <= 19:
    print('Categoria: \033[1;32mJunior\033[m')
elif idade <= 25:
    print('Categoria: \033[1;32mSênior \033[m')
elif idade > 30:
    print('Categoria: \033[1;32mMaster \033[m')
