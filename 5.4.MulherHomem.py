C = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
while C not in 'MmFf':
    C = str(input('\033[33m!! DIGITE APENAS ENTRE [M/F] !!\033[0m'
                  '\nQual seu sexo? [M/F]: ')).strip().upper()[0]
if C == 'M':
    print('Você é do sexo Masculino')
elif C == 'F':
    print('Você é do sexo Feminino')

